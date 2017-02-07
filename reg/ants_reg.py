# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os,sys                            # system functions
import nipype.interfaces.io as nio           # Data i/o
import nipype.interfaces.fsl as fsl          # fsl
import nipype.pipeline.engine as pe          # pypeline engine
import nipype.interfaces.utility as util     # utility
import nipype.interfaces.ants as ants
from nipype.interfaces.c3 import C3dAffineTool


fsl.FSLCommand.set_default_output_type('NIFTI_GZ')

"""
Project info
"""
template_brain = fsl.Info.standard_image('MNI152_T1_2mm_brain.nii.gz')
project_dir="/lustre/work/dpanyuko/Analysis/RuleSwitch/"
work_dir="/lustre/scratch/dpanyuko/RuleSwitch/"
if not os.path.exists(work_dir):
    os.makedirs(work_dir)

#which subjects to run
subj_list=str(sys.argv[1])


"""
Create workflow
"""

wf = pe.Workflow(name='wf')
wf.base_dir = os.path.join(work_dir,"reg_wdir")
wf.config = {"execution": {"crashdump_dir":os.path.join(work_dir,'reg_crashdumps')}}

infosource = pe.Node(interface=util.IdentityInterface(fields=['subject_id']), name="infosource")
infosource.iterables = ('subject_id', [subj_list])

def get_subjectinfo(subject_id):

    run_id=[]
    if subject_id=="Subject003" or subject_id=="Subject011" or subject_id=="Subject016" or subject_id=="Subject020":
        run_id=["2","3","4","5","6","7","8"]
    elif subject_id=="Subject019":
        run_id=["1","2","3","4","5","6"]
    else:
        run_id=["1","2","3","4","5","6","7","8"]
        
    return subject_id, run_id

subjinfo = pe.Node(util.Function(input_names=['subject_id'],
                                output_names=['subject_id','run_id'],
                                function=get_subjectinfo),
                       name='subjectinfo')

subjinfo.inputs.base_dir = project_dir
wf.connect([(infosource, subjinfo, [('subject_id', 'subject_id')]),])


datasource = pe.Node(nio.DataGrabber(infields=['subject_id','run_id'], outfields=['func', 'anat']), name='datasource')
datasource.inputs.base_directory = project_dir
datasource.inputs.template = '*'
datasource.inputs.field_template = dict(func='%s/bold/run%s/run*_mcf_brain.nii.gz',
                                        anat='%s/anatomy/highres001_BrainExtractionBrain.nii.gz')
datasource.inputs.template_args = dict(func=[['subject_id','run_id']],
                                       anat=[['subject_id']])
datasource.inputs.sort_filelist=True

wf.connect(subjinfo, 'subject_id', datasource, 'subject_id')
wf.connect(subjinfo, 'run_id', datasource, 'run_id')

"""
Setup preprocessing workflow
----------------------------


Set up a node to define all inputs required for the preprocessing workflow
"""

inputnode = pe.Node(interface=util.IdentityInterface(fields=['func',
                                                             'anat',]),
                    name='inputspec')

wf.connect([(datasource, inputnode, [('anat','anat'),('func', 'func'),]),])

"""
Convert functional images to float representation. Since there can be more than
one functional run we use a MapNode to convert each run.
"""

prefiltered_func_data = pe.MapNode(interface=fsl.ImageMaths(out_data_type='float',
                                             op_string = '',
                                             suffix='_dtype'),
                       iterfield=['in_file'],
                       name='prefiltered_func_data')

wf.connect(inputnode, 'func', prefiltered_func_data, 'in_file')

"""
Extract the middle volume of the run as the reference
"""

example_func = pe.MapNode(interface=fsl.ExtractROI(t_size=1),
                          iterfield=['in_file'],
                          name = 'example_func')

"""
Define a function to return the 1 based index of the middle volume
"""

def getmiddlevolume(func):
    from nibabel import load
    funcfile = func
    if isinstance(func, list):
        funcfile = func[0]
    _,_,_,timepoints = load(funcfile).get_shape()
    return (timepoints/2)-1

wf.connect(prefiltered_func_data, 'out_file', example_func, 'in_file')
wf.connect(inputnode, ('func', getmiddlevolume), example_func, 't_min')

"""
Registration
------------
"""

