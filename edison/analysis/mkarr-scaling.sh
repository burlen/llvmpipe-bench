for d in `ls -d ../data/scaling-*`; do t=`grep -m 1 RenderInternal $d/kh-new-jaguar-lic-b.log | cut -d' ' -f5`; np=`echo $d | cut -d- -f2`; echo "khbce[$np]=$t"; done
for d in `ls -d ../data/scaling-*`; do t=`grep -m 1 RenderInternal $d/kh-new-jaguar-lic-b-woce.log | cut -d' ' -f5`; np=`echo $d | cut -d- -f2`; echo "khbwoce[$np]=$t"; done
