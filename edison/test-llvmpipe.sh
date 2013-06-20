#!/bin/bash

for i in `seq 1 32`
do
  export LP_NUM_THREADS=$i;
  echo LP_NUM_THREADS=$LP_NUM_THREADS
  aprun -n 1 -j 2 -d 32 ctest -I 1002,1002,1
  echo
  echo
done
