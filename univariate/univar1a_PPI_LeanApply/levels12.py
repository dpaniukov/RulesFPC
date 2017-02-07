#!/usr/bin/env python

import os
import sys                          # system functions
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
# Subject to run
subj_list = str(sys.argv[1])
project_dir = "/mnt/net/LaCie/Analysis/RuleSwitch/"
work_dir = "/mnt/net/LaCie/scratch/RuleSwitch/"

model_id = '_univar1a_PPI_LearnApply'
task_id = 1
TR = 2.0
fwhm_thr = 8.0
hpcutoff = 100
film_thr = 1000  # default in FSL
film_ms = 5  # this should be Susan mask size, not fwhm
template_brain = fsl.Info.standard_image('MNI152_T1_2mm_brain.nii.gz')

wf = pe.Workflow(name='wf')
wf.base_dir = os.path.join(work_dir, "wdir" + str(model_id) + "lvl12")
wf.config = {"execution": {"crashdump_dir": os.path.join(project_dir, 'crashdumps')}}

infosource = pe.Node(interface=util.IdentityInterface(fields=['subject_id']), name="infosource")
infosource.iterables = ('subject_id', [subj_list])


def get_subjectinfo(subject_id, base_dir, task_id, model_id):
    #from glob import glob
    import os
    import numpy as np

    if subject_id == "Subject003" or subject_id == "Subject011" or subject_id == "Subject016" or subject_id == "Subject020":
        run_id = [2, 3, 4, 5, 6, 7, 8]
        itk_id = list(np.array(run_id) - 2)
        evs_l2 = dict(ev001=[1, 1, 1, 0, 0, 0, 0], ev002=[0, 0, 0, 1, 1, 1, 1])
    elif subject_id == "Subject019":
        run_id = [1, 2, 3, 4, 5, 6]
        itk_id = list(np.array(run_id) - 1)
        evs_l2 = dict(ev001=[1, 1, 1, 1, 0, 0], ev002=[0, 0, 0, 0, 1, 1])
    else:
        run_id = [1, 2, 3, 4, 5, 6, 7, 8]
        itk_id = list(np.array(run_id) - 1)
        evs_l2 = dict(ev001=[1, 1, 1, 1, 0, 0, 0, 0], ev002=[0, 0, 0, 0, 1, 1, 1, 1])

    # Conditions for level 2
    condition_info_l2 = []
    cond_file_l2 = os.path.join(base_dir, 'models', 'model%s' % model_id,
                                'condition_key_l2.txt')
    with open(cond_file_l2, 'rt') as fp_l2:
        for line in fp_l2:
            info_l2 = line.strip().split()
            condition_info_l2.append([info_l2[0], info_l2[1], ' '.join(info_l2[2:])])
    if len(condition_info_l2) == 0:
        raise ValueError('No condition info found in %s' % cond_file_l2)
    taskinfo_l2 = np.array(condition_info_l2)
    n_tasks_l2 = len(np.unique(taskinfo_l2[:, 0]))
    conds_l2 = []
    if task_id > n_tasks_l2:
        raise ValueError('Task id %d does not exist' % task_id)
    for idx in range(n_tasks_l2):
        taskidx_l2 = np.where(taskinfo_l2[:, 0] == 'task%03d' % (idx + 1))
        conds_l2.append([condition_l2.replace(' ', '_') for condition_l2
                         in taskinfo_l2[taskidx_l2[0], 2]])

    return subject_id, model_id, task_id, run_id, itk_id, evs_l2, conds_l2[task_id - 1],

subjinfo = pe.Node(util.Function(input_names=['subject_id', 'base_dir', 'task_id', 'model_id'],
                                 output_names=['subject_id', 'model_id', 'task_id',
                                               'run_id', 'itk_id', 'evs_l2', 'conds_l2'],
                                 function=get_subjectinfo),
                   name='subjectinfo')
