#!/bin/csh

set STUDY_NAME = $1
set SNUM = $2
set RAW_DIR = $3
set NUM_FUNC = $4
set NPTS = $5

mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"
mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"
mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/bold
mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/anatomy
mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/model
mkdir /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/behave

#DCM2NII
echo "Converting Functionals"
echo
echo
echo

set runs = `jot -s ' ' - 1 "$NUM_FUNC"`
echo "$runs"
foreach run ($runs)

	set func = `ls -d /mnt/net/LaCie/"$STUDY_NAME"/"$RAW_DIR"/HEAD_ROUTINE*/EP2D_BOLD_MOCO_*_"$run"_00*`
	echo "$func"
	rm -f "$func"/*.nii.gz
	set func = `ls -d /mnt/net/LaCie/"$STUDY_NAME"/"$RAW_DIR"/HEAD_ROUTINE*/EP2D_BOLD_MOCO_*_"$run"_00*`
	set ima_list = `ls "$func"`
	echo $ima_list[1]
 	mkdir  /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/bold/run"$run"

	dcm2nii -4 y -d n -i n "$func"/$ima_list[1]

	mv "$func"/*.nii.gz /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/bold/run"$run"/run"$run".nii.gz
	set wdir = /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/bold/run"$run"/
	#trim
	set nii_info = `fslinfo ${wdir}run"$run".nii.gz`
	echo "$nii_info"
	set timepts = $nii_info[10]
	@ timepts = $timepts - $NPTS
	echo "$timepts"

	fslroi ${wdir}run"$run".nii.gz ${wdir}run"$run"_trim.nii.gz $NPTS "$timepts"

	#mcflirt
	mcflirt -in ${wdir}run"$run"_trim -out ${wdir}run"$run"_mcf -plots -sinc_final

	#bet
	bet ${wdir}run"$run"_mcf ${wdir}run"$run"_mcf_brain -F -m

	fsl_motion_outliers -i ${wdir}run"$run"_trim.nii.gz -o ${wdir}scrubvols.txt --fd --thresh=.9 -s ${wdir}fd_out.txt

	set curscript_dir=`pwd`
	cd /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/bold/run"$run"/

	Rscript ${curscript_dir}/QAplotter.R fd_out.txt run"$run"_mcf.par scrubvols.txt

	cd ${curscript_dir}

end

Anat
echo
echo
echo "starting anatomical"
set anatdir = `ls -d ~/Desktop/"$STUDY_NAME"/"$RAW_DIR"/HEAD_ROUTINE*/T1_MPRAGE*`
rm -f "$anatdir"/*.nii.gz
dcm2nii -4 y -d n -i n -o "$anatdir"/*

mv "$anatdir"/o*.nii.gz /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/anatomy/Highres001.nii.gz

./antsBrainExtraction.sh -d 3 -a /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/anatomy/Highres001.nii.gz -e /mnt/net/LaCie/Analysis/OASIS/T_template0.nii.gz -m /mnt/net/LaCie/Analysis/OASIS/T_template0_BrainCerebellumProbabilityMask.nii.gz -o /mnt/net/LaCie/Analysis/"$STUDY_NAME"/Subject"$SNUM"/anatomy/highres001_ -f /mnt/net/LaCie/Analysis/OASIS/T_template0_BrainCerebellumRegistrationMask.nii.gz

echo "Done with $STUDY_NAME $SNUM" >> out.log
