#!/bin/bash
#
#SBATCH --job-name=kh
#SBATCH --output=res.txt

# parallel job using 128 processors. and runs for 4 hours (max)
#SBATCH -N 2   # node count
#SBATCH --ntasks-per-node=28
#SBATCH -t 4:00:00
# sends mail when process begins, and 
# when it ends. Make sure you define your email 
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user=cnstahl@princeton.edu

module purge 
module load openmpi/gcc

mpiexec -n 32 athena -i athinput.kh > athoutput.txt
python join.py > joinoutput.txt
python extract_times.py

module load anaconda
python plot_rho_vtk.py
