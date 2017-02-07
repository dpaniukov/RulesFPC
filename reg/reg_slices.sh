#!/bin/csh

#This file creates slices to check registration

set proj_dir=/lustre/work/dpanyuko/Analysis/RuleSwitch/reg/
set fsl_template="/lustre/work/apps/fsl/data/standard/MNI152_T1_2mm_brain_mask.nii.gz"
set slices_dir=${proj_dir}slices_dir/
mkdir ${slices_dir}

foreach subj (001 002 004 005 006 008 010 012 013 014 015 017 018 021 022 023 024 025 026 027)
	set subj_dir=${proj_dir}"Subject${subj}/"
	set out_dir="${slices_dir}Subject${subj}/"
	mkdir ${out_dir}
	foreach run (0 1 2 3 4 5 6 7)
		set run_dir="${subj_dir}bold/func2standard/_subject_id_Subject${subj}/_warp_func${run}/"
		slices "${run_dir}run*.nii.gz" ${fsl_template} -o "${out_dir}/run${run}.gif"
	end
end


foreach subj (003 011 016 020)
	set subj_dir=${proj_dir}"Subject${subj}/"
	set out_dir="${slices_dir}Subject${subj}/"
	mkdir ${out_dir}
	foreach run (0 1 2 3 4 5 6)
		set run_dir="${subj_dir}bold/func2standard/_subject_id_Subject${subj}/_warp_func${run}/"
		slices "${run_dir}run*.nii.gz" ${fsl_template} -o "${out_dir}/run${run}.gif"
	end
end

foreach subj (019)
	set subj_dir=${proj_dir}"Subject${subj}/"
	set out_dir="${slices_dir}Subject${subj}/"
	mkdir ${out_dir}
	foreach run (0 1 2 3 4 5)
		set run_dir="${subj_dir}bold/func2standard/_subject_id_Subject${subj}/_warp_func${run}/"
		slices "${run_dir}run*.nii.gz" ${fsl_template} -o "${out_dir}/run${run}.gif"
	end
end
