#$ -V
#$ -cwd
#$ -S /bin/bash
#$ -N jname
#$ -M dmitrii.paniukov@ttu.edu
#$ -m e
#$ -o $JOB_NAME.o$JOB_ID
#$ -e $JOB_NAME.e$JOB_ID
#$ -q normal
#$ -pe fill 12
#$ -P hrothgar

