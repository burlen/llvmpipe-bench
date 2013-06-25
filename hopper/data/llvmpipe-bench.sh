#!/bin/bash

export PV_HOME=/usr/common/graphics/ParaView/builds
source $PV_HOME/module-gnu.sh

for mpinp in `seq 1 24`
do
  for lpnt in `seq 1 24`
  do
    echo "submitting $mpinp $lpnt"
    export lpnt
    export mpinp
    qsub -N llpb-$lpnt-$mpinp -V -q regular -l walltime=00:30:00 -l mppwidth=24 $PV_HOME/llvmpipe-bench.qsub
  done
done
