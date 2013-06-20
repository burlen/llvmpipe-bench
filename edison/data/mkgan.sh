#!/bin/bash

# for a single run with 16 rank
# strip out event times for each rank

for i in `seq 0 15`;
do
   echo "rank$i=[";
   grep "^$i " 272/SurfaceLIC.log  | cut -d' ' -f5;
   echo "]";
   echo;
done
