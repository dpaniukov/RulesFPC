# Registration pipeline

In this pipeline, `ants_reg.py` registers functional (only example_func volume) and anatomical images to standard space, and creates transformation matrices. Go to `ants_reg` folder and run `python ../ants_reg.py Subject001` to register Subject001, or see `/ants_reg/` folder for how to create jobs for the cluster with `maker.sh`

To check the quality of your registration, run `reg_slices.sh`. It will create a folder `reg/slices_dir` and superimpose functional runs on an MNI template.
