#! /usr/bin/env python
# Uses join_vtk to join together all vtk files

import numpy as np
import matplotlib.pyplot as plt
import pathlib
import os
from mpi4py import MPI

rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

p = pathlib.Path('.')

num_files = len(list(p.glob("th_diff.block0.out1.*.tab")))

for i in range(rank,num_files,size):
  fname = "th_diff.block0.out1.{:05d}.tab".format(i)
  data = np.loadtxt(fname).T
  plt.plot(data[1], data[3])
  plt.savefig("vid.{:05d}.png".format(i))
  plt.clf()
  print("finished" + str(i))
