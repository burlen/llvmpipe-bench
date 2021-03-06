#!/bin/bash

export PV_HOME=/usr/common/graphics/ParaView/builds
source $PV_HOME/modules-gnu.sh

QUEUE=regular
#QUEUE=debug

for PV_NCPUS in `seq 16 8 512`
#for PV_NCPUS in `seq 64 8 64`
do
  echo "submitting for $PV_NCPUS cores"

  export PV_NCPUS
  export PV_NCPUS_PER_NODE=8
  export PV_NCPUS_PER_SOCKET=4
  export PV_WKD=`pwd`/

#  export PV_SCRIPT=`pwd`/pr1-lic.py
#  export PV_PORT=33110
#  export PV_TIME=0.0
#  export PV_COMPOSITE_STRATEGY='INPLACE'
#  export PV_LOGFILE=pr1-lic-b-ip.log
#  qsub -N pss-pr1-ip-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub
#
#  export PV_SCRIPT=`pwd`/pr1-lic.py
#  export PV_PORT=33112
#  export PV_TIME=0.0
#  export PV_COMPOSITE_STRATEGY='INPLACE DISJOINT'
#  export PV_LOGFILE=pr1-lic-b-ipd.log
#  qsub -N pss-pr1-ipd-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub
#
#  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-b.py
#  export PV_PORT=33114
#  export PV_TIME=2397096
#  export PV_COMPOSITE_STRATEGY='INPLACE'
#  export PV_LOGFILE=kh-new-jaguar-lic-b.log
#  qsub -N pss-kh-b-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub
#
#  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-ue.py
#  export PV_PORT=33116
#  export PV_TIME=1512960
#  export PV_COMPOSITE_STRATEGY='INPLACE'
#  export PV_LOGFILE=kh-new-jaguar-lic-ue.log
#  qsub -N pss-kh-ue-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub

  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-b-woce.py
  export PV_PORT=33114
  export PV_TIME=2397096
  export PV_COMPOSITE_STRATEGY='INPLACE'
  export PV_LOGFILE=kh-new-jaguar-lic-b-woce.log
  qsub -N pss-kh-b-woce-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub

  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-ue-woce.py
  export PV_PORT=33116
  export PV_TIME=1512960
  export PV_COMPOSITE_STRATEGY='INPLACE'
  export PV_LOGFILE=kh-new-jaguar-lic-ue-woce.log
  qsub -N pss-kh-ue-woce-$PV_NCPUS -V -q $QUEUE -l walltime=00:30:00 -l mppwidth=$PV_NCPUS -l mppnppn=$PV_NCPUS_PER_NODE ./pslic-scaling.qsub
done
