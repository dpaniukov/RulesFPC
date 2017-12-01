#!/bin/csh

#set proj_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"
set proj_dir="/home/dmitrii/results_rules/rt"

set model_name = 'model_univar1a_LearnApply_rt'

# Levels 1 and 2

# mkdir /mnt/net/LaCie/scratch/RuleSwitch/
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
# wait
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
# wait


# # Level 3

#foreach l1cope (1 2 3)
#foreach l2cope (1 2 3)
#    python level3.py ${l1cope} ${l2cope} &
#end
#end
#wait
#
#foreach l1cope (7 8 9)
#foreach l2cope (1 2 3)
#    python level3.py ${l1cope} ${l2cope} &
#end
#end
#wait
#
#foreach l1cope (1 2 3)
#foreach l2cope (1 2 3)
#    python level3.py ${l1cope} ${l2cope} &
#end
#end
#wait
#
#foreach l1cope (7 8 9)
#foreach l2cope (1 2 3)
#    python level3.py ${l1cope} ${l2cope} &
#end
#end
#wait
#
#
# #Randomize
# mkdir ${proj_dir}level3s/${model_name}/randomized
#foreach l1cope (1 2 3)
#foreach l2cope (1 2 3)
#   randomise -i ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_mat/design.mat -t ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_con/design.con -o ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope} -v 8 -C 2.49 &
#end
#end
#wait
#
#foreach l1cope (7 8 9)
#foreach l2cope (1 2 3)
#   randomise -i ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_mat/design.mat -t ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_con/design.con -o ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope} -v 8 -C 2.49 &
#end
#end
#wait
#
#
## # FPC mask
#mkdir ${proj_dir}level3s/${model_name}/randomized_frontal_pole
#foreach l1cope (1 2 3)
#foreach l2cope (1 2 3)
#   randomise -i ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_mat/design.mat -t ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_con/design.con -o ${proj_dir}level3s/${model_name}/randomized/rand_FPC_${l1cope}_${l2cope} -v 8 -C 2.49 &
#end
#end
#wait
#
#foreach l1cope (7 8 9)
#foreach l2cope (1 2 3)
#   randomise -i ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -m ${proj_dir}masks/frontal_pole.nii.gz -d ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_mat/design.mat -t ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/design_con/design.con -o ${proj_dir}level3s/${model_name}/randomized/rand_FPC_${l1cope}_${l2cope} -v 8 -C 2.49 &
#end
#end
#wait


 # # #Cluster info
 # mkdir ${proj_dir}level3s/${model_name}/randomized/cluster/
 # foreach l1cope (1 2 3)
 #   foreach l2cope (1 2 3)
 #     foreach l3cope (1 2)
 #       fslmaths ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/${model_name}/randomized/cluster/rand_${l1cope}_${l2cope}_${l3cope}
 #       cluster -i ${proj_dir}level3s/${model_name}/randomized/cluster/rand_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --mm --olmax=${proj_dir}level3s/${model_name}/randomized/cluster/lmax_${l1cope}_${l2cope}_${l3cope}.txt --osize=${proj_dir}level3s/${model_name}/randomized/cluster/clsize_${l1cope}_${l2cope}_${l3cope} > ${proj_dir}level3s/${model_name}/randomized/cluster/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
 #     end
 #   end
 # end
 #
 # # #Cluster info - in vox
 # mkdir ${proj_dir}level3s/${model_name}/randomized/cluster_vox/
 # foreach l1cope (1 2 3)
 #   foreach l2cope (1 2 3)
 #     foreach l3cope (1 2)
 #       fslmaths ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/${model_name}/randomized/rand_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/${model_name}/randomized/cluster_vox/rand_${l1cope}_${l2cope}_${l3cope}
 #       cluster -i ${proj_dir}level3s/${model_name}/randomized/cluster_vox/rand_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --olmax=${proj_dir}level3s/${model_name}/randomized/cluster_vox/lmax_${l1cope}_${l2cope}_${l3cope}.txt > ${proj_dir}level3s/${model_name}/randomized/cluster_vox/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
 #     end
 #   end
 # end
 #
 # Cluster info for FPC in mm
 mkdir ${proj_dir}/randomized_frontal_pole/cluster/
 foreach l1cope (1 2 3)
   foreach l2cope (1 2 3)
     foreach l3cope (1 2)
       fslmaths ${proj_dir}/randomized_frontal_pole/rand_FPC_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}/randomized_frontal_pole/rand_FPC_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}/randomized_frontal_pole/cluster/rand_${l1cope}_${l2cope}_${l3cope}
       cluster -i ${proj_dir}/randomized_frontal_pole/cluster/rand_FPC_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --mm --olmax=${proj_dir}/randomized_frontal_pole/cluster/lmax_${l1cope}_${l2cope}_${l3cope}.txt --osize=${proj_dir}/randomized_frontal_pole/cluster/clsize_${l1cope}_${l2cope}_${l3cope} > ${proj_dir}/randomized_frontal_pole/cluster/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
     end
   end
 end


