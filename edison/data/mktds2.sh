#!/bin/bash

#strip out the event times for all runs where
# num mpi is 1

for f in `grep LP_NUM_THREADS=16 ./ -rIl`
do
  echo rid`grep MPI_RANKS= $f | cut -d, -f1 | cut -d= -f2`"=["
  grep "^0 " $f | cut -d' ' -f5
   echo "]"
   echo
done
