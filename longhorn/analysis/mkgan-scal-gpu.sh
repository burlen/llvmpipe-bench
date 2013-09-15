#!/bin/bash

# for a single run with 16 rank
# strip out event times for each rank

echo -n "ip_ev=["
grep ^0 ../data/scaling-16/pr1-lic-b-ip.log | cut -d' ' -f2 | cut -d: -f3 | tr '\n' ','
echo "]"
for i in `seq 0 15`;
do
   echo -n  "ip_r$i=[";
   grep "^$i " ../data/scaling-16/pr1-lic-b-ip.log  | cut -d' ' -f5 | tr '\n' ', ';
   echo "]";
done

echo
echo
echo

echo -n "ipd_ev=["
grep ^0 ../data/scaling-16/pr1-lic-b-ipd.log | cut -d' ' -f2 | cut -d: -f3 | tr '\n' ','
echo "]"
for i in `seq 0 15`;
do
   echo -n "ipd_r$i=[";
   grep "^$i " ../data/scaling-16/pr1-lic-b-ipd.log  | cut -d' ' -f5 | tr '\n' ', ';
   echo "]";
done