"""
---ANTs---
"""
reg = pe.Node(ants.Registration(), name='antsRegister')
reg.inputs.output_transform_prefix = "output_"
reg.inputs.transforms = ['Rigid', 'Affine', 'SyN']
reg.inputs.transform_parameters = [(0.1,), (0.1,), (0.2, 3.0, 0.0)]
reg.inputs.number_of_iterations = [[100000, 111100, 111100]] * 2 + [[1000, 300, 200]]
reg.inputs.dimension = 3
reg.inputs.write_composite_transform = True
reg.inputs.collapse_output_transforms = True
reg.inputs.initial_moving_transform_com = True
reg.inputs.metric = ['Mattes'] * 2 + [['Mattes', 'CC']]
reg.inputs.metric_weight = [1] * 2 + [[0.5, 0.5]]
reg.inputs.radius_or_number_of_bins = [32] * 2 + [[32, 4]]
reg.inputs.sampling_strategy = ['Regular'] * 2 + [[None, None]]
reg.inputs.sampling_percentage = [0.3] * 2 + [[None, None]]
reg.inputs.convergence_threshold = [1.e-8] * 2 + [-0.01]
reg.inputs.convergence_window_size = [20] * 2 + [5]
reg.inputs.smoothing_sigmas = [[4, 2, 1]] * 2 + [[1, 0.5, 0]]
reg.inputs.sigma_units = ['vox'] * 3
reg.inputs.shrink_factors = [[3, 2, 1]]*2 + [[4, 2, 1]]
reg.inputs.use_estimate_learning_rate_once = [True] * 3
reg.inputs.use_histogram_matching = [False] * 2 + [True]
reg.inputs.winsorize_lower_quantile = 0.005
reg.inputs.winsorize_upper_quantile = 0.995
reg.inputs.args = '--float'
reg.inputs.output_warped_image = 'output_warped_image.nii.gz'
reg.inputs.num_threads = 12

reg.inputs.fixed_image=template_brain
wf.connect(inputnode, 'anat', reg, 'moving_image')

"""
---Func registration---
"""

"""
Estimate the tissue classes from the anatomical image.
"""

fast = pe.Node(fsl.FAST(), name='fast')

"""
Binarize the segmentation
"""

binarize = pe.Node(fsl.ImageMaths(op_string='-nan -thr 0.5 -bin'),
                   name='binarize')
pickindex = lambda x, i: x[i]

wf.connect(inputnode, 'anat', fast, 'in_files')
wf.connect(fast, ('partial_volume_files', pickindex, 2), binarize, 'in_file')

"""
Calculate rigid transform from example_func image to anatomical image
"""

func2anat = pe.MapNode(fsl.FLIRT(), iterfield=['in_file'], name='func2anat')
func2anat.inputs.dof = 6

wf.connect(example_func, 'roi_file', func2anat, 'in_file')
wf.connect(inputnode, 'anat', func2anat, 'reference')

"""
Now use bbr cost function to improve the transform
"""

func2anatbbr = pe.MapNode(fsl.FLIRT(), iterfield=['in_file','in_matrix_file'], name='func2anatbbr')
func2anatbbr.inputs.dof = 6
func2anatbbr.inputs.cost = 'bbr'
func2anatbbr.inputs.schedule = os.path.join(os.getenv('FSLDIR'),'etc/flirtsch/bbr.sch')

wf.connect(example_func, 'roi_file', func2anatbbr, 'in_file')
wf.connect(binarize, 'out_file', func2anatbbr, 'wm_seg')
wf.connect(inputnode, 'anat', func2anatbbr, 'reference')
wf.connect(func2anat, 'out_matrix_file', func2anatbbr, 'in_matrix_file')

"""
Convert the BBRegister transformation to ANTS ITK format
"""

convert2itk = pe.MapNode(C3dAffineTool(), iterfield=['source_file','transform_file'], name='convert2itk')
convert2itk.inputs.fsl2ras = True
convert2itk.inputs.itk_transform = True

wf.connect(func2anatbbr, 'out_matrix_file', convert2itk, 'transform_file')
wf.connect(example_func, 'roi_file',convert2itk, 'source_file')
wf.connect(inputnode, 'anat', convert2itk, 'reference_file')

"""
Concatenate the affine and ants transforms into a list
"""

merge = pe.MapNode(util.Merge(2), iterfield=['in2'], name='mergexfm')

wf.connect(convert2itk, 'itk_transform', merge, 'in2')
wf.connect(reg, 'composite_transform', merge, 'in1')

"""
Transform the mean image. First to anatomical and then to target
"""

warp_func = pe.MapNode(ants.ApplyTransforms(), iterfield=['input_image','transforms'], name='warp_func')
warp_func.inputs.input_image_type = 0
warp_func.inputs.interpolation = 'Linear'
warp_func.inputs.invert_transform_flags = [False, False]
warp_func.inputs.terminal_output = 'file'

wf.connect(example_func, 'roi_file', warp_func, 'input_image')
wf.connect(merge, 'out', warp_func, 'transforms')
warp_func.inputs.reference_image = template_brain

"""
Save data
"""

datasink = pe.Node(nio.DataSink(), name='sinker')
datasink.inputs.base_directory=os.path.join(project_dir, "reg")

wf.connect(subjinfo, 'subject_id', datasink, 'container')
wf.connect(reg, 'warped_image', datasink, 'anatomy.anat2standard')
wf.connect(reg, 'composite_transform', datasink, 'anatomy.anat2standard_mat')
wf.connect(warp_func, 'output_image', datasink, 'bold.func2standard')
wf.connect(func2anatbbr, 'out_matrix_file', datasink, 'bold.func2anat_transform')
wf.connect(merge, 'out', datasink, 'bold.func2standard_mat')
wf.connect(example_func, 'roi_file', datasink, 'bold.example_func')

"""
Run
"""
outgraph = wf.run(plugin='MultiProc')
