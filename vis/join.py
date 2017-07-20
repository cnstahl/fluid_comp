
# Uses join_vtk to join together all vtk files

import pathlib
import os
from mpi4py import MPI

rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

p = pathlib.Path('.')

num_files = len(list(p.glob("id0/*.vtk")))
name = str(list(p.glob("id0/*.vtk"))[0])
pos_dot = name.index('.')
name = name[4:pos_dot]

for i in range(rank,num_files,size):
  command = "./join_vtk -o %s.%04i.vtk " %(name,i)
  for path in p.glob("*/*.%04i.vtk" %i):
    command += "%s " %(str(path))
  os.system(command)