### COVARIATE
# Level 3

# python level3_covar.py 1 0 &
# python level3_covar.py 2 0 &
# python level3_covar.py 3 0
# wait

#mkdir ${proj_dir}level3s/model_univar1a_LearnApply/randomized_covar
#randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_0/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_0/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_1_0/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_covar/rand_1_0 -v 8 -C 2.49 &
#randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_0/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_0/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_2_0/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_covar/rand_2_0 -v 8 -C 2.49 &
#randomise -i ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_0/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/WB.nii.gz -d ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_0/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_LearnApply/copes_3_0/design_con/design.con -o ${proj_dir}level3s/model_univar1a_LearnApply/randomized_covar/rand_3_0 -v 8 -C 2.49 &


## 8 mm sphere around classification > baseline peak on rule application
#set MNI_template = "/Users/dmitrii/Lab_script/fsl/data/standard/MNI152lin_T1_2mm_brain_mask.nii.gz"
#fslmaths ${MNI_template} -mul 0 -add 1 -roi 65 1 90 1 38 1 0 1 ${proj_dir}level3s/model_univar1a_LearnApply/randomized/roi
#fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/randomized/roi -kernel sphere 8 -fmean -bin ${proj_dir}level3s/model_univar1a_LearnApply/randomized/sphere
#fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/randomized/sphere -mul ${MNI_template} ${proj_dir}level3s/model_univar1a_LearnApply/randomized/sphere_fin
#
#set pe_means = "${proj_dir}level3s/model_univar1a_LearnApply/randomized/PE_means.txt"
#echo "--- PE means for each contrast ---"  > ${pe_means}
#
# foreach l1cope (1 2 3)
#   foreach l2cope (1 2 3)
#
#        echo "l1cope ${l1cope}, l2cope ${l2cope}: " >> ${pe_means}
#
#        fslmaths ${proj_dir}level3s/model_univar1a_LearnApply/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -mul -1 ${proj_dir}level3s/model_univar1a_LearnApply/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg.nii.gz
#        fslstats ${proj_dir}level3s/model_univar1a_LearnApply/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -k ${proj_dir}level3s/model_univar1a_LearnApply/randomized/sphere_fin -M >> ${pe_means}
#        fslstats ${proj_dir}level3s/model_univar1a_LearnApply/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg.nii.gz -k ${proj_dir}level3s/model_univar1a_LearnApply/randomized/sphere_fin -M >> ${pe_means}
#
#        echo " " >> ${pe_means}
#
#   end
# end

#foreach l1cope (1 2 3 7 8 9)
#foreach l2cope (1 2 3)
#
#    fslmaths ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -mul -1 ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg
#    RandomiseGroupLevel ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged.nii.gz -mask ${proj_dir}masks/WB.nii.gz -groupmean -inferencemode 2 -cdt 2.49 -output ${proj_dir}level3s/${model_name}/randomized/results_${l1cope}_${l2cope}_1 -device 1 -permutations 10000 &
#    RandomiseGroupLevel ${proj_dir}level3s/${model_name}/copes_${l1cope}_${l2cope}/copes_merged/cope${l2cope}_merged_neg.nii.gz -mask ${proj_dir}masks/WB.nii.gz -groupmean -inferencemode 2 -cdt 2.49 -output ${proj_dir}level3s/${model_name}/randomized/results_${l1cope}_${l2cope}_2 -device 2 -permutations 10000
#end
#end
#wait
