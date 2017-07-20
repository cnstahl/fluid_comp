import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import struct

class vtk_output:

  def __init__(self,dim,x0,dx,time):
    self.dim = dim
    self.x0 = x0
    self.dx = dx
    self.time = time
    self.xstart = x0
    self.xend = np.array(x0) + np.array(dx)*np.array(dim)

  def get_coordinates(self):
    x = self.xstart[2] + self.dx[2]*np.linspace(0.5,self.dim[2]-0.5,self.dim[2])
    y = self.xstart[1] + self.dx[1]*np.linspace(0.5,self.dim[1]-0.5,self.dim[1])
    return (x,y)


def readline(file):
  line = ''
  char = file.read(1)
  while char!=b'\n':
    line = line+char.decode(encoding='UTF-8')
    char = file.read(1)
  return line

def readvtk(filename):
  f = open(filename,'rb')

# # vtk DataFile Version 3.0
# CONSERVED vars at time= 2.500003e+02, level= 0, domain= 0
# BINARY
# DATASET STRUCTURED_POINTS
# DIMENSIONS 257 4097 257
# ORIGIN -5.000000e-01 -8.000000e+00 -5.000000e-01
# SPACING 3.906250e-03 3.906250e-03 3.906250e-03
# CELL_DATA 268435456
# SCALARS density float
# LOOKUP_TABLE default

  line = readline(f)
  line = readline(f)
  time = float(line.split(' ')[4][:-1])
  line = readline(f)
  line = readline(f)
  line = readline(f)
  xdim = int(line.split(' ')[1])-1
  ydim = int(line.split(' ')[2])-1
  zdim = int(line.split(' ')[3])-1
  line = readline(f)
  x0 = float(line.split(' ')[1])
  y0 = float(line.split(' ')[2])
  z0 = float(line.split(' ')[3])
  line = readline(f)
  dx = float(line.split(' ')[1])
  dy = float(line.split(' ')[2])
  dz = float(line.split(' ')[3])
  line = readline(f)
  line = readline(f)
  line = readline(f)

  dim = [zdim,ydim,xdim]
  d = [dz,dy,dx]
  org = [z0,y0,x0]
  vtk_file = vtk_output(dim,org,d,time)

  u = np.zeros([zdim,ydim,xdim])
  w = np.zeros([zdim,ydim,xdim])
  rho = np.zeros([zdim,ydim,xdim])
  p = np.zeros([zdim,ydim,xdim])

  for k in range(zdim):
    for j in range(ydim):
      num = f.read(4*xdim)
      rho[k,j,:] = struct.unpack('!%df' % xdim,num)

  line = readline(f)

  for k in range(zdim):
    for j in range(ydim):

      num = f.read(4*xdim*3)
      velarray = struct.unpack('!%df' % (xdim*3),num)
      u[k,j,:] = velarray[0::3]
      w[k,j,:] = velarray[1::3]

  line = readline(f)
  line = readline(f)

  for k in range(zdim):
    for j in range(ydim):
      num = f.read(4*xdim)
      p[k,j,:] = struct.unpack('!%df' % xdim,num)

  f.close()

  return (u,w,rho,p,vtk_file)


