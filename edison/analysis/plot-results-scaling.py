#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# mpl.rcParams['figure.dpi'] = 200

saveFig=1


khbce={}
khbce[104]=32.0425
khbce[112]=29.084
khbce[120]=24.6978
khbce[128]=23.3816
khbce[136]=22.3624
khbce[144]=21.828
khbce[152]=20.5891
khbce[16]=142.508
khbce[160]=20.0915
khbce[168]=19.393
khbce[176]=19.0902
khbce[184]=18.6358
khbce[192]=17.6634
khbce[200]=17.5205
khbce[208]=16.9095
khbce[216]=17.0898
khbce[224]=16.1555
khbce[232]=15.8404
khbce[24]=101.58
khbce[240]=15.5155
khbce[248]=15.6209
khbce[256]=15.2575
khbce[264]=15.013
khbce[272]=15.0491
khbce[280]=14.4357
khbce[288]=14.3077
khbce[296]=14.1104
khbce[304]=14.0267
khbce[312]=13.6409
khbce[32]=77.5273
khbce[320]=13.3818
khbce[328]=13.1987
khbce[336]=13.2481
khbce[344]=12.9401
khbce[352]=12.8308
khbce[360]=12.577
khbce[368]=12.4907
khbce[376]=12.5545
#khbce[384]=16.2933 # ol
khbce[392]=12.4084
khbce[40]=63.7893
khbce[400]=11.8275
khbce[408]=11.9687
#khbce[416]=16.6242 # ol
khbce[424]=11.7993
khbce[432]=11.5913
khbce[440]=11.8619
khbce[448]=11.6161
khbce[456]=11.3475
#khbce[464]=21.259 # ol
khbce[472]=11.1072
khbce[48]=52.0882
#khbce[480]=16.7846 # ol
khbce[488]=11.004
#khbce[496]=17.2037 # ol
khbce[504]=10.8229
#khbce[512]=15.5969 # ol
khbce[56]=45.5269
khbce[64]=40.7915
khbce[72]=40.2894
khbce[80]=43.988
khbce[88]=33.9316
khbce[96]=31.5573

khbce_x=[]
khbce_t=[]
for k in sorted(khbce.keys()):
  khbce_x.append(k)
  khbce_t.append(khbce[k])

khbwoce={}
khbwoce[104]=23.9536
khbwoce[112]=22.5901
khbwoce[120]=21.5761
khbwoce[128]=20.1839
khbwoce[136]=19.3654
khbwoce[144]=18.304
khbwoce[152]=18.5237
khbwoce[16]=132.856
khbwoce[160]=16.8672
khbwoce[168]=16.2951
khbwoce[176]=15.6196
khbwoce[184]=15.5737
khbwoce[192]=14.8956
khbwoce[200]=14.5757
khbwoce[208]=14.118
khbwoce[216]=13.8427
khbwoce[224]=13.4187
khbwoce[232]=13.1268
khbwoce[24]=93.6664
khbwoce[240]=12.5807
khbwoce[248]=13.2726
khbwoce[256]=12.9092
khbwoce[264]=12.5001
khbwoce[272]=12.568
khbwoce[280]=11.9332
khbwoce[288]=11.6927
khbwoce[296]=11.4394
khbwoce[304]=11.3296
khbwoce[312]=10.7708
khbwoce[32]=70.8443
khbwoce[320]=10.9758
khbwoce[328]=10.5572
khbwoce[336]=10.298
khbwoce[344]=10.03
khbwoce[352]=9.92598
khbwoce[360]=9.79607
khbwoce[368]=9.52872
khbwoce[376]=9.51143
khbwoce[384]=9.28227
khbwoce[392]=9.08993
khbwoce[40]=57.2777
khbwoce[400]=9.16393
khbwoce[408]=9.0231
khbwoce[416]=8.8343
khbwoce[424]=8.98501
khbwoce[432]=8.92409
khbwoce[440]=8.74231
khbwoce[448]=8.75937
khbwoce[456]=8.42519
khbwoce[464]=8.22121
khbwoce[472]=8.26899
khbwoce[48]=46.7728

