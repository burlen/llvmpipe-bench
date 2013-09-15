#!/bin/bash

ACCT=TG-STA110013S
export PV_HOME=/scratch/01237/bloring/ParaView/next/PV

#module swap mvapich2 mvapich2/1.4
module load python/2.6.5

function submit {

  local jobname=$PV_JOBNAME
  local logfile=$PV_LOGFILE
  local queue=normal
  local f="/some/file"
  local over_limit=1
  local match=0
  local njobs=0

  # need to use the special queue for
  # large jobs
  if (( $PV_NCPUS > 128 ))
  then
    queue=request
  fi

  # need to use the fat nodes for
  # small jobs
  if (( $PV_NCPUS < 32 ))
  then
    queue=largemem
  fi

  # test to see if this job was already
  # run to completion
  match=0
  for f in `ls ~/$jobname.o*`
  do
    grep "Wrote $logfile" $f
    if (( $? == 0 ))
    then
      let match=match+1
    fi
  done
  echo $match
  if (( $match != 0 ))
  then
    # it was already run
    echo "SKIPPED : $jobname was already completed successfully."
  else
    # submit a job for this file
    # only allowed 20 jobs in the queue
    over_limit=1
    while (( $over_limit == 1 ))
    do
      njobs=`qstat | wc -l`
      if (( $njobs < 10 ))
      then
        over_limit=0
      fi
    done

    echo "submitting $jobname..."
    qsub -j y -N $jobname -V -q $queue -A $ACCT -P vis -pe 8way $PV_NCPUS -l h_rt=00:30:00 ./pslic-scaling.qsub
  fi

}

for PV_NCPUS in `seq 128 8 128`
do
  echo "submitting for $PV_NCPUS cores"

  export PV_NCPUS
  export PV_NCPUS_PER_NODE=8
  export PV_NCPUS_PER_SOCKET=4
  export PV_WKD=`pwd`/

  export PV_SCRIPT=`pwd`/pr1-lic.py
  export PV_PORT=33110
  export PV_TIME=0.0
  export PV_COMPOSITE_STRATEGY='INPLACE'
  export PV_LOGFILE=pr1-lic-b-ip.log
  PV_JOBNAME=pss-pr1-ip-$PV_NCPUS
  submit

  export PV_SCRIPT=`pwd`/pr1-lic.py
  export PV_PORT=33112
  export PV_TIME=0.0
  export PV_COMPOSITE_STRATEGY='INPLACE DISJOINT'
  export PV_LOGFILE=pr1-lic-b-ipd.log
  PV_JOBNAME=pss-pr1-ipd-$PV_NCPUS
  submit

  export PV_SCRIPT=`pwd`/pr1-lic.py
  export PV_PORT=33114
  export PV_TIME=0.0
  export PV_COMPOSITE_STRATEGY='BALANCED'
  export PV_LOGFILE=pr1-lic-b-bal.log
  PV_JOBNAME=pss-pr1-bal-$PV_NCPUS
  submit

  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-b.py
  export PV_PORT=33116
  export PV_TIME=2397096
  export PV_COMPOSITE_STRATEGY='INPLACE'
  export PV_LOGFILE=kh-new-jaguar-lic-b.log
  PV_JOBNAME=pss-kh-b-$PV_NCPUS
  submit

#  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-ue.py
#  export PV_PORT=33118
#  export PV_TIME=1512960
#  export PV_COMPOSITE_STRATEGY='INPLACE'
#  export PV_LOGFILE=kh-new-jaguar-lic-ue.log
#  PV_JOBNAME=pss-kh-ue-$PV_NCPUS
#  submit

  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-b-woce.py
  export PV_PORT=33120
  export PV_TIME=2397096
  export PV_COMPOSITE_STRATEGY='INPLACE'
  export PV_LOGFILE=kh-new-jaguar-lic-b-woce.log
  PV_JOBNAME=pss-kh-b-woce-$PV_NCPUS
  submit

#  export PV_SCRIPT=`pwd`/kh-new-jaguar-lic-ue-woce.py
#  export PV_PORT=33122
#  export PV_TIME=1512960
#  export PV_COMPOSITE_STRATEGY='INPLACE'
#  export PV_LOGFILE=kh-new-jaguar-lic-ue-woce.log
#  PV_JOBNAME=pss-kh-ue-woce-$PV_NCPUS
#  submit

done
