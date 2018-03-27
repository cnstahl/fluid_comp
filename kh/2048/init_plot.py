
import numpy as np
#import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from athena_read import *

problem_name = 'athena_kh'
t = 0
output_num = 0

x,y,z_faces,data = vtk('kh.%04i.vtk' %output_num)  

rho = data["dens"]

xm, ym = np.meshgrid(x,y)

fig = plt.figure()
title = fig.suptitle("{:s} KH at t={:g}; nx={:d}".format(problem_name, t, len(x)))
ax1 = fig.add_subplot(1,1,1)
p1 = ax1.pcolormesh(xm, ym, rho[0])
cbar = fig.colorbar(p1)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$z$')
ax1.set_xlim([ 0.0,1.0])
ax1.set_ylim([ 0.0,1.0])

p1.set_clim([0.9,1.1])
cbar.set_clim([0.9,1.1])

if not os.path.isdir('frames'):
  os.mkdir('frames')
j = 0
#(u,w,rho,p,vtk) = readvtk('kh.%04i.vtk' %j)
x_faces,y_faces,z_faces,data = vtk('kh.%04i.vtk' %j)
#print(data)
mom = data["mom"]

dat = rho
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; rho".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}rho.png'.format(problem_name,j), dpi=300)

dat = mom[:, :, :, 0]
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; mom1".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}mom1.png'.format(problem_name,j), dpi=300)

dat = mom[:, :, :, 1]
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; mom2".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}mom2.png'.format(problem_name,j), dpi=300)

dat = mom[:, :, :, 0]/rho
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; vel1".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}vel1.png'.format(problem_name,j), dpi=300)

dat = mom[:, :, :, 1]/rho
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; vel2".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}vel2.png'.format(problem_name,j), dpi=300)

dat = data["Etot"]
p1.set_cmap('RdBu')
p1.set_array(np.ravel(dat[0]))
p1.set_clim([np.min(dat),np.max(dat)])
cbar.set_clim([np.min(dat),np.max(dat)])
title.set_text("{:s} Instability at t={:g}; nx={:d}; ener".format(problem_name, t, len(x)))

fig.savefig('frames/{0:s}_{1:04d}ener.png'.format(problem_name,j), dpi=300)

