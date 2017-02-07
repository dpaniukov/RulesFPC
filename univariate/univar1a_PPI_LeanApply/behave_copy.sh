#!/bin/csh

set proj_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"

foreach subj (001 002 004 005 006 008 010 012 013 014 015 017 018 021 022 023 024 025 026 027)

  set to_dir="${proj_dir}Subject${subj}/behave/univar1a_PPI_LeanApply/"
  rm -rf ${to_dir}
  mkdir ${to_dir}

  foreach run (0 1 2 3 4 5 6 7)

    set from_dir="${proj_dir}level3s/model_univar1a_LearnApply/randomized/ts_means/_subject_id_Subject${subj}/_ts_means${run}/"
    cp ${from_dir}run*.txt ${to_dir}

  end
end

foreach subj (003 011 016 020)

    set to_dir="${proj_dir}Subject${subj}/behave/univar1a_PPI_LeanApply/"
    rm -rf ${to_dir}
    mkdir ${to_dir}

  foreach run (0 1 2 3 4 5 6)

    set from_dir="${proj_dir}level3s/model_univar1a_LearnApply/randomized/ts_means/_subject_id_Subject${subj}/_ts_means${run}/"
    cp ${from_dir}run*.txt ${to_dir}

  end
end

foreach subj (019)

    set to_dir="${proj_dir}Subject${subj}/behave/univar1a_PPI_LeanApply/"
    rm -rf ${to_dir}
    mkdir ${to_dir}

  foreach run (0 1 2 3 4 5)

    set from_dir="${proj_dir}level3s/model_univar1a_LearnApply/randomized/ts_means/_subject_id_Subject${subj}/_ts_means${run}/"
    cp ${from_dir}run*.txt ${to_dir}

  end
end
