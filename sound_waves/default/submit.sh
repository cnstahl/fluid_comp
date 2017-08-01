#!/bin/bash
#
#SBATCH --job-name=sound_wave
#SBATCH --output=res.txt

# parallel job using 128 processors. and runs for 4 hours (max)
#SBATCH -N 1   # node count
#SBATCH --ntasks-per-node=8
#SBATCH -t 1:00:00
# sends mail when process begins, and 
# when it ends. Make sure you define your email 
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user=cnstahl@princeton.edu

module load openmpi/gcc
module load anaconda3
mpiexec -n 8 athena -i athinput.linear_wave3d 
mpiexec -n 4 python join.py
module load anaconda
python extract.py