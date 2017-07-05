#! /bin/bash

for f in kh.block0.*.vtk; do 
    file=${f%.vtk}
    numb=${file#kh.block0.}
    ~/Documents/Junior/Summer_Astro/fluid_comp/join/join_vtk++ -o kh.${numb}.vtk kh.*.$numb.vtk
    rm kh.*.$numb.vtk
done