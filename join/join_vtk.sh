#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
for f in kh.block0.*.vtk; do 
    file=${f%.vtk}
    numb=${file#kh.block0.}
    if $DIR/join_vtk++ -o kh.${numb}.vtk kh.*.$numb.vtk; then
	rm kh.*.$numb.vtk
    else
	continue
    fi
done