khbwoce_x=[]
khbwoce_t=[]
for k in sorted(khbwoce.keys()):
  khbwoce_x.append(k)
  khbwoce_t.append(khbwoce[k])

khuece={}
khuece[104]=38.5025
khuece[112]=36.0805
khuece[120]=34.3148
khuece[128]=32.3343
khuece[136]=31.4684
khuece[144]=30.4467
khuece[152]=29.3235
khuece[16]=173.249
khuece[160]=28.3463
khuece[168]=28.6288
khuece[176]=26.484
khuece[184]=25.8904
khuece[192]=24.7343
khuece[200]=24.7252
khuece[208]=24.0082
khuece[216]=23.6696
khuece[224]=22.8833
khuece[232]=22.588
khuece[24]=126.868
khuece[240]=22.0613
khuece[248]=22.5252
khuece[256]=22.3153
khuece[264]=22.0021
khuece[272]=21.9122
khuece[280]=21.1887
khuece[288]=20.9771
khuece[296]=20.7026
khuece[304]=19.9607
khuece[312]=19.4785
khuece[32]=97.714
khuece[320]=19.7376
khuece[328]=18.9315
khuece[336]=18.9382
khuece[344]=18.6339
#khuece[352]=26.2274 # ol
khuece[360]=18.568
khuece[368]=18.1261
khuece[376]=17.7401
#khuece[384]=22.5635 # ol
khuece[392]=17.4838
khuece[40]=81.4806
khuece[400]=17.4053
khuece[408]=17.2163
#khuece[416]=24.634 # ol
khuece[424]=17.687
khuece[432]=17.0204
khuece[440]=16.6337
#khuece[448]=20.8148 # ol
khuece[456]=16.2872
#khuece[464]=22.4105 # ol
khuece[472]=16.0591
khuece[48]=77.632
#khuece[480]=21.1149 # ol
khuece[488]=15.8804
#khuece[496]=23.4219 # ol
khuece[504]=15.7731
#khuece[512]=20.1823 # ol
khuece[56]=60.1741
khuece[64]=53.8108
khuece[72]=53.2676
khuece[80]=48.6588
khuece[88]=46.0398
khuece[96]=42.8827

khuece_x=[]
khuece_t=[]
for k in sorted(khuece.keys()):
  khuece_x.append(k)
  khuece_t.append(khuece[k])

khuewoce={}
khuewoce[104]=25.1491
khuewoce[112]=22.8523
khuewoce[120]=21.6033
khuewoce[128]=19.9662
khuewoce[136]=19.0106
khuewoce[144]=18.3284
khuewoce[152]=17.4884
khuewoce[16]=133.701
khuewoce[160]=16.6077
khuewoce[168]=16.4521
khuewoce[176]=15.5318
khuewoce[184]=15.3465
khuewoce[192]=14.8237
khuewoce[200]=14.6031
khuewoce[208]=14.2602
khuewoce[216]=13.9309
khuewoce[224]=13.3887
khuewoce[232]=13.114
khuewoce[24]=95.5917
khuewoce[240]=12.6778
khuewoce[248]=13.0033
khuewoce[256]=12.6564
khuewoce[264]=12.6273
khuewoce[272]=12.2433
khuewoce[280]=11.6155
khuewoce[288]=11.6636
khuewoce[296]=11.6579
khuewoce[304]=11.04
khuewoce[312]=10.6836
khuewoce[32]=70.4328
khuewoce[320]=11.2269
khuewoce[328]=10.7072
khuewoce[336]=10.3749
khuewoce[344]=10.1602
khuewoce[352]=9.79956
khuewoce[360]=9.93226
khuewoce[368]=9.65149
khuewoce[376]=9.49496
khuewoce[384]=9.32749
khuewoce[392]=9.15468
khuewoce[40]=56.9969
khuewoce[400]=9.39902
khuewoce[408]=9.17476
khuewoce[416]=8.83211
khuewoce[424]=8.9648
khuewoce[432]=8.90424
khuewoce[440]=8.55696
khuewoce[448]=8.56203
khuewoce[456]=9.03888
khuewoce[464]=8.41087
khuewoce[472]=8.42082
khuewoce[48]=47.2458
khuewoce[480]=8.26238
khuewoce[488]=8.14242
khuewoce[496]=7.9741
khuewoce[504]=8.16156
khuewoce[512]=8.14701
khuewoce[56]=40.9981
khuewoce[64]=36.3277
khuewoce[72]=37.4166
khuewoce[80]=34.0683
khuewoce[88]=31.4238
khuewoce[96]=28.9472

