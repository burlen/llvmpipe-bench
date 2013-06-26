#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

mpl.rcParams['figure.dpi'] = 200
#figSize=mpl.rcParams['figure.figsize']
#mpl.rcParams['figure.figsize'] = [2*b[0] for b in zip(figSize)]

# small data
if 1:

  # results from missmarple
  #mm_threads = [1,     2,     4,     8,     16,    20,    24,    28,    32   ]
  #mm_time = [62.07 ,37.46 ,24.58 ,20.26 ,18.12 ,17.83 ,20.39 ,20.75 ,21.43]

  mm_threads=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  mm_time=[64.16, 37.00, 26.30, 21.42, 19.00, 18.96, 17.77, 18.21, 18.91, 17.88, 16.86, 16.52, 16.50, 15.98, 16.38, 16.41]
  t_nvidia = 1.06
  mm_nvx = [0, 48]
  mm_nvt = [1.06, 1.06]

  # results from edison
  ed_threads=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
  ed_time=[40.79, 23.62, 18.53, 14.78, 12.48, 10.85, 11.01, 10.52, 9.96, 9.47, 9.35, 8.87, 8.61, 7.95, 7.83, 8.06, 8.01, 8.02, 8.11, 8.28, 8.15, 8.19, 8.18, 8.68, 8.81, 8.78, 8.72, 9.02, 8.97, 8.70, 8.64, 8.94]
  edht_time=[40.13, 34.34, 20.79, 19.62, 15.33, 14.64, 12.08, 12.22, 11.12, 10.77, 10.27, 9.61, 9.24, 8.73, 8.31, 8.56, 8.53, 8.51, 8.38, 8.17, 8.10, 7.67, 7.92, 7.21, 7.50, 7.19, 7.30, 7.08, 7.14, 6.94, 7.13, 7.09]

  #results from hopper
  hop_threads=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
  hop_time=[150.58, 86.06, 63.19, 51.60, 35.58, 32.01, 29.95, 26.63, 25.17, 21.44, 21.00, 21.14, 22.94, 24.85, 22.59, 23.38, 23.07, 28.27, 23.89, 22.97, 15.79, 15.50, 17.07, 15.04, 15.91, 15.09, 16.19, 16.61, 16.18, 17.27, 17.08, 17.06, 18.51, 22.81, 22.69, 24.70, 25.94, 23.69, 24.55, 20.30, 18.37, 19.11, 19.48, 21.49, 18.51, 18.77, 19.96, 18.23]

  mpl.plot(mm_nvx, mm_nvt, 'b-', linewidth=2, label='missmarple.lbl Nvidia GTX 480')
  mpl.plot(mm_threads,mm_time,'r-',linewidth=2, label='missmarple.lbl 2x4 core Xeon E5630 2.53GHz')
  mpl.plot(ed_threads,ed_time,'k-',linewidth=2, label='edison.nersc 2x8 core Xeon E5-2670 2.60GHz')
  mpl.plot(ed_threads,edht_time,'c-',linewidth=2, label='edison.nersc w/ HT 2x8 core Xeon E5-2670 2.60GHz')
  mpl.plot(hop_threads,hop_time,'g-',linewidth=2, label='hopper.nersc 4x6 core Opteron 6172 2.1GHz')
  mpl.xlim(1,32)

  ticks=[2,4,8,16,24,32]
  mpl.xticks(ticks)

  #Surface LIC 756 Tri. Regression Data
  mpl.legend(prop={'size': 9})
  mpl.title('OS Mesa llvmpipe Single Process Performance\n Surface LIC 756 Tri. 4k it.',fontweight='bold')
  mpl.ylabel('seconds',fontweight='bold')
  mpl.xlabel('LP_NUM_THREADS',fontweight='bold')
  mpl.grid()

  fig = mpl.gcf()
  mpl.savefig('llvmpipe-1proc.png',dpi=200)
  mpl.savefig('llvmpipe-1proc-sm.png',dpi=80)
  #mpl.show()


