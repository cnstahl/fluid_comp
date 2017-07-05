#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=8
#SBATCH --time=1:00
#SBATCH --mem-per-cpu=100

module load openmpi/gcc
mpiexec -n 8 ./athena -i athinput.kh
