#!/bin/csh

set proj_dir="/mnt/net/LaCie/Analysis/RuleSwitch/"

# Time series extraction

python PPI_ts.py Subject001 &
python PPI_ts.py Subject002 &
python PPI_ts.py Subject003 &
python PPI_ts.py Subject004 &
python PPI_ts.py Subject005 &
python PPI_ts.py Subject006 &
python PPI_ts.py Subject008 &
python PPI_ts.py Subject010 &
python PPI_ts.py Subject011 &
python PPI_ts.py Subject012 &
python PPI_ts.py Subject013 &
python PPI_ts.py Subject014
python PPI_ts.py Subject015 &
python PPI_ts.py Subject016 &
python PPI_ts.py Subject017 &
python PPI_ts.py Subject018 &
python PPI_ts.py Subject019 &
python PPI_ts.py Subject020 &
python PPI_ts.py Subject021 &
python PPI_ts.py Subject022 &
python PPI_ts.py Subject023 &
python PPI_ts.py Subject024 &
python PPI_ts.py Subject025 &
python PPI_ts.py Subject026 &
python PPI_ts.py Subject027
wait

# Copy behave files
./behave_copy.sh
wait

RUN FSL
cd ${proj_dir}template/univar1a_PPI_LearnApply/
./feat_runner.sh
wait
cd /mnt/net/LaCie/Dmitrii/repos/rules/univariate/univar1a_PPI_LeanApply/

# Level 2

python levels12.py Subject001 &
python levels12.py Subject002 &
python levels12.py Subject003 &
python levels12.py Subject004 &
python levels12.py Subject005 &
python levels12.py Subject006 &
python levels12.py Subject008 &
python levels12.py Subject010 &
python levels12.py Subject011
python levels12.py Subject012 &
python levels12.py Subject013 &
python levels12.py Subject014 &
python levels12.py Subject015 &
python levels12.py Subject016 &
python levels12.py Subject017 &
python levels12.py Subject018 &
python levels12.py Subject019 &
python levels12.py Subject020
python levels12.py Subject021 &
python levels12.py Subject022 &
python levels12.py Subject023 &
python levels12.py Subject024 &
python levels12.py Subject025 &
python levels12.py Subject026 &
python levels12.py Subject027
wait


# Level 3

python level3.py 7 1 &
python level3.py 7 2 &
python level3.py 7 3 &
python level3.py 8 1 &
python level3.py 8 2 &
python level3.py 8 3 &
python level3.py 9 1 &
python level3.py 9 2 &
python level3.py 9 3 &
wait

#Randomize
mkdir ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_7_1 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_7_2 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_7_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_7_3 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_8_1 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_8_2 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_8_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_8_3 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_1/copes_merged/cope1_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_1/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_1/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_9_1 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_2/copes_merged/cope2_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_2/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_2/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_9_2 -v 8 -C 2.49 &
randomise -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_3/copes_merged/cope3_merged.nii.gz -m ${proj_dir}masks/caudate.nii.gz -d ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_3/design_mat/design.mat -t ${proj_dir}level3s/model_univar1a_PPI_LearnApply/copes_9_3/design_con/design.con -o ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_9_3 -v 8 -C 2.49
wait

# #Cluster info (coordinates are in mm)
mkdir ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/
foreach l1cope (7 8 9)
  foreach l2cope (1 2 3)
    foreach l3cope (1 2)
      fslmaths ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/rand_caud_${l1cope}_${l2cope}_${l3cope}
      cluster -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/rand_caud_${l1cope}_${l2cope}_${l3cope} -t 0.001 --mm --num=4 --peakdist=10 --olmax=${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/lmax_${l1cope}_${l2cope}_${l3cope}.txt --osize=${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/clsize_${l1cope}_${l2cope}_${l3cope} > ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
    end
  end
end

# #Cluster info (coordinates are in vox)
mkdir ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster_vox/
foreach l1cope (7 8 9)
  foreach l2cope (1 2 3)
    foreach l3cope (1 2)
      fslmaths ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_${l1cope}_${l2cope}_clusterm_corrp_tstat${l3cope}.nii.gz -thr 0.95 -bin -mul ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/rand_caud_${l1cope}_${l2cope}_tstat${l3cope}.nii.gz ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster_vox/rand_caud_${l1cope}_${l2cope}_${l3cope}
      cluster -i ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster_vox/rand_caud_${l1cope}_${l2cope}_${l3cope} -t 0.001 --num=4 --peakdist=10 --olmax=${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster_vox/lmax_${l1cope}_${l2cope}_${l3cope}.txt > ${proj_dir}level3s/model_univar1a_PPI_LearnApply/randomized/cluster_vox/clinfo_${l1cope}_${l2cope}_${l3cope}.txt
    end
  end
end
