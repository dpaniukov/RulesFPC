#!/usr/bin/env python

import os
import sys                                  # system functions
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

# Cope from level 1
lvl1_cope = int(sys.argv[1])
# Cope from level 2
lvl2_cope = int(sys.argv[2])


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

l12_out_dir = os.path.join(project_dir, "level2s", "model" + model_id)

wf = pe.Workflow(name='wf')
wf.base_dir = os.path.join(work_dir, "wdir" + str(model_id) + "lvl3",
                           "copes_" + str(lvl1_cope) + "_" + str(lvl2_cope))
wf.config = {"execution": {"crashdump_dir": os.path.join(project_dir, 'crashdumps')}}


subj_copes = []
subj_varcopes = []
if lvl2_cope == 1:  # matching
    subj_copes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz")]

    subj_varcopes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz")]


elif lvl2_cope == 2:  # classification
    subj_copes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz"),
                  os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope1.nii.gz"),
                  os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "cope2.nii.gz")]

    subj_varcopes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz"),
                     os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope1.nii.gz"),
                     os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "varcope2.nii.gz")]

elif lvl2_cope == 3:  # matching>classification
    subj_copes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz"),
                  os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                               "_flameo" + str(lvl1_cope - 1), "stats", "cope4.nii.gz"),
                  os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "cope3.nii.gz")]

    subj_varcopes = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz"),
                     os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                                  "_flameo" + str(lvl1_cope - 1), "stats", "varcope4.nii.gz"),
                     os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "varcope3.nii.gz")]

subj_masks = [os.path.join(l12_out_dir, "Subject001", "stats_dir", "_subject_id_Subject001", "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject002", "stats_dir", "_subject_id_Subject002",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject003", "stats_dir", "_subject_id_Subject003",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject004", "stats_dir", "_subject_id_Subject004",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject005", "stats_dir", "_subject_id_Subject005",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject006", "stats_dir", "_subject_id_Subject006",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject008", "stats_dir", "_subject_id_Subject008",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject010", "stats_dir", "_subject_id_Subject010",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject011", "stats_dir", "_subject_id_Subject011",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject012", "stats_dir", "_subject_id_Subject012",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject013", "stats_dir", "_subject_id_Subject013",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject014", "stats_dir", "_subject_id_Subject014",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject015", "stats_dir", "_subject_id_Subject015",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject016", "stats_dir", "_subject_id_Subject016",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject017", "stats_dir", "_subject_id_Subject017",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject018", "stats_dir", "_subject_id_Subject018",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject019", "stats_dir", "_subject_id_Subject019",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject020", "stats_dir", "_subject_id_Subject020",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject021", "stats_dir", "_subject_id_Subject021",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject022", "stats_dir", "_subject_id_Subject022",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject023", "stats_dir", "_subject_id_Subject023",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject024", "stats_dir", "_subject_id_Subject024",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject025", "stats_dir", "_subject_id_Subject025",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject026", "stats_dir", "_subject_id_Subject026",
                           "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz"),
              os.path.join(l12_out_dir, "Subject027", "stats_dir", "_subject_id_Subject027", "_flameo" + str(lvl1_cope - 1), "stats", "mask.nii.gz")]


def get_subjectinfo(subj_list, base_dir, task_id, model_id):
    #from glob import glob
    import os
    import numpy as np

    evs_l3 = dict(ev001=[1] * len(subj_list))

    # Conditions for level 3
    condition_info = []
    cond_file = os.path.join(base_dir, 'models', 'model%s' % model_id,
                             'condition_key_l3.txt')
    with open(cond_file, 'rt') as fp:
        for line in fp:
            info = line.strip().split()
            condition_info.append([info[0], info[1], ' '.join(info[2:])])
    if len(condition_info) == 0:
        raise ValueError('No condition info found in %s' % cond_file)
    taskinfo = np.array(condition_info)
    n_tasks = len(np.unique(taskinfo[:, 0]))
    conds = []
    if task_id > n_tasks:
        raise ValueError('Task id %d does not exist' % task_id)
    for idx in range(n_tasks):
        taskidx = np.where(taskinfo[:, 0] == 'task%03d' % (idx + 1))
        conds.append([condition.replace(' ', '_') for condition
                      in taskinfo[taskidx[0], 2]])

    return task_id, evs_l3, conds[task_id - 1]

subjinfo = pe.Node(util.Function(input_names=['subj_list', 'base_dir', 'task_id', 'model_id'],
                                 output_names=['task_id', 'evs_l3', 'conds'],
                                 function=get_subjectinfo),
                   name='subjectinfo')
subjinfo.inputs.base_dir = project_dir
subjinfo.inputs.task_id = task_id
subjinfo.inputs.model_id = model_id
subjinfo.inputs.subj_list = subj_copes

datasource = pe.Node(nio.DataGrabber(
    infields=['model_id'], outfields=['contrasts_l3']), name='grabber')
datasource.inputs.base_directory = project_dir
datasource.inputs.template = '*'
datasource.inputs.field_template = dict(contrasts_l3='models/model%s/task_contrasts_l3.txt')
datasource.inputs.template_args = dict(contrasts_l3=[['model_id']])
datasource.inputs.sort_filelist = True
datasource.inputs.model_id = model_id

"""
Use :class:`nipype.interfaces.fsl.Merge` to merge the copes and
varcopes for each subject
"""

copemerge = pe.Node(interface=fsl.Merge(dimension='t'),
                    name="copemerge")

varcopemerge = pe.Node(interface=fsl.Merge(dimension='t'),
                       name="varcopemerge")

maskemerge = pe.Node(interface=fsl.Merge(dimension='t'),
                     name="maskemerge")

copemerge.inputs.in_files = subj_copes
varcopemerge.inputs.in_files = subj_varcopes
maskemerge.inputs.in_files = subj_masks

"""
Setup a set of contrasts for level 2
"""


def get_contrasts_l3(contrast_file, task_id, conds):
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

contrastgen_l3 = pe.Node(util.Function(input_names=['contrast_file',
                                                    'task_id', 'conds'],
                                       output_names=['contrasts'],
                                       function=get_contrasts_l3),
                         name='contrastgen_l3')

wf.connect(subjinfo, 'conds', contrastgen_l3, 'conds')
wf.connect(datasource, 'contrasts_l3', contrastgen_l3, 'contrast_file')
wf.connect(subjinfo, 'task_id', contrastgen_l3, 'task_id')

"""
Use MultipleRegressDesign to generate subject and condition
specific level 2 model design files
"""
level3model = pe.Node(interface=fsl.MultipleRegressDesign(),
                      name='l3model')

wf.connect(contrastgen_l3, 'contrasts', level3model, 'contrasts')
wf.connect(subjinfo, 'evs_l3', level3model, 'regressors')

"""
Saving
"""

datasink = pe.Node(nio.DataSink(), name='sinker')
datasink.inputs.base_directory = os.path.join(
    project_dir, "level3s", "model" + model_id, "copes_" + str(lvl1_cope) + "_" + str(lvl2_cope))

wf.connect(copemerge, 'merged_file', datasink, 'copes_merged')
wf.connect(level3model, 'design_con', datasink, 'design_con')
wf.connect(level3model, 'design_mat', datasink, 'design_mat')

"""
RUN
"""

outgraph = wf.run()
#outgraph = wf.run(plugin='MultiProc')