khuewoce_x=[]
khuewoce_t=[]
for k in sorted(khuewoce.keys()):
  khuewoce_x.append(k)
  khuewoce_t.append(khuewoce[k])

# note:
# ue  - 2000 steps
# b - 1000 steps
# b/ue w/o - 800 steps
#def onpick2(event):
#  print('onpick2 line:', event.pickx, event.picky)
#
#fig = mpl.figure()
#fig.canvas.mpl_connect('pick_event', onpick2)
#
#mpl.plot(khbce_x, khbce_t, 'b-', linewidth=2, label='lic(B) w/CE')
#mpl.plot(khbwoce_x, khbwoce_t, 'g-', linewidth=2, label='lic(B)')
#mpl.plot(khuece_x, khuece_t, 'r-', linewidth=2, label='lic(Ue) w/CE')
#mpl.plot(khuewoce_x, khuewoce_t, 'c-', linewidth=2, label='lic(Ue)')
#
#mpl.xlim(16, 512)
#
#ticks=[32, 96, 160, 224, 288, 352, 416, 480]
#mpl.xticks(ticks)
#
#mpl.legend(prop={'size': 9})
#mpl.title('Surface LIC Scaling\n 8 Ranks per Node 4 threads',fontweight='bold')
#mpl.ylabel('seconds',fontweight='bold')
#mpl.xlabel('Number of MPI Ranks',fontweight='bold')
#mpl.grid()
#mpl.show()

mpl.loglog(khbce_x, khbce_t, 'g-', linewidth=2, label='B w/CE 2000 steps')
mpl.loglog(khuece_x, khuece_t, 'c-', linewidth=2, label='Ue w/CE 4000 steps')
mpl.loglog(khbwoce_x, khbwoce_t, 'r-', linewidth=2, label='B 1600 steps')
mpl.loglog(khuewoce_x, khuewoce_t, 'b-', linewidth=2, label='Ue 1600 steps')
mpl.title('Scaling 222 M Tri. Slice at 2500x1050 res.\nOS Mesa 8 Ranks per Node 4 threads',fontweight='bold')
mpl.ylabel('time (sec)',fontweight='bold')
mpl.xlabel('Number of MPI Ranks',fontweight='bold')
mpl.legend(prop={'size': 9})
mpl.grid(True,which='both')
mpl.grid(which='major',ls='-')
mpl.grid(which='minor',ls=':')
if saveFig:
  fig = mpl.gcf()
  mpl.savefig('scaling-ce-slice-mesa.png',dpi=200)
  mpl.savefig('scaling-ce-slice-mesa-sm.png',dpi=80)
else:
  mpl.show()


pripd={}
pripd[104]=6.80178
pripd[112]=6.71193
pripd[120]=6.78673
pripd[128]=6.54333
pripd[136]=6.59083
pripd[144]=6.22489
pripd[152]=5.97461
pripd[16]=16.9717
pripd[160]=5.76116
pripd[168]=5.76604
pripd[176]=5.59598
pripd[184]=5.57516
pripd[192]=5.98787
pripd[200]=5.74258
pripd[208]=5.61816
pripd[216]=5.678
pripd[224]=5.75246
pripd[232]=5.39838
pripd[24]=14.3177
pripd[240]=5.33441
pripd[248]=5.25786
pripd[256]=5.31479
pripd[264]=5.2702
pripd[272]=5.18137
pripd[280]=5.13818
pripd[288]=5.27303
pripd[296]=5.18375
pripd[304]=5.15316
pripd[312]=5.12089
pripd[32]=11.5151
pripd[320]=5.13908
pripd[328]=5.32752
pripd[336]=5.25351
pripd[344]=5.00962
# pripd[352]=14.335
pripd[360]=5.05639
pripd[368]=5.05
pripd[376]=4.85058
pripd[384]=5.08312
pripd[392]=4.8372
pripd[40]=10.7818
pripd[400]=5.05626
pripd[408]=4.88047
pripd[416]=4.87881
pripd[424]=4.81901
pripd[432]=4.89145
pripd[440]=4.79828
pripd[448]=4.75134
pripd[456]=4.66365
# pripd[464]=8.35888
pripd[472]=4.87717
pripd[48]=9.58444
pripd[480]=4.5743
pripd[488]=4.5605
#pripd[496]=9.73865 # ol
pripd[504]=4.7795
pripd[512]=4.69257
pripd[56]=8.71484
pripd[64]=8.34135
pripd[72]=8.15055
pripd[80]=7.50806
pripd[88]=7.11525
pripd[96]=6.87599

