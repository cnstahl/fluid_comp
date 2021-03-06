
# Uses join_vtk to join together all vtk files

import glob
import os

num_files = len(list(glob.glob("*.block0.*.vtk")))
name = str(list(glob.glob("*.vtk"))[0])
pos_dot = name.index('.')
name = name[:pos_dot]

for i in range(num_files):
  command = "./join_vtk++ -o %s.%04i.vtk " %(name,i)
  command2 = "rm  " 
  for path in glob.glob("*.%05i.vtk" %i):
    command += "%s " %(str(path))
    command2 += "%s " %(str(path))
  print(command)
  os.system(command)
  os.system(command2)
  print(command2)
