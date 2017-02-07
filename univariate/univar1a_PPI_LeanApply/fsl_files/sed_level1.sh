#!/bin/csh

#this will need to be set for each analysis
set analysis_name = 'univar1a_PPI_LearnApply'

#this needs to be set for each study
set analysis_dir = /Volumes/LaCie/Analysis/RuleSwitch/template/${analysis_name}/

#this will need to be changed only if you didn't use the template_[subject]_run[run]_[analysis_name] format that is recommended.
set template_file = $analysis_dir'template_001_run1_'$analysis_name'.fsf'

#this sets up a list of FEAT commands to run based on the template; it
#removes it if it already exists; creates it; changes permissions to be executable

set CTRLNAME = "$analysis_dir"ctrl_"$analysis_name"
rm -f $CTRLNAME
touch $CTRLNAME
chmod +x $CTRLNAME

foreach subj (001 002 003 004 005 006 008 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027)
	     foreach run (1 2 3 4 5 6 7 8)
	     	     	sed -e 's/Subject001/Subject'$subj'/' -e 's/Subject001_/Subject'$subj'_/' -e 's/run1/run'$run'/' -e 's/run1_/run'$run'_/' < "$template_file"  > $analysis_dir"$analysis_name"_"$subj"_"$run".fsf
			#The next line appends a command to the list
	     		#of feat commands to run
			echo feat "$analysis_name"_"$subj"_"$run".fsf >> $CTRLNAME
		end
	end