pripd_x=[]
pripd_t=[]
for k in sorted(pripd.keys()):
  pripd_x.append(k)
  pripd_t.append(pripd[k])

prip={}
prip[104]=8.53869
prip[112]=8.5428
prip[120]=8.51903
prip[128]=8.57604
prip[136]=7.73217
prip[144]=8.32623
prip[152]=8.34585
prip[16]=24.6196
prip[160]=7.69961
prip[168]=7.93408
prip[176]=7.37595
prip[184]=6.8086
prip[192]=7.04259
prip[200]=7.03536
prip[208]=6.9785
prip[216]=6.6776
prip[224]=6.91348
prip[232]=7.06622
prip[24]=20.0398
prip[240]=6.17461
prip[248]=6.1135
prip[256]=6.39992
prip[264]=6.20855
prip[272]=5.95947
prip[280]=6.53734
prip[288]=5.98882
prip[296]=5.82849
prip[304]=6.07203
prip[312]=6.09151
prip[32]=16.4377
prip[320]=5.69259
prip[328]=5.87208
prip[336]=5.98723
prip[344]=5.83367
prip[352]=5.50614
prip[360]=5.6009
prip[368]=5.70119
prip[376]=5.38846
prip[384]=5.35052
prip[392]=5.46811
prip[40]=14.9472
prip[400]=5.49201
prip[408]=5.45418
prip[416]=5.39674
prip[424]=5.45973
prip[432]=5.12994
prip[440]=5.01575
prip[448]=5.14443
prip[456]=5.04878
#prip[464]=9.16913 # ol
prip[472]=5.06233
prip[48]=12.6223
#prip[480]=8.84682 # ol
prip[488]=4.91487
prip[496]=4.98957
prip[504]=5.00703
prip[512]=5.11834
prip[56]=11.8381
prip[64]=11.5226
prip[72]=10.9887
prip[80]=10.3413
prip[88]=9.80519
prip[96]=9.76479

prip_x=[]
prip_t=[]
for k in sorted(prip.keys()):
  prip_x.append(k)
  prip_t.append(prip[k])

mpl.loglog(prip_x, prip_t, 'r-', linewidth=2, label='INPLACE')
mpl.loglog(pripd_x, pripd_t, 'b-', linewidth=2, label='INPLACE_DISJOINT')
mpl.title('Scaling of Compositing Methods\n1024^3 box at 1215x1090 res\nOS Mesa 8 Ranks per Node 4 threads',fontweight='bold')
mpl.ylabel('seconds',fontweight='bold')
mpl.xlabel('Number of MPI Ranks',fontweight='bold')
mpl.legend(prop={'size': 9})
mpl.grid(True,which='both')
mpl.grid(which='major',ls='-')
mpl.grid(which='minor',ls=':')
#mpl.grid()
mpl.subplots_adjust(top=0.85)
if saveFig:
  fig = mpl.gcf()
  mpl.savefig('scaling-composite-cube-mesa.png',dpi=200)
  mpl.savefig('scaling-composite-cube-mesa-sm.png',dpi=80)
else:
  mpl.show()






