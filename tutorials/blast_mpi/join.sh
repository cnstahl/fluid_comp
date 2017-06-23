for i in `seq 10 11`;
do
#    echo $i
    ./join_vtk++ -o Blast.000$i.vtk Blast.block0.out1.000$i.vtk Blast.block1.out1.000$i.vtk Blast.block2.out1.000$i.vtk Blast.block3.out1.000$i.vtk \
	Blast.block4.out1.000$i.vtk Blast.block5.out1.000$i.vtk Blast.block6.out1.000$i.vtk Blast.block7.out1.000$i.vtk 
done 