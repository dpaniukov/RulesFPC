#!/bin/csh

#This file rearranges behavioral files to openfmri standard for level 1 mvpa analysis

set project_dir = "/Volumes/LaCie/Analysis/RuleSwitch/"
set model_name = 'univar1a_LearnApply'
set task = "001"
set repo_dir = "/Volumes/LaCie/Dmitrii/repos/rules/"

foreach subj (001 002 004 005 006 008 010 012 013 014 015 017 018 021 022 023 024 025 026 027)
	set subj_dir = "${project_dir}Subject${subj}/"
	mkdir ${subj_dir}model/model_${model_name}
	mkdir ${subj_dir}model/model_${model_name}/onsets

	foreach run (1 2 3 4 5 6 7 8)
	set out_dir = "${subj_dir}model/model_${model_name}/onsets/task${task}_run${run}/"
	mkdir ${out_dir}

	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev1_run${run}.txt ${out_dir}ev001.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev2_run${run}.txt ${out_dir}ev002.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev3_run${run}.txt ${out_dir}ev003.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev4_run${run}.txt ${out_dir}ev004.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev5_run${run}.txt ${out_dir}ev005.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev6_run${run}.txt ${out_dir}ev006.txt

	end
end

foreach subj (003 011 016 020)
	set subj_dir = "${project_dir}Subject${subj}/"
	mkdir ${subj_dir}model/model_${model_name}
	mkdir ${subj_dir}model/model_${model_name}/onsets

	foreach run (2 3 4 5 6 7 8)
	set out_dir = "${subj_dir}model/model_${model_name}/onsets/task${task}_run${run}/"
	mkdir ${out_dir}

	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev1_run${run}.txt ${out_dir}ev001.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev2_run${run}.txt ${out_dir}ev002.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev3_run${run}.txt ${out_dir}ev003.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev4_run${run}.txt ${out_dir}ev004.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev5_run${run}.txt ${out_dir}ev005.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev6_run${run}.txt ${out_dir}ev006.txt
	end
end

foreach subj (019)
	set subj_dir = "${project_dir}Subject${subj}/"
	mkdir ${subj_dir}model/model_${model_name}
	mkdir ${subj_dir}model/model_${model_name}/onsets

	foreach run (1 2 3 4 5 6)
	set out_dir = "${subj_dir}model/model_${model_name}/onsets/task${task}_run${run}/"
	mkdir ${out_dir}

	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev1_run${run}.txt ${out_dir}ev001.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev2_run${run}.txt ${out_dir}ev002.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev3_run${run}.txt ${out_dir}ev003.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev4_run${run}.txt ${out_dir}ev004.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev5_run${run}.txt ${out_dir}ev005.txt
	cp ${repo_dir}univariate/${model_name}/behave/source_files/Subject${subj}_${model_name}_ev6_run${run}.txt ${out_dir}ev006.txt
	end
end