subjinfo.inputs.base_dir = project_dir
subjinfo.inputs.task_id = task_id
subjinfo.inputs.model_id = model_id

datasource = pe.Node(nio.DataGrabber(infields=['subject_id', 'model_id', 'task_id', 'run_id', 'itk_id'], outfields=[
                     'copes', 'varcopes', 'masks', 'contrasts_l2', 'itk_transform', 'composite_transform']), name='grabber')
datasource.inputs.base_directory = project_dir
datasource.inputs.template = '*'
datasource.inputs.field_template = dict(copes='%s/model/run%d_level1%s.feat/stats/cope*.nii.gz',
                                        varcopes='%s/model/run%d_level1%s.feat/stats/varcope*.nii.gz',
                                        masks='%s/model/run%d_level1%s.feat/mask.nii.gz',
                                        contrasts_l2='models/model%s/task_contrasts_l2.txt',
                                        itk_transform='reg/%s/bold/func2standard_mat/_subject_id_%s/_convert2itk%d/affine.txt',
                                        composite_transform='reg/%s/anatomy/anat2standard_mat/_subject_id_%s/output_Composite.h5')
datasource.inputs.template_args = dict(copes=[['subject_id', 'run_id','model_id']],
                                       varcopes=[['subject_id', 'run_id','model_id']],
                                       masks=[['subject_id', 'run_id','model_id']],
                                       contrasts_l2=[['model_id']],
                                       itk_transform=[['subject_id', 'subject_id', 'itk_id']],
                                       composite_transform=[['subject_id', 'subject_id']])
datasource.inputs.sort_filelist = True

wf.connect([(infosource, subjinfo, [('subject_id', 'subject_id')]), ])
wf.connect(subjinfo, 'subject_id', datasource, 'subject_id')
wf.connect(subjinfo, 'model_id', datasource, 'model_id')
wf.connect(subjinfo, 'task_id', datasource, 'task_id')
wf.connect(subjinfo, 'run_id', datasource, 'run_id')
wf.connect(subjinfo, 'itk_id', datasource, 'itk_id')


"""
Level 2
-----------------------------

Apply Registration

Here we merge copes, varcopes, masks and transformation matrices for each run to register them appropriately.
Then we split them back to merge in time and use in flameo.
"""

"""
Merge transforms
"""

merge_mat = pe.MapNode(util.Merge(2), iterfield=['in2'], name='merge_mat')

wf.connect(datasource, 'itk_transform', merge_mat, 'in2')
wf.connect(datasource, 'composite_transform', merge_mat, 'in1')


def warp_files(copes, varcopes, masks, mat, template_brain):
    import nipype.interfaces.ants as ants

    out_copes = []
    out_varcopes = []
    out_masks = []

    warp = ants.ApplyTransforms()
    warp.inputs.input_image_type = 0
    warp.inputs.interpolation = 'Linear'
    warp.inputs.invert_transform_flags = [False, False]
    warp.inputs.terminal_output = 'file'
    warp.inputs.reference_image = template_brain
    warp.inputs.transforms = mat

    warp.inputs.input_image = masks
    res = warp.run()
    out_masks.append(str(res.outputs.output_image))

    for cope in copes:
        warp.inputs.input_image = cope
        res = warp.run()
        out_copes.append(str(res.outputs.output_image))

    for varcope in varcopes:
        warp.inputs.input_image = varcope
        res = warp.run()
        out_varcopes.append(str(res.outputs.output_image))

    return out_copes, out_varcopes, out_masks

warpfunc = pe.MapNode(util.Function(input_names=['copes', 'varcopes', 'masks', 'mat', 'template_brain'],
                                    output_names=['out_copes', 'out_varcopes', 'out_masks'],
                                    function=warp_files),
                      iterfield=['copes', 'varcopes', 'masks', 'mat'],
                      name='warpfunc')