# large data
if 1:
  a=np.zeros((16,16),np.float64)
  a[6-1][4-1]=169.132
  a[6-1][5-1]=142.974
  a[6-1][6-1]=132.53
  a[6-1][7-1]=125.154
  a[6-1][8-1]=119.574
  a[6-1][9-1]=113.457
  a[6-1][10-1]=107.305
  a[6-1][11-1]=105.541
  a[6-1][12-1]=102.697
  a[6-1][13-1]=100.49
  a[6-1][14-1]=97.3898
  a[6-1][15-1]=97.4166
  a[6-1][16-1]=102.751
  a[7-1][1-1]=516.864
  a[7-1][2-1]=267.431
  a[7-1][3-1]=199.03
  a[7-1][4-1]=165.916
  a[7-1][5-1]=146.423
  a[7-1][6-1]=135.255
  a[7-1][7-1]=130.4
  a[7-1][8-1]=120.734
  a[7-1][9-1]=113.927
  a[7-1][10-1]=107.472
  a[7-1][11-1]=105.835
  a[7-1][12-1]=102.559
  a[7-1][13-1]=100.128
  a[7-1][14-1]=96.8069
  a[7-1][15-1]=99.0209
  a[7-1][16-1]=98.1807
  a[8-1][1-1]=508.036
  a[8-1][2-1]=272.365
  a[8-1][3-1]=194.624
  a[8-1][4-1]=163.092
  a[8-1][5-1]=148.678
  a[8-1][6-1]=136.639
  a[8-1][7-1]=127.531
  a[8-1][8-1]=121.81
  a[8-1][9-1]=114.386
  a[8-1][10-1]=108.263
  a[8-1][11-1]=105.371
  a[8-1][12-1]=102.965
  a[8-1][13-1]=100.465
  a[8-1][14-1]=98.7924
  a[8-1][15-1]=96.8367
  a[8-1][16-1]=96.0931
  a[9-1][1-1]=502.086
  a[9-1][2-1]=269.656
  a[9-1][3-1]=193.037
  a[9-1][4-1]=168.853
  a[9-1][5-1]=149.943
  a[9-1][6-1]=138.117
  a[9-1][7-1]=129.845
  a[9-1][8-1]=122.351
  a[9-1][9-1]=114.343
  a[9-1][10-1]=108.13
  a[9-1][11-1]=106.065
  a[9-1][12-1]=104.14
  a[9-1][13-1]=100.833
  a[9-1][14-1]=98.5761
  a[9-1][15-1]=99.6839
  a[9-1][16-1]=94.9788
  a[10-1][1-1]=491.129
  a[10-1][2-1]=267.182
  a[10-1][3-1]=190.379
  a[10-1][4-1]=172.108
  a[10-1][5-1]=152.922
  a[10-1][6-1]=139.213
  a[10-1][7-1]=129.542
  a[10-1][8-1]=122.651
  a[10-1][9-1]=115.536
  a[1-1][1-1]=1007.9
  a[10-1][10-1]=108.509
  a[10-1][11-1]=106.495
  a[10-1][12-1]=102.439
  a[10-1][13-1]=99.939
  a[10-1][14-1]=97.922
  a[10-1][15-1]=99.7396
  a[10-1][16-1]=95.1783
  a[11-1][1-1]=484.501
  a[11-1][2-1]=272.795
  a[11-1][3-1]=195.695
  a[1-1][2-1]=550.793
  a[11-1][4-1]=173.473
  a[11-1][5-1]=154.491
  a[11-1][6-1]=138.751
  a[11-1][7-1]=129.577
  a[11-1][8-1]=121.717
  a[11-1][9-1]=116.076
  a[11-1][10-1]=108.895
  a[11-1][11-1]=106.4
  a[11-1][12-1]=103.837
  a[11-1][13-1]=99.6134
  a[1-1][3-1]=364.99
  a[11-1][14-1]=96.4009
  a[11-1][15-1]=96.9729
  a[11-1][16-1]=94.6873
  a[12-1][1-1]=481.631
  a[12-1][2-1]=267.901
  a[12-1][3-1]=199.668
  a[12-1][4-1]=173.348
  a[12-1][5-1]=154.655
  a[12-1][6-1]=140.983
  a[12-1][7-1]=129.441
  a[1-1][4-1]=297.131
  a[12-1][8-1]=122.701
  a[12-1][9-1]=115.113
  a[12-1][10-1]=109.267
  a[12-1][11-1]=107.129
  a[12-1][12-1]=102.55
  a[12-1][13-1]=100.007
  a[12-1][14-1]=96.4291
  a[12-1][15-1]=95.9789
  a[12-1][16-1]=93.5132
  a[13-1][1-1]=485.199
  a[1-1][5-1]=252.48
  a[13-1][2-1]=274.138
  a[13-1][3-1]=200.834
  a[13-1][4-1]=171.509
  a[13-1][5-1]=152.317
  a[13-1][6-1]=140.375
  a[13-1][7-1]=129.795
  a[13-1][8-1]=121.847
  a[13-1][9-1]=115.939
  a[13-1][10-1]=108.946
  a[13-1][11-1]=106.735
  a[1-1][6-1]=224.116
  a[13-1][12-1]=103.019
  a[13-1][13-1]=100.058
  a[13-1][14-1]=94.3551
  a[13-1][15-1]=94.9462
  a[13-1][16-1]=94.1517
  a[14-1][1-1]=470.985
  a[14-1][2-1]=271.07
  a[14-1][3-1]=200.596
  a[14-1][4-1]=172.533
  a[14-1][5-1]=152.638
  a[1-1][7-1]=195.153
  a[14-1][6-1]=139.319
  a[14-1][7-1]=130.463
  a[14-1][8-1]=123.65
  a[14-1][9-1]=116.274
  a[14-1][10-1]=109.14
  a[14-1][11-1]=106.555
  a[14-1][12-1]=102.76
  a[14-1][13-1]=97.94
  a[14-1][14-1]=94.4615
  a[14-1][15-1]=95.6358
  a[1-1][8-1]=168.354
  a[14-1][16-1]=95.6711
  a[15-1][1-1]=473.11
  a[15-1][2-1]=270.613
  a[15-1][3-1]=203.753
  a[15-1][4-1]=173.105
  a[15-1][5-1]=153.382
  a[15-1][6-1]=139.773
  a[15-1][7-1]=129.908
  a[15-1][8-1]=122.547
  a[15-1][9-1]=116.297
  a[1-1][9-1]=154.079
  a[15-1][10-1]=109.747
  a[15-1][11-1]=107.134
  a[15-1][12-1]=102.63
  a[15-1][13-1]=99.6386
  a[15-1][14-1]=94.3018
  a[15-1][15-1]=97.061
  a[15-1][16-1]=97.3994
  a[16-1][1-1]=467.338
  a[16-1][2-1]=268.873
  a[16-1][3-1]=201.454
  a[1-1][10-1]=141.603
  a[16-1][4-1]=172.739
  a[16-1][5-1]=152.863
  a[16-1][6-1]=140.719
  a[16-1][7-1]=129.968
  a[16-1][8-1]=123.928
  a[16-1][9-1]=117.73
  a[16-1][10-1]=109.305
  a[16-1][11-1]=106.396
  a[16-1][12-1]=101.524
  a[16-1][13-1]=97.5687
  a[1-1][11-1]=134.678
  a[16-1][14-1]=94.7827
  a[16-1][15-1]=96.2361
  a[16-1][16-1]=94.0615
  a[1-1][12-1]=126.38
  a[1-1][13-1]=119.052
  a[1-1][14-1]=113.071
  a[1-1][15-1]=118.956
  a[1-1][16-1]=125.707
  a[2-1][1-1]=777.188
  a[2-1][2-1]=407.231
  a[2-1][3-1]=280.416
  a[2-1][4-1]=217.527
  a[2-1][5-1]=185.129
  a[2-1][6-1]=157.183
  a[2-1][7-1]=142.38
  a[2-1][8-1]=128.898
  a[2-1][9-1]=119.578
  a[2-1][10-1]=113.58
  a[2-1][11-1]=111.73
  a[2-1][12-1]=105.361
  a[2-1][13-1]=100.342
  a[2-1][14-1]=96.6284
  a[2-1][15-1]=98.456
  a[2-1][16-1]=94.9187
  a[3-1][1-1]=640.871
  a[3-1][2-1]=322.025
  a[3-1][3-1]=231.463
  a[3-1][4-1]=182.67
  a[3-1][5-1]=159.659
  a[3-1][6-1]=140.246
  a[3-1][7-1]=132.833
  a[3-1][8-1]=120.222
  a[3-1][9-1]=111.828
  a[3-1][10-1]=102.987
  a[3-1][11-1]=102.829
  a[3-1][12-1]=99.4352
  a[3-1][13-1]=97.738
  a[3-1][14-1]=95.2811
  a[3-1][15-1]=100.813
  a[3-1][16-1]=96.1579
  a[4-1][1-1]=589.005
  a[4-1][2-1]=297.05
  a[4-1][3-1]=211.8
  a[4-1][4-1]=178.349
  a[4-1][5-1]=151.268
  a[4-1][6-1]=134.549
  a[4-1][7-1]=125.707
  a[4-1][8-1]=114.159
  a[4-1][9-1]=110.529
  a[4-1][10-1]=102.478
  a[4-1][11-1]=102.706
  a[4-1][12-1]=104.456
  a[4-1][13-1]=96.5682
  a[4-1][14-1]=96.2393
  a[4-1][15-1]=98.6982
  a[4-1][16-1]=96.1018
  a[5-1][1-1]=558.649
  a[5-1][2-1]=297.309
  a[5-1][3-1]=203.407
  a[5-1][4-1]=169.447
  a[5-1][5-1]=145.175
  a[5-1][6-1]=129.716
  a[5-1][7-1]=124.851
  a[5-1][8-1]=121.26
  a[5-1][9-1]=112.831
  a[5-1][10-1]=105.985
  a[5-1][11-1]=105.235
  a[5-1][12-1]=101.76
  a[5-1][13-1]=101.656
  a[5-1][14-1]=98.2356
  a[5-1][15-1]=100.111
  a[5-1][16-1]=97.4923
  a[6-1][1-1]=540.216
  a[6-1][2-1]=284.324
  a[6-1][3-1]=197.475


  idx=np.argmin(a)
  yid=idx/16
  xid=idx%16


  print 'fastest run time'
  print np.min(a)
  print 'ranks x threads'
  print xid
  print yid
  print a[yid][xid]
  print '% diff of 16x16 case to the fastest'
  print (a[15][15]-a[yid][xid])/a[yid][xid]
  print 

  idxf=np.argmin(a)
  yidf=idxf/16
  xidf=idxf%16

  idxs=np.argmax(a)
  yids=idxs/16
  xids=idxs%16

  print 'fastest total rendering time'
  print np.min(a)
  print 'ranks x threads'
  print xidf
  print yidf
  print a[yidf][xidf]

  print 'slowest total rendering time'
  print np.max(a)
  print 'ranks x threads'
  print xids
  print yids
  print a[yids][xids]

  print 'speed up'
  print a[yids][xids]/a[yidf][xidf]


  #mpl.contour(a,128)
  #mpl.show()
  # \nSurface LIC 52.4M Tri 2D VPIC Data
  x = y = np.arange(1, 17)
  X, Y = np.meshgrid(x, y)
  fig = mpl.figure()
  ax = fig.gca(projection='3d')
  surf = ax.plot_surface(X, Y, a, rstride=1, cstride=1, cmap=cm.coolwarm,
          linewidth=1, antialiased=True)
  ax.set_xlabel('Num. MPI Ranks',fontweight='bold', fontsize='10')
  ax.set_ylabel('Num. threads Per\n MPI Rank', fontweight='bold',fontsize='10')
  ax.set_zlabel('time (sec)', fontweight='bold',fontsize='10')
  mpl.title('OS Mesa llvmpipe Edison Single Node Performance\n MPI+pthreads Surface LIC 54M Tri. 10k it.',fontweight='bold',fontsize='12')

  ax.azim += 40;
  fig = mpl.gcf()
  mpl.savefig('llvmpipe-edison-1node.png',dpi=200)
  mpl.savefig('llvmpipe-edison-1node-sm.png',dpi=80)
  #mpl.show()




