#!/bin/bash

for i in `seq 1 48`
do
  export LP_NUM_THREADS=$i;
  echo LP_NUM_THREADS=$LP_NUM_THREADS
  aprun -n 1 -d 24 ctest -I 1002,1002,1
  echo
  echo
done