warpfunc.inputs.template_brain = template_brain
wf.connect(datasource, 'copes', warpfunc, 'copes')
wf.connect(datasource, 'varcopes', warpfunc, 'varcopes')
wf.connect(datasource, 'masks', warpfunc, 'masks')
wf.connect(merge_mat, 'out', warpfunc, 'mat')


"""
Use :class:`nipype.interfaces.fsl.Merge` to merge the copes and
varcopes for each condition
"""

copemerge = pe.MapNode(interface=fsl.Merge(dimension='t'),
                       iterfield=['in_files'],
                       name="copemerge")

varcopemerge = pe.MapNode(interface=fsl.Merge(dimension='t'),
                          iterfield=['in_files'],
                          name="varcopemerge")

maskemerge = pe.MapNode(interface=fsl.Merge(dimension='t'),
                        iterfield=['in_files'],
                        name="maskemerge")


def sort_copes(files):
    numelements = len(files[0])
    outfiles = []
    for i in range(numelements):
        outfiles.insert(i, [])
        for j, elements in enumerate(files):
            outfiles[i].append(elements[i])
    return outfiles

wf.connect(warpfunc, ('out_copes', sort_copes), copemerge, 'in_files')
wf.connect(warpfunc, ('out_varcopes', sort_copes), varcopemerge, 'in_files')
wf.connect(warpfunc, ('out_masks', sort_copes), maskemerge, 'in_files')

"""
Setup a set of contrasts for level 2
"""


def get_contrasts_l2(contrast_file, task_id, conds):
    import numpy as np
    contrast_def = np.genfromtxt(contrast_file, dtype=object)
    if len(contrast_def.shape) == 1:
        contrast_def = contrast_def[None, :]
    contrasts = []
    for row in contrast_def:
        if row[0] != 'task%03d' % task_id:
            continue
        con = [row[1], 'T', ['ev%03d' % (i + 1) for i in range(len(conds))],
               row[2:].astype(float).tolist()]
        contrasts.append(con)
    return contrasts

contrastgen_l2 = pe.Node(util.Function(input_names=['contrast_file',
                                                    'task_id', 'conds'],
                                       output_names=['contrasts'],
                                       function=get_contrasts_l2),
                         name='contrastgen_l2')

wf.connect(subjinfo, 'conds_l2', contrastgen_l2, 'conds')
wf.connect(datasource, 'contrasts_l2', contrastgen_l2, 'contrast_file')
wf.connect(subjinfo, 'task_id', contrastgen_l2, 'task_id')

"""
Use MultipleRegressDesign to generate subject and condition
specific level 2 model design files
"""
level2model = pe.Node(interface=fsl.MultipleRegressDesign(),
                      name='l2model')

wf.connect(contrastgen_l2, 'contrasts', level2model, 'contrasts')
wf.connect(subjinfo, 'evs_l2', level2model, 'regressors')

"""
Use :class:`nipype.interfaces.fsl.FLAMEO` to estimate a second level model
"""

flameo = pe.MapNode(interface=fsl.FLAMEO(run_mode='fe'), name="flameo",
                    iterfield=['cope_file', 'var_cope_file'])

pickfirst = lambda x: x[0]

wf.connect([(copemerge, flameo, [('merged_file', 'cope_file')]),
            (varcopemerge, flameo, [('merged_file', 'var_cope_file')]),
            (level2model, flameo, [('design_mat', 'design_file'),
                                   ('design_con', 't_con_file'),
                                   ('design_grp', 'cov_split_file')]),
            (maskemerge, flameo, [(('merged_file', pickfirst), 'mask_file')]),
            ])


"""
Saving
"""

datasink = pe.Node(nio.DataSink(), name='sinker')
datasink.inputs.base_directory = os.path.join(project_dir, "level2s", "model" + model_id)

wf.connect(infosource, 'subject_id', datasink, 'container')
wf.connect([(flameo, datasink, [('stats_dir', 'stats_dir')])])

"""
RUN
"""

outgraph = wf.run()
