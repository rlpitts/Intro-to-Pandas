#!/bin/bash
#SBATCH -A lu-test              # project number (FIXME)
#SBATCH -t 00:05:00             # Asking for 5 min. max 
#SBATCH -J numba_demo           # name of job
#SBATCH -o numba_demo_%j.out    # output file
#SBATCH -e numba_demo_%j.err    # error messages
#SBATCH --cpus-per-task=6       # cores per task = n_threads (adjust as desired)

cat $0

echo "Running with $SLURM_CPUS_PER_TASK threads."
# Delete this next line if you're on PDC
ml purge  > /dev/null 2>&1
# Adjust according to your computing resource
ml foss/2023b Python/3.11.5 SciPy-bundle/2023.11 numba/0.60.0

python3 numba_demo.py
