import glob
import numpy as np
from numpy import unravel_index
import athena_read

print "make sure to use python2"

def mag(data, type_):
    if type_ == 'vel':
        return np.linalg.norm(data)
    if type_ == 'press' or type_ == 'rho':
        return data
    else: raise ValueError

names  = glob.glob('*.vtk')
nfiles = len(names)

name   = str(names[0])
pos_dot = name.index('.')
name   = name[:pos_dot]

data   = athena_read.hst("%s.hst" %(name))
times  = data['time']
np.savetxt('times', times)

filename = "%s.%04i.vtk" %(name, 0)
maxes    = {}
x_faces,y_faces,z_faces,data     = athena_read.vtk(filename)
for key in data:
    maxes[key] = np.zeros(nfiles)

for n in range(nfiles):
    print("-------", n, "------")
    filename = "%s.%04i.vtk" %(name, n)
    x_faces,y_faces,z_faces,data = athena_read.vtk(filename)

    for key in data:
        array = data[key]
        maxes[key][n] = array[unravel_index(array.argmax(), array.shape)]


    # press = data['Etot']
    # vel   = data['mom']
    # rho   = data['dens']
    # max_press = 0
    # max_vel   = 0
    # max_rho   = 0
    
    # for i in range(len(z_faces)-1):
    #     for j in range(len(y_faces)-1):
    #         for k in range(len(x_faces)-1):
    #             max_press = max(max_press, mag(press[i,j,k], 'press'))
    #             max_vel   = max(max_vel  , mag(vel[i,j,k],   'vel'))
    #             max_rho   = max(max_rho  , mag(rho[i,j,k],   'rho'))
    # presss[n] = max_press
    # vels[n]   = max_vel
    # rhos[n]   = max_rho

for key in maxes:
    np.savetxt(key, maxes[key])


# np.savetxt('presss', presss)
# np.savetxt('vels', vels)
# np.savetxt('rhos', rhos)
