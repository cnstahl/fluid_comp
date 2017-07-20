#!/bin/bash
#
#SBATCH --job-name=inviscid
#SBATCH --output=res.txt

# parallel job using 128 processors. and runs for 4 hours (max)
#SBATCH -N 5   # node count
#SBATCH --ntasks-per-node=28
#SBATCH -t 1:00:00
# sends mail when process begins, and 
# when it ends. Make sure you define your email 
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user=cnstahl@princeton.edu

module load openmpi/gcc
module load hdf5/gcc/openmpi-1.10.2/1.8.16
mpiexec -n 128 athena -i athinput.kh
