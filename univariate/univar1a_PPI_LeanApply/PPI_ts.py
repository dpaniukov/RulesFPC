#!/usr/bin/env python

import os,sys                          # system functions
import nipype.interfaces.io as nio           # Data i/o
from nipype.interfaces.io import DataSink
import nipype.interfaces.fsl as fsl          # fsl
import nipype.interfaces.ants as ants
import nipype.pipeline.engine as pe          # pypeline engine
import nipype.interfaces.utility as util     # utility
import nipype.algorithms.modelgen as model   # model generation
import errno


fsl.FSLCommand.set_default_output_type('NIFTI_GZ')

"""
Project info
"""
#Subject to run
subj_list=str(sys.argv[1])
project_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"
work_dir="/mnt/net/LaCie/scratch/RuleSwitch/"

model_id='_univar1a_LearnApply'
task_id=1
TR=2.0
fwhm_thr=8.0
hpcutoff = 100
film_thr=1000 #default in FSL
film_ms=5 # this should be Susan mask size, not fwhm
template_brain = fsl.Info.standard_image('MNI152_T1_2mm_brain.nii.gz')

wf = pe.Workflow(name='wf')
wf.base_dir = os.path.join(work_dir,"wdir"+str(model_id)+"_PPIts")
wf.config = {"execution": {"crashdump_dir":os.path.join(project_dir,'crashdumps')}}

infosource = pe.Node(interface=util.IdentityInterface(fields=['subject_id']), name="infosource")
infosource.iterables = ('subject_id', [subj_list])

def get_subjectinfo(subject_id, base_dir, task_id, model_id):
    #from glob import glob
    import os
    import numpy as np

    if subject_id=="Subject003" or subject_id=="Subject011" or subject_id=="Subject016" or subject_id=="Subject020":
        run_id=[2,3,4,5,6,7,8]
        itk_id=list(np.array(run_id)-2)
    elif subject_id=="Subject019":
        run_id=[1,2,3,4,5,6]
        itk_id=list(np.array(run_id)-1)
    else:
        run_id=[1,2,3,4,5,6,7,8]
        itk_id=list(np.array(run_id)-1)

    return subject_id, model_id, task_id, run_id, itk_id

subjinfo = pe.Node(util.Function(input_names=['subject_id','base_dir', 'task_id', 'model_id'],
                                output_names=['subject_id','model_id','task_id','run_id','itk_id'],
                                function=get_subjectinfo),
                       name='subjectinfo')
subjinfo.inputs.base_dir = project_dir
subjinfo.inputs.task_id = task_id
subjinfo.inputs.model_id = model_id

datasource = pe.Node(nio.DataGrabber(infields=['subject_id','model_id','task_id','run_id','itk_id'], outfields=['func','itk_transform','composite_transform']), name='grabber')
datasource.inputs.base_directory = project_dir
datasource.inputs.template = '*'
datasource.inputs.field_template = dict(func='level2s/model%s/%s/filtered_func_data/_subject_id_%s/_highpass%d/run%d_mcf_brain_dtype_mask_smooth_mask_intnorm_tempfilt.nii.gz',
                                        itk_transform='reg/%s/bold/func2standard_mat/_subject_id_%s/_convert2itk%d/affine.txt',
                                        composite_transform='reg/%s/anatomy/anat2standard_mat/_subject_id_%s/output_Composite.h5')
datasource.inputs.template_args = dict(func=[['model_id','subject_id','subject_id','itk_id','run_id']],
                                        itk_transform=[['subject_id','subject_id','itk_id']],
                                        composite_transform=[['subject_id','subject_id']])
datasource.inputs.sort_filelist=True

wf.connect([(infosource, subjinfo, [('subject_id', 'subject_id')]),])
wf.connect(subjinfo, 'subject_id', datasource, 'subject_id')
wf.connect(subjinfo, 'model_id', datasource, 'model_id')
wf.connect(subjinfo, 'task_id', datasource, 'task_id')
wf.connect(subjinfo, 'run_id', datasource, 'run_id')
wf.connect(subjinfo, 'itk_id', datasource, 'itk_id')

inputnode = pe.Node(interface=util.IdentityInterface(fields=['func']),
                    name='inputspec')

wf.connect([(datasource, inputnode, [('func', 'func'),]),])

"""
Transform func_filtered_data into standard space
"""

merge = pe.MapNode(util.Merge(2), iterfield=['in2'], name='mergexfm')

wf.connect(datasource, 'itk_transform', merge, 'in2')
wf.connect(datasource, 'composite_transform', merge, 'in1')

warp_func = pe.MapNode(ants.ApplyTransforms(), iterfield=['input_image','transforms'], name='warp_func')
warp_func.inputs.input_image_type = 3
warp_func.inputs.interpolation = 'Linear'
warp_func.inputs.invert_transform_flags = [False, False]
warp_func.inputs.terminal_output = 'file'

wf.connect(inputnode, 'func', warp_func, 'input_image')
wf.connect(merge, 'out', warp_func, 'transforms')
warp_func.inputs.reference_image = template_brain


"""
Create a point at a particular location on MNI template.
This specific point is based on activation from univar1a incorrect matching right frontal pole
"""
point = pe.Node(interface=fsl.ImageMaths(op_string='-mul 0 -add 1 -roi 65 1 90 1 38 1 0 1',
                                            out_data_type='float'),
                       name='point')

point.inputs.in_file = template_brain

"""
Create a sphere of 8 mm (same as smoothing in the original model)
"""
sphere = pe.Node(interface=fsl.ImageMaths(op_string='-kernel sphere 8 -fmean -bin',
                                            out_data_type='float'),
                       name='sphere')

wf.connect(point, 'out_file', sphere, 'in_file')

"""
Extract time series means for the sphere
"""
ts_means = pe.MapNode(interface=fsl.ImageMeants(),
                       iterfield=['in_file'],
                       name='ts_means')

wf.connect(warp_func, 'output_image', ts_means, 'in_file')
wf.connect(sphere, 'out_file', ts_means, 'mask')

"""
Saving
"""

datasink = pe.Node(nio.DataSink(), name='sinker')
datasink.inputs.base_directory=os.path.join(project_dir, "level3s", "model"+model_id, "randomized")

#wf.connect(infosource, 'subject_id', datasink, 'container')
wf.connect(ts_means, 'out_file', datasink, 'ts_means')

"""
RUN
"""

outgraph = wf.run()
#outgraph = wf.run(plugin='MultiProc')
