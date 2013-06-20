#!/bin/bash

# get the total run time
# for each run
# generate code to load a 2d array
# with threads on y axis and mpi ranks on the x axis

for d in `ls --color=never -d *`;
do
  ids=`grep -m1 MPI_ $d/SurfaceLIC.log`;
  x=`echo $ids | cut -d, -f1 | cut -d= -f2`;
  y=`echo $ids | cut -d, -f2 | cut -d= -f2`;
  z=`grep -m1 "RenderGeometry" $d/SurfaceLIC.log | cut -d' ' -f5`;
  #if [ -z "$z" ]; then z=-1.0; fi
  echo "renGeomT[$y][$x]=$z";
  #if [ -z "$z" ]; then ../tmp.sh $x $y; fi
done



