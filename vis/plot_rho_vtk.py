
import numpy as np
import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from readvtk import *

from mpi4py import MPI

rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

output_num = 1
problem_name = 'athena_implode'

(u,w,rho,p,vtk) = readvtk('Implode.%04i.vtk' %output_num)

t = (output_num)*0.01

(x,y) = vtk.get_coordinates()

xm, ym = np.meshgrid(x,y)

fig = plt.figure()
title = fig.suptitle("{:s} Implode at t={:g}; nx={:d}".format(problem_name, t, len(x)))
ax1 = fig.add_subplot(1,1,1)
p1 = ax1.pcolormesh(xm, ym, rho[0])
cbar = fig.colorbar(p1)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$z$')
ax1.set_xlim([0,0.3])
ax1.set_ylim([0,0.3])

p1.set_clim([0.4,1.1])
cbar.set_clim([0.4,1.1])

if rank == 0:
  if not os.path.isdir('frames'):
    os.mkdir('frames')

for j in range(rank,251,size):
  print(j)
  (u,w,rho,p,vtk) = readvtk('Implode.%04i.vtk' %j)
  t = j*0.01

  p1.set_array(np.ravel(rho[0,:-1,:-1]))
#  p1.set_clim([np.min(rho_total),np.max(rho_total)])
#  cbar.set_clim([np.min(rho_total),np.max(rho_total)])
  title.set_text("{:s} Implode at t={:g}; nx={:d}".format(problem_name, t, len(x)))

  fig.savefig('frames/{0:s}_{1:04d}.png'.format(problem_name,j), dpi=300)

