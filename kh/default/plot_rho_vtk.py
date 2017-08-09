
import numpy as np
#import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from athena_read import *

#from mpi4py import MPI

#rank = MPI.COMM_WORLD.rank
#size = MPI.COMM_WORLD.size
rank = 0
size = 1

output_num = 1
problem_name = 'athena_kh'

# (u,w,rho,p,vtk) = readvtk('kh.%04i.vtk' %output_num)
x,y,z_faces,data = vtk('kh.%04i.vtk' %output_num)  
#for key in data: print key
rho = data["dens"]

times = np.loadtxt('times')
t = times[output_num]

#(x,y) = vtk.get_coordinates()

xm, ym = np.meshgrid(x,y)

fig = plt.figure()
title = fig.suptitle("{:s} KH at t={:g}; nx={:d}".format(problem_name, t, len(x)))
ax1 = fig.add_subplot(1,1,1)
p1 = ax1.pcolormesh(xm, ym, rho[0])
cbar = fig.colorbar(p1)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$z$')
ax1.set_xlim([-0.5,0.5])
ax1.set_ylim([ 0.0,1.0])

p1.set_clim([0.9,1.1])
cbar.set_clim([0.9,1.1])

if rank == 0:
  if not os.path.isdir('frames'):
    os.mkdir('frames')

for j in range(rank,102,size):
  print(j)
  #(u,w,rho,p,vtk) = readvtk('kh.%04i.vtk' %j)
  x_faces,y_faces,z_faces,data = vtk('kh.%04i.vtk' %j)
  rho = data["dens"]
  t = times[j]

  p1.set_array(np.ravel(rho[0,:-1,:-1]))
  p1.set_clim([np.min(rho),np.max(rho)])
  cbar.set_clim([np.min(rho),np.max(rho)])
  title.set_text("{:s} Instability at t={:g}; nx={:d}".format(problem_name, t, len(x)))

  fig.savefig('frames/{0:s}_{1:04d}.png'.format(problem_name,j), dpi=300)

