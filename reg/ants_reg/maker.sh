#!/bin/csh

#job maker

foreach subj (001 002 003 004 005 006 008 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027)
  set myfile=job_${subj}.sh
  cat job_template.sh > ${myfile}
  sed -i s/jname/"ru_${subj}_reg"/g ${myfile}
  echo "python ../ants_reg.py Subject${subj}" >> ${myfile}
  echo "qsub ${myfile}" >> qsub_SL
end

chmod +x qsub_SL
