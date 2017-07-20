#! /usr/bin/env python 

import numpy as np
import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

from mpi4py import MPI

rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

output_num = 1
problem_name = 'athena_implode'

f = h5py.File('Implode.out1.%05i.athdf' %output_num,flag='r')

t = (output_num)*0.01

x = np.array(f['x1f'][:,:-1])
y = np.array(f['x2f'][:,:-1])

x_sort = np.argsort(x[:,0])
y_sort = np.argsort(y[:,0])

mesh_nx = int(np.sqrt(x.shape[0]))
mesh_ny = int(np.sqrt(y.shape[0]))
mesh_dx = 64
mesh_dy = 64

x = x[x_sort[::mesh_nx]].flatten()
y = y[y_sort[::mesh_ny]].flatten()

x_inv_sort = np.zeros(mesh_nx*mesh_ny)
y_inv_sort = np.zeros(mesh_nx*mesh_ny)
for i in range(mesh_nx*mesh_ny):
  x_inv_sort[x_sort[i]] = i
  y_inv_sort[y_sort[i]] = i

rho = np.array(f['prim'][0,:,0,:,:])
rho_shape = np.array(rho[0].shape)
rho_shape[0] *= mesh_nx
rho_shape[1] *= mesh_ny
rho_total = np.zeros(rho_shape)

for i in range(mesh_nx*mesh_ny):
  rho_total[mesh_dy*(y_inv_sort[i]//mesh_ny):mesh_dy*(y_inv_sort[i]//mesh_ny+1),
            mesh_dx*(x_inv_sort[i]//mesh_nx):mesh_dx*(x_inv_sort[i]//mesh_nx+1)] = rho[i]

xm, ym = np.meshgrid(x,y)

fig = plt.figure()
title = fig.suptitle("{:s} Implode at t={:g}; nx={:d}".format(problem_name, t, len(x)))
ax1 = fig.add_subplot(1,1,1)
p1 = ax1.pcolormesh(xm, ym, rho_total)
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
  f = h5py.File('Implode.out1.%05i.athdf' %j,flag='r')
  t = j*0.01
  rho = np.array(f['prim'][0,:,0,:,:])

  for i in range(mesh_nx*mesh_ny):
    rho_total[mesh_dy*(y_inv_sort[i]//mesh_ny):mesh_dy*(y_inv_sort[i]//mesh_ny+1),
              mesh_dx*(x_inv_sort[i]//mesh_nx):mesh_dx*(x_inv_sort[i]//mesh_nx+1)] = rho[i]

  p1.set_array(np.ravel(rho_total[:-1,:-1]))
#  p1.set_clim([np.min(rho_total),np.max(rho_total)])
#  cbar.set_clim([np.min(rho_total),np.max(rho_total)])
  title.set_text("{:s} Implode at t={:g}; nx={:d}".format(problem_name, t, len(x)))

  fig.savefig('frames/{0:s}_{1:04d}.png'.format(problem_name,j), dpi=300)