# gant
ip_ev=['RenderGeometry','GatherVectors','TransformVectors','Integrate1','ContrastEnhance1','EdgeEnahnce','Integrate2','ContrastEnhance2','ComputeLIC','ColorLIC','ContrastEnhanceC','DepthCopy','RenderInternal','DepthCopy','RenderInternal']
ip_r0=[9.08836,0.465344,0.068629,6.71203,2.76863,0.110974,3.3967,1.51991,14.6399,0.137254,0.11577,0.0745132,24.6196,0.000128031,0.00031209]
ip_r1=[4.84808,4.71319,0.062187,6.50192,2.98067,0.117237,3.25431,1.65574,14.6345,0.136736,0.116352,0.0744421,24.6223,0.000128031,0.000306129]
ip_r2=[4.81037,4.75223,0.072006,6.3854,3.08613,0.110721,3.26322,1.65336,14.6331,0.137899,0.115264,0.0746741,24.6226,0.000123978,0.00030303]
ip_r3=[9.08205,0.504243,0.062664,6.34711,3.10615,0.111166,3.25559,1.66094,14.6068,0.14214,0.112949,0.0727,24.6197,0.000117064,0.000247955]
ip_r4=[4.9113,4.64433,0.0695629,4.64194,4.83799,0.112513,2.33586,2.57972,14.6397,0.138181,0.115692,0.073324,24.622,0.000129938,0.000319958]
ip_r5=[9.10655,0.450602,0.063051,6.45127,3.03136,0.112294,3.26505,1.65072,14.6358,0.144375,0.108968,0.0739222,24.6191,0.000133038,0.000319958]
ip_r6=[4.93471,4.62362,0.0620642,5.07079,4.41419,0.112172,2.59273,2.32319,14.6371,0.138102,0.11547,0.0737221,24.6221,0.000126839,0.000319958]
ip_r7=[9.19545,0.357971,0.069155,5.06016,4.42013,0.112051,2.53252,2.38353,14.6397,0.14341,0.110058,0.0737841,24.6191,0.000123978,0.000319958]
ip_r8=[4.80664,4.77416,0.0665321,6.88151,2.57571,0.110443,3.46481,1.45307,14.614,0.137567,0.115987,0.0748472,24.6231,0.000137091,0.000326872]
ip_r9=[9.11398,0.461931,0.065474,8.08057,1.37995,0.110346,4.12393,0.794041,14.6165,0.146618,0.107118,0.074604,24.6201,0.000138044,0.000326872]
ip_r10=[4.8108,4.77449,0.0677981,7.23413,2.21728,0.110342,3.77404,1.14394,14.6095,0.137571,0.116698,0.074048,24.623,0.000132084,0.000325918]
ip_r11=[9.08462,0.491337,0.0630829,7.89621,1.56674,0.110828,3.94996,0.967544,14.6165,0.148154,0.105314,0.0747819,24.62,0.000134945,0.000326872]
ip_r12=[4.89312,4.6935,0.0646389,8.75496,0.698964,0.111126,4.5605,0.356732,14.6088,0.148071,0.105657,0.0744421,24.6229,0.000118017,0.000250816]
ip_r13=[9.10687,0.472364,0.061435,9.43484,0.027096,0.111291,4.91264,0.0044241,14.6137,0.144749,0.108864,0.074645,24.62,0.000136137,0.000298977]
ip_r14=[4.9234,4.66215,0.0643651,6.15351,3.30186,0.110852,3.15588,1.76162,14.6099,0.137698,0.116167,0.0743721,24.6229,0.000130892,0.000318766]
ip_r15=[9.12112,0.455557,0.067379,7.64393,1.81441,0.111309,3.81222,1.10483,14.6162,0.138743,0.114941,0.0746129,24.62,0.000130892,0.000317812]

groups=(ip_ev[0:8]+ip_ev[9:12])
ids=[0,1,2,3,4,5,6,7,9,10,11]
groupData=[[],[],[],[],[],[],[],[],[],[],[]]
groupColors=[[],[],[],[],[],[],[],[],[],[],[]]
i=0
while i<11:
  groupData[i]=[ip_r0[ids[i]],
      ip_r1[ids[i]],
      ip_r2[ids[i]],
      ip_r3[ids[i]],
      ip_r4[ids[i]],
      ip_r5[ids[i]],
      ip_r6[ids[i]],
      ip_r7[ids[i]],
      ip_r8[ids[i]],
      ip_r9[ids[i]],
      ip_r10[ids[i]],
      ip_r11[ids[i]],
      ip_r12[ids[i]],
      ip_r13[ids[i]],
      ip_r14[ids[i]],
      ip_r15[ids[i]]]
  #print groups[i]
  #print groupData[i]
  j=i/10.0 #j=1.0-i/10.0
  groupColors[i]=cm.Paired(j)
  groupColors[i]=cm.Dark2(j)
  #groupColors[i]=cm.Set1(j)
  #groupColors[i]=cm.Set3(j)
  i+=1