# gant for mpi 16 x threads 16 on edison
if 1:
  rank0=[32.5349,
  1.78882,
  58.9621,
  0.140097,
  0.188306,
  0.0774481,
  94.0615]

  rank1=[32.9077,
  1.51634,
  58.8862,
  0.148117,
  0.122565,
  0.0779059,
  94.0042]

  rank2=[33.4998,
  0.863452,
  58.9617,
  0.141177,
  0.119136,
  0.076627,
  94.0063]

  rank3=[32.7067,
  1.72561,
  58.8936,
  0.136232,
  0.135577,
  0.077354,
  94.0191]

  rank4=[32.7642,
  1.67912,
  58.8827,
  0.133961,
  0.126359,
  0.129915,
  94.0603]

  rank5=[32.3881,
  2.04724,
  58.8907,
  0.133312,
  0.128521,
  0.075062,
  94.007]

  rank6=[32.5385,
  1.8966,
  58.89,
  0.140469,
  0.119699,
  0.13005,
  94.0597]

  rank7=[32.3921,
  2.04309,
  58.8907,
  0.138181,
  0.122675,
  0.076308,
  94.0071]

  rank8=[32.3968,
  2.02055,
  58.9086,
  0.144639,
  0.126077,
  0.0776551,
  94.0184]

  rank9=[33.1979,
  1.17931,
  58.9086,
  0.139152,
  0.121035,
  0.0789521,
  93.9948]

  rank10=[32.0617,
  2.3047,
  58.9586,
  0.137966,
  0.122371,
  0.076813,
  94.0065]

  rank11=[32.5191,
  1.84739,
  58.9584,
  0.138631,
  0.132303,
  0.0777018,
  94.018]

  rank12=[34.2234,
  0.1407,
  58.9612,
  0.152353,
  0.107971,
  0.0773721,
  94.0071]

  rank13=[32.8556,
  1.51304,
  58.9573,
  0.136108,
  0.124153,
  0.076694,
  94.007]

  rank14=[33.9385,
  0.407941,
  58.9631,
  0.142338,
  0.186104,
  0.0774322,
  94.0615]

  rank15=[32.5208,
  1.84628,
  58.958,
  0.13228,
  0.128392,
  0.0780151,
  94.0081]

  #groups=('RenderGeometry',
  #'GatherVectors',
  #'ComputeLIC',
  #'ColorLIC',
  #'ContrastEnhance',
  #'DepthCopy')
  #'vtkSurfaceLICPainter::RenderInternal')

  groupData=[[],[],[],[],[],[],[]]
  i=0
  while i<7:
    groupData[i]=[rank0[i],
        rank1[i],
        rank2[i],
        rank3[i],
        rank4[i],
        rank5[i],
        rank6[i],
        rank7[i],
        rank8[i],
        rank9[i],
        rank10[i],
        rank11[i],
        rank12[i],
        rank13[i],
        rank14[i],
        rank15[i]]

    #print groups[i]
    #print groupData[i]
    i+=1

  groupDataBot=[[],[],[],[],[],[],[]]
  groupDataBot[0]=[0]*16
  i=1
  while i<6:
    tmp0=groupDataBot[i-1]
    tmp1=groupData[i-1]
    tmp2=[sum(d) for d in (zip(*[tmp0,tmp1]))]
    groupDataBot[i]=tmp2
    #print
    #print groups[i]
    #print groupDataBot[i-1]
    #print '+'
    #print groupData[i-1]
    #print '='
    #print groupDataBot[i]
    i+=1

  groupPlots=[[],[],[],[],[],[],[]]
  #groupColors=['r','g','b','c','m','y','p']
  groupColors=['c','g','y','m','r','b']

  ranks=np.arange(16)-0.5

  mpl.subplot(121)
  groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
  i=1
  while i<6:
    groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
    i+=1

  mpl.subplots_adjust(right=1.125,hspace=0.05)
  #pl.title('Edison Node Per Rank Activity\n 16 MPI x 16 threads per', fontweight='bold')
  mpl.title('OS Mesa llvmpipe Edison Single Node Performance\n Activity by Rank Surface LIC 54M Tri. 10k it.\n 16 MPI Ranks x 16 Threads per Rank\n',fontweight='bold',fontsize='12')
  mpl.xlabel('MPI Rank', fontweight='bold')
  mpl.xlim([-0.75, 15.5])
  #mpl.ylim([0, 140])
  mpl.ylabel('time (sec)', fontweight='bold')
  mpl.grid()

  groups=('Vertex Processing & Vector Projection',
  'Composite & Guard Pixel Exch.',
  'LIC Computation',
  'Scalar Color Shading',
  'Contrast Enhance',
  'Fragment Depth Test')

  mpl.legend((groupPlots[0],
    groupPlots[1],
    groupPlots[2],
    groupPlots[3],
    groupPlots[4],
    groupPlots[5]),
    groups,
    prop={'size': 9},
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

  mpl.subplots_adjust(top=0.85)

  fig = mpl.gcf()
  mpl.savefig('llvmpipe-edison-1node-16mpi-activity.png',dpi=200)
  mpl.savefig('llvmpipe-edison-1node-16mpi-activity-sm.png',dpi=80)
  #mpl.show()

tid1=[422.279,
0.165306,
584.773,
0.137389,
0.133167,
0.0943279,
1007.9]

tid2=[424.113,
0.153341,
352.268,
0.132789,
0.122756,
0.08408,
777.188]

tid3=[411.667,
0.146932,
228.422,
0.126023,
0.116418,
0.0785301,
640.871]

tid4=[412.197,
0.146485,
176.038,
0.123075,
0.111956,
0.0749569,
589.005]

tid6=[416.142,
0.145438,
123.307,
0.121813,
0.111794,
0.0741489,
540.216]

tid9=[415.593,
0.141701,
85.7382,
0.118896,
0.108184,
0.0721021,
502.086]

tid10=[412.028,
0.142278,
78.3434,
0.120335,
0.109046,
0.0718288,
491.129]

tid11=[410.481,
0.144271,
73.2661,
0.117612,
0.107225,
0.0707321,
484.501]

tid13=[418.833,
0.143412,
65.6109,
0.119715,
0.108001,
0.07112,
485.199]

tid15=[414.119,
0.142573,
58.2395,
0.11758,
0.107334,
0.0704679,
473.11]

tid5=[415.204,
0.146711,
142.675,
0.123032,
0.112078,
0.0746949,
558.649]

tid7=[409.211,
0.144501,
106.89,
0.120841,
0.110523,
0.073004,
516.864]

tid8=[413.661,
0.143845,
93.616,
0.119489,
0.109532,
0.0725398,
508.036]

tid12=[411.457,
0.142271,
69.4206,
0.118667,
0.107811,
0.0711021,
481.631]

tid14=[407.461,
0.143269,
62.7686,
0.119998,
0.106882,
0.0711241,
470.985]

tid16=[407.001,
0.14372,
59.5837,
0.118125,
0.107349,
0.0705788,
467.338]

groups=['RenderGeometry',
'GatherVectors',
'ComputeLIC',
'ColorLIC',
'ContrastEnhance',
'DepthCopy',
'vtkSurfaceLICPainter::RenderInternal']

groupData=[[],[],[],[],[],[],[]]
i=0
while i<7:
  groupData[i]=[tid1[i],
      tid2[i],
      tid3[i],
      tid4[i],
      tid5[i],
      tid6[i],
      tid7[i],
      tid8[i],
      tid9[i],
      tid10[i],
      tid11[i],
      tid12[i],
      tid13[i],
      tid14[i],
      tid15[i],
      tid16[i]]
  #print groups[i]
  #print groupData[i]
  i+=1

groupDataBot=[[],[],[],[],[],[],[]]
groupDataBot[0]=[0]*16
i=1
while i<7:
  tmp0=groupDataBot[i-1]
  tmp1=groupData[i-1]
  tmp2=[sum(d) for d in (zip(*[tmp0,tmp1]))]
  groupDataBot[i]=tmp2
  #print
  #print groups[i]
  #print groupDataBot[i-1]
  #print '+'
  #print groupData[i-1]
  #print '='
  #print groupDataBot[i]
  i+=1


fig = mpl.figure()
ax = fig.add_subplot(111)

groupColors=['c','g','y','m','r','b']

t=np.arange(1, 17)

i=0
while i<6:
  ax.fill_between(t,groupDataBot[i], groupDataBot[i+1], facecolor=groupColors[i],linewidth=0)
  i+=1

mpl.grid()
mpl.xlim([1, 16])
mpl.ylim([0, 1100])
mpl.xlabel('Number of Threads', fontweight='bold')
mpl.ylabel('Time (sec)', fontweight='bold')
mpl.title('OS Mesa llvmpipe Edison Single Node Performance\n 1 MPI Rank+n pthreads Surface LIC 54M Tri. 10k it.',fontweight='bold',fontsize='12')

#mpl.title('OS Mesa llvmpipe\nSingle Process Performance Edison')

groups=('Vertex Processing & Vector Projection',
'Composite & Guard Pixel Exch.',
'LIC Computation',
'Scalar Color Shading',
'Contrast Enhance',
'Fragment Depth Test')

mpl.legend((groupPlots[0],
  groupPlots[1],
  groupPlots[2],
  groupPlots[3],
  groupPlots[4],
  groupPlots[5]),
  groups,
  prop={'size': 9})
#  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

fig = mpl.gcf()
mpl.savefig('llvmpipe-edison-1node-1rank-threads.png',dpi=200)
mpl.savefig('llvmpipe-edison-1node-1rank-threads-sm.png',dpi=80)
#mpl.show()



# vertex pipeline time
renGeomT=np.zeros((16,16),np.float64)
renGeomT[6-1][4-1]=109.092
renGeomT[6-1][5-1]=88.0594
renGeomT[6-1][6-1]=73.1194
renGeomT[6-1][7-1]=63.245
renGeomT[6-1][8-1]=56.7789
renGeomT[6-1][9-1]=49.7155
renGeomT[6-1][10-1]=43.1637
renGeomT[6-1][11-1]=40.6872
renGeomT[6-1][12-1]=36.3183
renGeomT[6-1][13-1]=33.5186
renGeomT[6-1][14-1]=32.3751
renGeomT[6-1][15-1]=33.9868
renGeomT[6-1][16-1]=35.4851
renGeomT[7-1][1-1]=409.211
renGeomT[7-1][2-1]=211.016
renGeomT[7-1][3-1]=138.003
renGeomT[7-1][4-1]=109.218
renGeomT[7-1][5-1]=87.4608
renGeomT[7-1][6-1]=73.1295
renGeomT[7-1][7-1]=66.7576
renGeomT[7-1][8-1]=55.6525
renGeomT[7-1][9-1]=49.0702
renGeomT[7-1][10-1]=43.4207
renGeomT[7-1][11-1]=40.6212
renGeomT[7-1][12-1]=36.8588
renGeomT[7-1][13-1]=34.7442
renGeomT[7-1][14-1]=32.2764
renGeomT[7-1][15-1]=35.7098
renGeomT[7-1][16-1]=35.4328
renGeomT[8-1][1-1]=413.661
renGeomT[8-1][2-1]=211.069
renGeomT[8-1][3-1]=137.085
renGeomT[8-1][4-1]=109.255
renGeomT[8-1][5-1]=87.491
renGeomT[8-1][6-1]=73.2795
renGeomT[8-1][7-1]=63.1312
renGeomT[8-1][8-1]=55.3586
renGeomT[8-1][9-1]=48.3677
renGeomT[8-1][10-1]=43.7447
renGeomT[8-1][11-1]=40.1869
renGeomT[8-1][12-1]=37.5624
renGeomT[8-1][13-1]=34.1959
renGeomT[8-1][14-1]=32.5803
renGeomT[8-1][15-1]=34.0734
renGeomT[8-1][16-1]=31.9772
renGeomT[9-1][1-1]=415.593
renGeomT[9-1][2-1]=214.405
renGeomT[9-1][3-1]=137.805
renGeomT[9-1][4-1]=108.282
renGeomT[9-1][5-1]=86.299
renGeomT[9-1][6-1]=73.1882
renGeomT[9-1][7-1]=62.6589
renGeomT[9-1][8-1]=55.7961
renGeomT[9-1][9-1]=49.2426
renGeomT[9-1][10-1]=42.9277
renGeomT[9-1][11-1]=40.0838
renGeomT[9-1][12-1]=36.4892
renGeomT[9-1][13-1]=34.7385
renGeomT[9-1][14-1]=34.3376
renGeomT[9-1][15-1]=34.1413
renGeomT[9-1][16-1]=32.795
renGeomT[10-1][1-1]=412.028
renGeomT[10-1][2-1]=209.517
renGeomT[10-1][3-1]=135.676
renGeomT[10-1][4-1]=109.004
renGeomT[10-1][5-1]=86.2403
renGeomT[10-1][6-1]=73.8052
renGeomT[10-1][7-1]=63.1192
renGeomT[10-1][8-1]=56.9927
renGeomT[10-1][9-1]=50.0027
renGeomT[1-1][1-1]=422.279
renGeomT[10-1][10-1]=43.5414
renGeomT[10-1][11-1]=41.0597
renGeomT[10-1][12-1]=36.4144
renGeomT[10-1][13-1]=34.6607
renGeomT[10-1][14-1]=32.0151
renGeomT[10-1][15-1]=36.0207
renGeomT[10-1][16-1]=32.8331
renGeomT[11-1][1-1]=410.481
renGeomT[11-1][2-1]=218.136
renGeomT[11-1][3-1]=139.904
renGeomT[1-1][2-1]=215.974
renGeomT[11-1][4-1]=108.954
renGeomT[11-1][5-1]=87.6551
renGeomT[11-1][6-1]=73.4623
renGeomT[11-1][7-1]=63.0434
renGeomT[11-1][8-1]=54.9028
renGeomT[11-1][9-1]=49.2498
renGeomT[11-1][10-1]=43.9819
renGeomT[11-1][11-1]=39.3804
renGeomT[11-1][12-1]=37.0114
renGeomT[11-1][13-1]=34.2723
renGeomT[1-1][3-1]=140.095
renGeomT[11-1][14-1]=33.1844
renGeomT[11-1][15-1]=34.3774
renGeomT[11-1][16-1]=32.0551
renGeomT[12-1][1-1]=411.457
renGeomT[12-1][2-1]=211.468
renGeomT[12-1][3-1]=139.877
renGeomT[12-1][4-1]=105.847
renGeomT[12-1][5-1]=89.364
renGeomT[12-1][6-1]=72.8842
renGeomT[12-1][7-1]=64.3179
renGeomT[1-1][4-1]=107.964
renGeomT[12-1][8-1]=55.5137
renGeomT[12-1][9-1]=49.9346
renGeomT[12-1][10-1]=44.5087
renGeomT[12-1][11-1]=39.6049
renGeomT[12-1][12-1]=37.0841
renGeomT[12-1][13-1]=34.3966
renGeomT[12-1][14-1]=32.2149
renGeomT[12-1][15-1]=34.3926
renGeomT[12-1][16-1]=32.0641
renGeomT[13-1][1-1]=418.833
renGeomT[1-1][5-1]=90.3059
renGeomT[13-1][2-1]=219.386
renGeomT[13-1][3-1]=139.939
renGeomT[13-1][4-1]=107.324
renGeomT[13-1][5-1]=86.0862
renGeomT[13-1][6-1]=73.038
renGeomT[13-1][7-1]=63.7552
renGeomT[13-1][8-1]=56.1092
renGeomT[13-1][9-1]=50.5544
renGeomT[13-1][10-1]=43.1001
renGeomT[13-1][11-1]=40.9229
renGeomT[1-1][6-1]=74.9504
renGeomT[13-1][12-1]=37.6457
renGeomT[13-1][13-1]=34.9631
renGeomT[13-1][14-1]=32.3588
renGeomT[13-1][15-1]=34.9051
renGeomT[13-1][16-1]=32.7933
renGeomT[14-1][1-1]=407.461
renGeomT[14-1][2-1]=213.378
renGeomT[14-1][3-1]=138.927
renGeomT[14-1][4-1]=106.754
renGeomT[14-1][5-1]=87.0112
renGeomT[1-1][7-1]=64.2281
renGeomT[14-1][6-1]=72.2967
renGeomT[14-1][7-1]=64.5289
renGeomT[14-1][8-1]=57.5048
renGeomT[14-1][9-1]=49.3833
renGeomT[14-1][10-1]=43.0274
renGeomT[14-1][11-1]=40.3883
renGeomT[14-1][12-1]=36.8785
renGeomT[14-1][13-1]=34.0028
renGeomT[14-1][14-1]=32.5781
renGeomT[14-1][15-1]=35.7204
renGeomT[1-1][8-1]=56.532
renGeomT[14-1][16-1]=33.4267
renGeomT[15-1][1-1]=414.119
renGeomT[15-1][2-1]=217.747
renGeomT[15-1][3-1]=139.731
renGeomT[15-1][4-1]=106.973
renGeomT[15-1][5-1]=88.3495
renGeomT[15-1][6-1]=73.8287
renGeomT[15-1][7-1]=63.8849
renGeomT[15-1][8-1]=56.6074
renGeomT[15-1][9-1]=50.0214
renGeomT[1-1][9-1]=51.5035
renGeomT[15-1][10-1]=45.0847
renGeomT[15-1][11-1]=41.2142
renGeomT[15-1][12-1]=37.1302
renGeomT[15-1][13-1]=34.273
renGeomT[15-1][14-1]=32.6535
renGeomT[15-1][15-1]=38.1699
renGeomT[15-1][16-1]=37.0814
renGeomT[16-1][1-1]=407.001
renGeomT[16-1][2-1]=211.515
renGeomT[16-1][3-1]=137.513
renGeomT[1-1][10-1]=44.2055
renGeomT[16-1][4-1]=107.04
renGeomT[16-1][5-1]=87.531
renGeomT[16-1][6-1]=72.5148
renGeomT[16-1][7-1]=63.8464
renGeomT[16-1][8-1]=56.4129
renGeomT[16-1][9-1]=49.0392
renGeomT[16-1][10-1]=44.0067
renGeomT[16-1][11-1]=40.1229
renGeomT[16-1][12-1]=36.9683
renGeomT[16-1][13-1]=34.7034
renGeomT[1-1][11-1]=41.1101
renGeomT[16-1][14-1]=32.6688
renGeomT[16-1][15-1]=34.5211
renGeomT[16-1][16-1]=32.5349
renGeomT[1-1][12-1]=37.3949
renGeomT[1-1][13-1]=35.035
renGeomT[1-1][14-1]=31.6511
renGeomT[1-1][15-1]=46.0222
renGeomT[1-1][16-1]=32.9175
renGeomT[2-1][1-1]=424.113
renGeomT[2-1][2-1]=213.723
renGeomT[2-1][3-1]=137.4
renGeomT[2-1][4-1]=107.072
renGeomT[2-1][5-1]=85.9562
renGeomT[2-1][6-1]=73.5742
renGeomT[2-1][7-1]=63.4702
renGeomT[2-1][8-1]=55.5111
renGeomT[2-1][9-1]=49.3423
renGeomT[2-1][10-1]=42.4772
renGeomT[2-1][11-1]=39.7691
renGeomT[2-1][12-1]=37.1779
renGeomT[2-1][13-1]=34.3317
renGeomT[2-1][14-1]=32.748
renGeomT[2-1][15-1]=34.2392
renGeomT[2-1][16-1]=32.301
renGeomT[3-1][1-1]=411.667
renGeomT[3-1][2-1]=210.824
renGeomT[3-1][3-1]=138.216
renGeomT[3-1][4-1]=107.154
renGeomT[3-1][5-1]=87.7023
renGeomT[3-1][6-1]=73.4413
renGeomT[3-1][7-1]=65.1457
renGeomT[3-1][8-1]=56.5665
renGeomT[3-1][9-1]=49.3575
renGeomT[3-1][10-1]=43.8
renGeomT[3-1][11-1]=40.9349
renGeomT[3-1][12-1]=37.6128
renGeomT[3-1][13-1]=33.9861
renGeomT[3-1][14-1]=32.3781
renGeomT[3-1][15-1]=35.4577
renGeomT[3-1][16-1]=31.8137
renGeomT[4-1][1-1]=412.197
renGeomT[4-1][2-1]=210.526
renGeomT[4-1][3-1]=137.644
renGeomT[4-1][4-1]=109.115
renGeomT[4-1][5-1]=87.7655
renGeomT[4-1][6-1]=72.9951
renGeomT[4-1][7-1]=64.7202
renGeomT[4-1][8-1]=55.1217
renGeomT[4-1][9-1]=48.0531
renGeomT[4-1][10-1]=43.1236
renGeomT[4-1][11-1]=40.3192
renGeomT[4-1][12-1]=35.8197
renGeomT[4-1][13-1]=34.2183
renGeomT[4-1][14-1]=32.2314
renGeomT[4-1][15-1]=33.6265
renGeomT[4-1][16-1]=32.151
renGeomT[5-1][1-1]=415.204
renGeomT[5-1][2-1]=212.167
renGeomT[5-1][3-1]=138.645
renGeomT[5-1][4-1]=106.033
renGeomT[5-1][5-1]=87.3917
renGeomT[5-1][6-1]=73.3912
renGeomT[5-1][7-1]=62.8726
renGeomT[5-1][8-1]=60.1754
renGeomT[5-1][9-1]=50.8924
renGeomT[5-1][10-1]=43.2293
renGeomT[5-1][11-1]=39.3018
renGeomT[5-1][12-1]=36.7803
renGeomT[5-1][13-1]=34.0267
renGeomT[5-1][14-1]=32.385
renGeomT[5-1][15-1]=35.6098
renGeomT[5-1][16-1]=33.7101
renGeomT[6-1][1-1]=416.142
renGeomT[6-1][2-1]=212.558
renGeomT[6-1][3-1]=137.644

idxf=np.argmin(renGeomT)
yidf=idxf/16
xidf=idxf%16

idxs=np.argmax(renGeomT)
yids=idxs/16
xids=idxs%16

print 'fastest geometry rendering time'
print np.min(renGeomT)
print 'ranks x threads'
print xidf
print yidf
print renGeomT[yidf][xidf]

print 'slowest geometry rendering time'
print np.max(renGeomT)
print 'ranks x threads'
print xids
print yids
print renGeomT[yids][xids]

print 'speed up'
print renGeomT[yids][xids]/renGeomT[yidf][xidf]



rid2=[
211.515,
7.57627,
49.1714,
0.123308,
0.103962,
0.0693479,
268.873]

rid4=[
107.04,
0.121371,
64.9617,
0.119196,
0.108901,
0.071928,
172.739]

rid7=[
63.8464,
0.486612,
65.0009,
0.128461,
0.105777,
0.072859,
129.968]

rid8=[
56.4129,
1.19762,
65.6729,
0.135031,
0.103219,
0.0732481,
123.928]

rid9=[
49.0392,
3.31544,
64.7242,
0.129274,
0.116403,
0.0801959,
117.73]

rid10=[
44.0067,
0.630403,
64.0145,
0.140282,
0.10423,
0.075546,
109.305]

rid12=[
36.9683,
0.804046,
63.0974,
0.131217,
0.115039,
0.0744388,
101.524]

rid13=[
34.7034,
0.725159,
61.469,
0.13222,
0.120486,
0.0738509,
97.5687]

rid1=[
407.001,
0.14372,
59.5837,
0.118125,
0.107349,
0.0705788,
467.338]

rid3=[
137.513,
0.572094,
62.7582,
0.121578,
0.102,
0.071552,
201.454]

rid5=[
87.531,
0.684823,
64.0198,
0.126261,
0.106804,
0.0714698,
152.863]

rid6=[
72.5148,
2.7876,
64.782,
0.131413,
0.108248,
0.07196,
140.719]

rid11=[
40.1229,
0.867718,
64.7443,
0.135095,
0.114416,
0.0773869,
106.396]

rid14=[
32.6688,
2.23357,
59.1903,
0.139912,
0.119235,
0.0863981,
94.7827]

rid16=[
32.5349,
1.78882,
58.9621,
0.140097,
0.188306,
0.0774481,
94.0615]

rid15=[
34.5211,
2.39653,
58.6027,
0.134191,
0.162932,
0.0743761,
96.2361]

groups=['RenderGeometry',
'GatherVectors',
'ComputeLIC',
'ColorLIC',
'ContrastEnhance',
'DepthCopy',
'vtkSurfaceLICPainter::RenderInternal']

groupData=[[],[],[],[],[],[],[]]
i=0
while i<7:
  groupData[i]=[rid1[i],
      rid2[i],
      rid3[i],
      rid4[i],
      rid5[i],
      rid6[i],
      rid7[i],
      rid8[i],
      rid9[i],
      rid10[i],
      rid11[i],
      rid12[i],
      rid13[i],
      rid14[i],
      rid15[i],
      rid16[i]]
  #print groups[i]
  #print groupData[i]
  i+=1

groupDataBot=[[],[],[],[],[],[],[]]
groupDataBot[0]=[0]*16
i=1
while i<7:
  tmp0=groupDataBot[i-1]
  tmp1=groupData[i-1]
  tmp2=[sum(d) for d in (zip(*[tmp0,tmp1]))]
  groupDataBot[i]=tmp2
  #print
  #print groups[i]
  #print groupDataBot[i-1]
  #print '+'
  #print groupData[i-1]
  #print '='
  #print groupDataBot[i]
  i+=1


fig = mpl.figure()
ax = fig.add_subplot(111)

groupColors=['c','g','y','m','r','b']

t=np.arange(1, 17)

i=0
while i<6:
  ax.fill_between(t,groupDataBot[i], groupDataBot[i+1], facecolor=groupColors[i],linewidth=0)
  i+=1

mpl.grid()
mpl.xlim([1, 16])
#mpl.ylim([0, 1100])
mpl.xlabel('Number of MPI Ranks', fontweight='bold')
mpl.ylabel('Time (sec)', fontweight='bold')
mpl.title('OS Mesa llvmpipe Edison Single Node Performance\n n MPI Ranks+16 pthreads Surface LIC 54M Tri. 10k it.',fontweight='bold',fontsize='12')

#mpl.title('OS Mesa llvmpipe\nSingle Process Performance Edison')

groups=('Vertex Processing & Vector Projection',
'Composite & Guard Pixel Exch.',
'LIC Computation',
'Scalar Color Shading',
'Contrast Enhance',
'Fragment Depth Test')

mpl.legend((groupPlots[0],
  groupPlots[1],
  groupPlots[2],
  groupPlots[3],
  groupPlots[4],
  groupPlots[5]),
  groups,
  prop={'size': 9})
#  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

fig = mpl.gcf()
mpl.savefig('llvmpipe-edison-1node-nrank-16threads.png',dpi=200)
mpl.savefig('llvmpipe-edison-1node-nrank-16threads-sm.png',dpi=80)
mpl.show()
