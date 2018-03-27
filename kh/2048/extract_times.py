import glob
import numpy as np
import athena_read

#print "make sure to use python2"

names  = glob.glob('*.vtk')
nfiles = len(names)

name   = str(names[0])
pos_dot = name.index('.')
name   = name[:pos_dot]

data   = athena_read.hst("%s.hst" %(name))
times  = data['time']
np.savetxt('times', times)