groupDataBot=[[],[],[],[],[],[],[],[],[],[],[],[]]
groupDataBot[0]=[0]*16
i=1
while i<11:
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

groupPlots=[[],[],[],[],[],[],[],[],[],[],[]]

ranks=np.arange(16)-0.5

mpl.subplot(121)
groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<11:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('INPLACE Compositing Activity by Rank\n1024^3 box at 1215x1090 res',fontweight='bold',fontsize='12')
mpl.xlabel('MPI Rank', fontweight='bold')
mpl.xlim([-0.75, 15.5])
#mpl.ylim([0, 140])
mpl.ylabel('time (sec)', fontweight='bold')
mpl.grid()

mpl.legend((groupPlots[0],
  groupPlots[1],
  groupPlots[2],
  groupPlots[3],
  groupPlots[4],
  groupPlots[5],
  groupPlots[6],
  groupPlots[7],
  groupPlots[8],
  groupPlots[9],
  groupPlots[10]),
  tuple(groups),
  prop={'size': 9},
  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

mpl.subplots_adjust(top=0.85)

if saveFig:
  fig = mpl.gcf()
  mpl.savefig('scaling-gant-inplace-composite-mesa.png',dpi=200)
  mpl.savefig('scaling-gant-inplace-composite-mesa-sm.png',dpi=80)
else:
  mpl.show()


ipd_ev=['RenderGeometry','GatherVectors','TransformVectors','Integrate1','ContrastEnhance1','EdgeEnahnce','Integrate2','ContrastEnhance2','ComputeLIC','ScatterLIC','ColorLIC','ContrastEnhanceC','DepthCopy','RenderInternal','DepthCopy','RenderInternal']
ipd_r0=[8.91797,0.601769,0.0635419,1.84561,2.53953,0.110742,0.777521,1.45316,6.85199,0.092078,0.14424,0.191144,0.0738831,16.9717,0.000136137,0.000329971]
ipd_r1=[4.92925,4.59431,0.066004,3.39835,0.982242,0.110909,1.70336,0.527464,6.84999,0.093472,0.14265,0.191585,0.073487,16.9743,0.000138998,0.000329018]
ipd_r2=[4.9315,4.59479,0.0716331,4.23472,0.137797,0.111129,2.11099,0.119599,6.84736,0.136953,0.144529,0.145461,0.0741901,16.9743,0.000121832,0.000329971]
ipd_r3=[8.91755,0.599465,0.067857,2.12174,2.26124,0.11107,1.01767,1.213,6.85438,0.107586,0.144537,0.178611,0.0739009,16.9748,0.000138998,0.000329971]
ipd_r4=[4.96553,4.53991,0.06198,4.23465,0.16693,0.112909,2.19732,0.0314591,6.86791,0.114938,0.141249,0.172966,0.072875,16.9752,0.000133991,0.000330925]
ipd_r5=[8.9644,0.426501,0.0612562,2.90849,1.60667,0.112794,1.36779,0.860972,6.98006,0.0695629,0.141662,0.217778,0.0732632,16.9724,0.000135899,0.000330925]
ipd_r6=[4.94552,4.5468,0.0640271,4.38753,0.024996,0.112293,2.22649,0.0028882,6.88087,0.115607,0.140987,0.172364,0.0732541,16.9753,0.000135899,0.000330925]
ipd_r7=[8.98532,0.445062,0.0597808,3.63182,0.845057,0.112853,1.89043,0.338373,6.94057,0.0918601,0.141561,0.195476,0.0737171,16.9728,0.000134945,0.000330925]
ipd_r8=[5.02773,4.48758,0.070585,2.93347,1.44953,0.110207,1.45454,0.777182,6.85785,0.109311,0.140168,0.176994,0.0746069,16.9742,0.000135183,0.000324011]
ipd_r9=[9.11802,0.403861,0.060643,2.44935,1.93393,0.110468,1.16535,1.06586,6.84889,0.117005,0.151465,0.157903,0.074636,16.9712,0.000136852,0.000324011]
ipd_r10=[4.96328,4.52834,0.063097,3.26931,1.14511,0.110412,1.65134,0.580301,6.88149,0.117031,0.146544,0.163713,0.0738938,16.9743,0.000135183,0.000324011]
ipd_r11=[9.06269,0.369109,0.058207,2.78207,1.69512,0.110433,1.34769,0.883708,6.93886,0.095118,0.143659,0.188253,0.073993,16.9712,0.00013423,0.000324011]
ipd_r12=[4.93606,4.55674,0.0215681,0.00266409,4.42866,9.05991e-06,0.00130582,2.36289,6.88088,0.125333,0.190043,0.108656,0.0759511,16.9731,0.000141859,0.000322104]
ipd_r13=[9.02472,0.478832,0.0211291,0.00258207,4.41611,7.86781e-06,0.00127697,2.36292,6.8677,0.132735,0.18958,0.101828,0.0758371,16.9701,0.000131845,0.000323057]
ipd_r14=[4.99745,4.46018,0.0628791,2.88413,1.56506,0.10922,1.31797,0.915068,6.91612,0.12137,0.143487,0.163317,0.074518,16.9758,0.000130892,0.000324965]
ipd_r15=[9.01455,0.411515,0.0599511,2.84884,1.63286,0.108853,1.45859,0.774578,6.94522,0.104593,0.142938,0.179888,0.07476,16.9723,0.000124931,0.000323057]


groups=(ipd_ev[0:8]+ipd_ev[9:13])
ids=[0,1,2,3,4,5,6,7,9,10,11,12]
groupData=[[],[],[],[],[],[],[],[],[],[],[],[]]
groupColors=[[],[],[],[],[],[],[],[],[],[],[],[]]
i=0
while i<12:
  groupData[i]=[ipd_r0[ids[i]],
      ipd_r1[ids[i]],
      ipd_r2[ids[i]],
      ipd_r3[ids[i]],
      ipd_r4[ids[i]],
      ipd_r5[ids[i]],
      ipd_r6[ids[i]],
      ipd_r7[ids[i]],
      ipd_r8[ids[i]],
      ipd_r9[ids[i]],
      ipd_r10[ids[i]],
      ipd_r11[ids[i]],
      ipd_r12[ids[i]],
      ipd_r13[ids[i]],
      ipd_r14[ids[i]],
      ipd_r15[ids[i]]]
  #print groups[i]
  #print groupData[i]
  j=i/11.0 #j=1.0-i/10.0
  groupColors[i]=cm.Paired(j)
  groupColors[i]=cm.Dark2(j)
  #groupColors[i]=cm.Set1(j)
  #groupColors[i]=cm.Set3(j)
  i+=1

groupDataBot=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
groupDataBot[0]=[0]*16
i=1
while i<12:
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

groupPlots=[[],[],[],[],[],[],[],[],[],[],[],[]]

ranks=np.arange(16)-0.5

mpl.subplot(121)
groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<12:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('INPLACE_DISJOINT Compositing Activity by Rank\n1024^3 box at 1215x1090 res',fontweight='bold',fontsize='12')
mpl.xlabel('MPI Rank', fontweight='bold')
mpl.xlim([-0.75, 15.5])
mpl.ylabel('time (sec)', fontweight='bold')
mpl.grid()

mpl.legend((groupPlots[0],
  groupPlots[1],
  groupPlots[2],
  groupPlots[3],
  groupPlots[4],
  groupPlots[5],
  groupPlots[6],
  groupPlots[7],
  groupPlots[8],
  groupPlots[9],
  groupPlots[10],
  groupPlots[11]),
  tuple(groups),
  prop={'size': 9},
  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

mpl.subplots_adjust(top=0.85)

if saveFig:
  fig = mpl.gcf()
  mpl.savefig('scaling-gant-inplace-disjoint-composite.png',dpi=200)
  mpl.savefig('scaling-gant-inplace-disjoint-composite-sm.png',dpi=80)
else:
  mpl.show()
