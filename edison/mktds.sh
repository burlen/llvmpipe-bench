#!/bin/bash

#strip out the event times for all runs where
# num mpi is 1

for f in `grep MPI_RANKS=1, ./ -rIl`
do
  echo tid`grep MPI_RANKS= $f | cut -d, -f2 | cut -d= -f2`"=["
  grep "^0 " $f | cut -d' ' -f5
   echo "]"
   echo
done
