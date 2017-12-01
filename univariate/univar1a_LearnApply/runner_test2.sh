#!/bin/csh

set proj_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"

# Levels 1 and 2

# mkdir /mnt/net/LaCie/scratch/RuleSwitch/

# python levels12.py Subject001 &
# python levels12.py Subject002 &
# python levels12.py Subject003 &
# python levels12.py Subject004 &
# python levels12.py Subject005 &
# python levels12.py Subject006 &
# python levels12.py Subject008 &
# python levels12.py Subject010 &
# python levels12.py Subject011
# python levels12.py Subject012 &
# python levels12.py Subject013 &
# python levels12.py Subject014 &
# python levels12.py Subject015 &
# python levels12.py Subject016 &
# python levels12.py Subject017 &
# python levels12.py Subject018 &
# python levels12.py Subject019 &
# python levels12.py Subject020
# python levels12.py Subject021 &
# python levels12.py Subject022 &
# python levels12.py Subject023 &
# python levels12.py Subject024 &
# python levels12.py Subject025 &
# python levels12.py Subject026 &
# python levels12.py Subject027
#wait
#
# python levels12.py Subject001 &
# python levels12.py Subject002 &
# python levels12.py Subject003 &
# python levels12.py Subject004 &
# python levels12.py Subject005 &
# python levels12.py Subject006 &
# python levels12.py Subject008 &
# python levels12.py Subject010 &
# python levels12.py Subject011
# python levels12.py Subject012 &
# python levels12.py Subject013 &
# python levels12.py Subject014 &
# python levels12.py Subject015 &
# python levels12.py Subject016 &
# python levels12.py Subject017 &
# python levels12.py Subject018 &
# python levels12.py Subject019 &
# python levels12.py Subject020
# python levels12.py Subject021 &
# python levels12.py Subject022 &
# python levels12.py Subject023 &
# python levels12.py Subject024 &
# python levels12.py Subject025 &
# python levels12.py Subject026 &
# python levels12.py Subject027
#wait


# Level 3

# python level3.py 1 1 &
# python level3.py 1 2 &
# python level3.py 1 3 &
# python level3.py 2 1 &
# python level3.py 2 2 &
# python level3.py 2 3 &
# python level3.py 3 1 &
# python level3.py 3 2 &
# python level3.py 3 3
# python level3.py 4 1 &
# python level3.py 4 2 &
# python level3.py 4 3 &
# python level3.py 5 1 &
# python level3.py 5 2 &
# python level3.py 5 3 &
# python level3.py 6 1 &
# python level3.py 6 2 &
# python level3.py 6 3
# wait

# python level3.py 1 1 &
# python level3.py 1 2 &
# python level3.py 1 3 &
# python level3.py 2 1 &
# python level3.py 2 2 &
# python level3.py 2 3 &
# python level3.py 3 1 &
# python level3.py 3 2 &
# python level3.py 3 3
# python level3.py 4 1 &
# python level3.py 4 2 &
# python level3.py 4 3 &
# python level3.py 5 1 &
# python level3.py 5 2 &
# python level3.py 5 3 &
# python level3.py 6 1 &
# python level3.py 6 2 &
# python level3.py 6 3
# wait


#BROCCOLI randomise
set model_name = "model_univar1a_LearnApply"

#mkdir ${proj_dir}level3s/${model_name}/randomized
#foreach l1cope (1)
#foreach l2cope (3)

#    fslmaths ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -mul -1 ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg
#    RandomiseGroupLevel ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -mask ${proj_dir}masks/WB.nii.gz -groupmean -inferencemode 2 -cdt 2.49 -output ${proj_dir}level3s/${model_name}/randomized/results_${l1cope}_${l2cope}_1 -device 1 -permutations 10000 &
#    RandomiseGroupLevel ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg.nii.gz -mask ${proj_dir}masks/WB.nii.gz -groupmean -inferencemode 2 -cdt 2.49 -output ${proj_dir}level3s/${model_name}/randomized/results_${l1cope}_${l2cope}_2 -device 2 -permutations 10000
#end
#end
#wait

#Randomize
# mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_1_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_1_2 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_3/copes_merged/cope3_merged_neg.nii.gz -m ${proj_dir}masks/WB.nii.gz -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_1_3_25 -1 -v 8 -C 2.5
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_2_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_2_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_2_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_3_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_3_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_3_3 -v 8 -C 2.49
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_4_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_4_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_4_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_4_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_5_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_5_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_5_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_5_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_6_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_6_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_6_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_6_3 -v 8 -C 2.49
# wait
#
# FPC mask
# mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_1_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_1_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_1_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_2_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_2_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_2_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_3_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_3_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_3_3 -v 8 -C 2.49


## #Cluster info
#mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/
#foreach l1cope (1 2 3)
#  foreach l2cope (1 2 3)
#    foreach l3cope (1 2)
#      fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/rand_${l1cope}_${l2cope}_${l3cope}
#      cluster -i ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/rand_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --mm --olmax=${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/lmax_${l1cope}_${l2cope}_${l3cope}.txt --osize=${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/clsize_${l1cope}_${l2cope}_${l3cope} > ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
#    end
#  end
#end
#
## #Cluster info - in vox
#mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster_vox/
#foreach l1cope (1 2 3)
#  foreach l2cope (1 2 3)
#    foreach l3cope (1 2)
#      fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster_vox/rand_${l1cope}_${l2cope}_${l3cope}
#      cluster -i ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster_vox/rand_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --olmax=${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster_vox/lmax_${l1cope}_${l2cope}_${l3cope}.txt > ${proj_dir}level3s/model_univar1a_LearnApply/randomized/cluster_vox/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
#    end
#  end
#end
#
## Cluster info for FPC in mm
#mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/
#foreach l1cope (1 2 3)
#  foreach l2cope (1 2 3)
#    foreach l3cope (1 2)
#      fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/rand_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/rand_${l1cope}_${l2cope}_${l3cope}
#      cluster -i ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/rand_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --mm --olmax=${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/lmax_${l1cope}_${l2cope}_${l3cope}.txt --osize=${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/clsize_${l1cope}_${l2cope}_${l3cope} > ${proj_dir}level3s/model_univar1a_LearnApply/randomized_frontal_pole/cluster/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
#    end
#  end
#end


# Seger and Cincotta, 2006 replication
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/hippocampus.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_hipp_3_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/hippocampus.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_hipp_3_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/hippocampus.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_hipp_3_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/striatum.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_str_3_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/striatum.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_str_3_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/striatum.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_str_3_3 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_caud_3_1 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_caud_3_2 -v 8 -C 2.49 &
# randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized/rand_caud_3_3 -v 8 -C 2.49
