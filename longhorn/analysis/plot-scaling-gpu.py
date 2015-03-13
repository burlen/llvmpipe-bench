#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter

saveFig = 0
plotOutlier = 0

khbce_gpu={}
#khbce_gpu[160]=
khbce_gpu[104]=13.0597
khbce_gpu[112]=13.0875
khbce_gpu[120]=12.1235
khbce_gpu[128]=12.2268
khbce_gpu[136]=11.9705
khbce_gpu[144]=11.644
khbce_gpu[152]=11.5232
khbce_gpu[16]=69.9943
khbce_gpu[168]=11.0973
khbce_gpu[184]=11.3364
khbce_gpu[200]=10.4847
khbce_gpu[208]=10.3717
khbce_gpu[216]=10.5024
khbce_gpu[24]=34.4396
khbce_gpu[240]=10.3564
khbce_gpu[248]=10.2475
khbce_gpu[256]=10.1053
khbce_gpu[264]=11.0897
khbce_gpu[280]=11.1324
khbce_gpu[288]=11.0831
khbce_gpu[296]=10.0639
khbce_gpu[312]=9.66767
khbce_gpu[32]=27.9898
khbce_gpu[328]=9.98905
khbce_gpu[352]=11.0573
khbce_gpu[360]=10.9711
khbce_gpu[368]=9.59873
khbce_gpu[376]=9.5939
khbce_gpu[392]=10.7879
khbce_gpu[40]=25.3224
khbce_gpu[400]=9.47
khbce_gpu[408]=10.7271
khbce_gpu[416]=9.73353
khbce_gpu[432]=10.7228
khbce_gpu[440]=10.784
khbce_gpu[448]=10.4342
khbce_gpu[464]=10.7521
khbce_gpu[472]=10.3952
khbce_gpu[48]=23.0079
khbce_gpu[480]=10.706
khbce_gpu[488]=10.2838
khbce_gpu[496]=10.6667
khbce_gpu[504]=9.18155
khbce_gpu[512]=9.31821
khbce_gpu[56]=22.7969
khbce_gpu[64]=23.4879
khbce_gpu[72]=21.5675
khbce_gpu[8]=171.675
khbce_gpu[80]=21.3605
khbce_gpu[88]=19.074
khbce_gpu[96]=13.4728
if plotOutlier:
  khbce_gpu[176]=12.9135 # ol
  khbce_gpu[192]=13.8763 # ol
  khbce_gpu[224]=12.1429 # ol
  khbce_gpu[232]=11.994 # ol
  khbce_gpu[272]=13.0234 # ol
  khbce_gpu[304]=13.1753 # ol
  khbce_gpu[320]=13.669 # ol
  khbce_gpu[336]=12.5709 # ol
  khbce_gpu[344]=12.662 # ol
  khbce_gpu[384]=14.0504 # ol
  khbce_gpu[424]=11.9493 # ol
  khbce_gpu[456]=11.4108 # ol

khbce_gpu_x=[]
khbce_gpu_t=[]
for k in sorted(khbce_gpu.keys()):
  khbce_gpu_x.append(k)
  khbce_gpu_t.append(khbce_gpu[k])

# fit a curve in log space
x = np.log(np.array(khbce_gpu_x))
t = np.log(np.array(khbce_gpu_t))
khbce_gpu_cc = np.polyfit(x,t,2)
khbce_gpu_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
khbce_gpu_tt = np.exp(khbce_gpu_cc[0]*(khbce_gpu_xx**2) + khbce_gpu_cc[1]*khbce_gpu_xx + khbce_gpu_cc[2])




khbce_mesa={}
khbce_mesa[104]=32.0425
khbce_mesa[112]=29.084
khbce_mesa[120]=24.6978
khbce_mesa[128]=23.3816
khbce_mesa[136]=22.3624
khbce_mesa[144]=21.828
khbce_mesa[152]=20.5891
khbce_mesa[16]=142.508
khbce_mesa[160]=20.0915
khbce_mesa[168]=19.393
khbce_mesa[176]=19.0902
khbce_mesa[184]=18.6358
khbce_mesa[192]=17.6634
khbce_mesa[200]=17.5205
khbce_mesa[208]=16.9095
khbce_mesa[216]=17.0898
khbce_mesa[224]=16.1555
khbce_mesa[232]=15.8404
khbce_mesa[24]=101.58
khbce_mesa[240]=15.5155
khbce_mesa[248]=15.6209
khbce_mesa[256]=15.2575
khbce_mesa[264]=15.013
khbce_mesa[272]=15.0491
khbce_mesa[280]=14.4357
khbce_mesa[288]=14.3077
khbce_mesa[296]=14.1104
khbce_mesa[304]=14.0267
khbce_mesa[312]=13.6409
khbce_mesa[32]=77.5273
khbce_mesa[320]=13.3818
khbce_mesa[328]=13.1987
khbce_mesa[336]=13.2481
khbce_mesa[344]=12.9401
khbce_mesa[352]=12.8308
khbce_mesa[360]=12.577
khbce_mesa[368]=12.4907
khbce_mesa[376]=12.5545
#khbce_mesa[384]=16.2933 # ol
khbce_mesa[392]=12.4084
khbce_mesa[40]=63.7893
khbce_mesa[400]=11.8275
khbce_mesa[408]=11.9687
#khbce_mesa[416]=16.6242 # ol
khbce_mesa[424]=11.7993
khbce_mesa[432]=11.5913
khbce_mesa[440]=11.8619
khbce_mesa[448]=11.6161
khbce_mesa[456]=11.3475
#khbce_mesa[464]=21.259 # ol
khbce_mesa[472]=11.1072
khbce_mesa[48]=52.0882
#khbce_mesa[480]=16.7846 # ol
khbce_mesa[488]=11.004
#khbce_mesa[496]=17.2037 # ol
khbce_mesa[504]=10.8229
#khbce_mesa[512]=15.5969 # ol
khbce_mesa[56]=45.5269
khbce_mesa[64]=40.7915
khbce_mesa[72]=40.2894
khbce_mesa[80]=43.988
khbce_mesa[88]=33.9316
khbce_mesa[96]=31.5573

khbce_mesa_x=[]
khbce_mesa_t=[]
for k in sorted(khbce_mesa.keys()):
  khbce_mesa_x.append(k)
  khbce_mesa_t.append(khbce_mesa[k])

# fit a curve in log space
x = np.log(np.array(khbce_mesa_x))
t = np.log(np.array(khbce_mesa_t))
khbce_mesa_cc = np.polyfit(x,t,2)
khbce_mesa_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
khbce_mesa_tt = np.exp(khbce_mesa_cc[0]*(khbce_mesa_xx**2) + khbce_mesa_cc[1]*khbce_mesa_xx + khbce_mesa_cc[2])

# avg speedup when using gpu
khbce_gpu_tt_ = np.exp(khbce_gpu_cc[0]*(khbce_mesa_xx**2) + khbce_gpu_cc[1]*khbce_mesa_xx + khbce_gpu_cc[2])
q = (khbce_mesa_tt - khbce_gpu_tt_)/khbce_mesa_tt
khbce_gpu_su = np.sum(q)/len(khbce_mesa_xx)
print 'khbce_gpu_su = %f, %f, %f'%(np.min(q), khbce_gpu_su, np.max(q))

khuece_gpu={}
khuece_gpu[104]=15.2368
khuece_gpu[112]=14.768
khuece_gpu[120]=13.8621
khuece_gpu[128]=14.4154
#khuece_gpu[136]=23.3288 # ol
#khuece_gpu[144]=22.6664 # ol
khuece_gpu[152]=12.7043
khuece_gpu[16]=101.244
#khuece_gpu[160]=
khuece_gpu[168]=12.4141
khuece_gpu[176]=12.6448
khuece_gpu[184]=12.1015
#khuece_gpu[192]=22.2965 # ol
khuece_gpu[200]=11.6956
#khuece_gpu[208]=
#khuece_gpu[216]=18.7714 # ol
khuece_gpu[224]=12.8309
khuece_gpu[232]=10.5883
khuece_gpu[24]=44.9088
khuece_gpu[240]=11.4853
khuece_gpu[248]=11.5913
#khuece_gpu[256]=17.8126 # ol
#khuece_gpu[264]=21.6831 # ol
khuece_gpu[272]=12.0543
khuece_gpu[280]=11.4412
#khuece_gpu[288]=17.5068 # ol
#khuece_gpu[296]=19.2472 # ol
khuece_gpu[304]=10.6378
khuece_gpu[312]=11.1913
khuece_gpu[32]=34.2061
khuece_gpu[320]=11.5221
khuece_gpu[328]=11.7003
khuece_gpu[336]=10.5185
khuece_gpu[344]=10.8903
khuece_gpu[352]=11.2541
#khuece_gpu[360]=17.1015 # ol
khuece_gpu[368]=10.9194
#khuece_gpu[376]=17.1986 # ol
khuece_gpu[384]=11.1504
khuece_gpu[392]=11.2105
khuece_gpu[40]=31.6938
#khuece_gpu[400]=19.2329 # ol
#khuece_gpu[408]=17.9332 # ol
khuece_gpu[416]=11.2578
khuece_gpu[424]=11.1196
#khuece_gpu[432]=18.6527 # ol
khuece_gpu[440]=9.73587
khuece_gpu[448]=11.8128
#khuece_gpu[456]=18.2636 # ol
khuece_gpu[464]=11.3711
khuece_gpu[472]=10.9745
khuece_gpu[48]=31.054
#khuece_gpu[480]=14.5783 # ol
khuece_gpu[488]=11.0974
khuece_gpu[496]=10.7072
khuece_gpu[504]=10.7632
khuece_gpu[512]=10.0102
khuece_gpu[56]=22.7209
khuece_gpu[64]=23.0317
#khuece_gpu[72]=
khuece_gpu[8]=172.097
khuece_gpu[80]=16.6123
khuece_gpu[88]=16.4512
khuece_gpu[96]=16.2593

khuece_gpu_x=[]
khuece_gpu_t=[]
for k in sorted(khuece_gpu.keys()):
  khuece_gpu_x.append(k)
  khuece_gpu_t.append(khuece_gpu[k])

# fit a curve in log space
x = np.log(np.array(khuece_gpu_x))
t = np.log(np.array(khuece_gpu_t))
khuece_gpu_cc = np.polyfit(x,t,2)
khuece_gpu_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
khuece_gpu_tt = np.exp(khuece_gpu_cc[0]*(khuece_gpu_xx**2) + khuece_gpu_cc[1]*khuece_gpu_xx + khuece_gpu_cc[2])

khuece_mesa={}
khuece_mesa[104]=38.5025
khuece_mesa[112]=36.0805
khuece_mesa[120]=34.3148
khuece_mesa[128]=32.3343
khuece_mesa[136]=31.4684
khuece_mesa[144]=30.4467
khuece_mesa[152]=29.3235
khuece_mesa[16]=173.249
khuece_mesa[160]=28.3463
khuece_mesa[168]=28.6288
khuece_mesa[176]=26.484
khuece_mesa[184]=25.8904
khuece_mesa[192]=24.7343
khuece_mesa[200]=24.7252
khuece_mesa[208]=24.0082
khuece_mesa[216]=23.6696
khuece_mesa[224]=22.8833
khuece_mesa[232]=22.588
khuece_mesa[24]=126.868
khuece_mesa[240]=22.0613
khuece_mesa[248]=22.5252
khuece_mesa[256]=22.3153
khuece_mesa[264]=22.0021
khuece_mesa[272]=21.9122
khuece_mesa[280]=21.1887
khuece_mesa[288]=20.9771
khuece_mesa[296]=20.7026
khuece_mesa[304]=19.9607
khuece_mesa[312]=19.4785
khuece_mesa[32]=97.714
khuece_mesa[320]=19.7376
khuece_mesa[328]=18.9315
khuece_mesa[336]=18.9382
khuece_mesa[344]=18.6339
#khuece_mesa[352]=26.2274 # ol
khuece_mesa[360]=18.568
khuece_mesa[368]=18.1261
khuece_mesa[376]=17.7401
#khuece_mesa[384]=22.5635 # ol
khuece_mesa[392]=17.4838
khuece_mesa[40]=81.4806
khuece_mesa[400]=17.4053
khuece_mesa[408]=17.2163
#khuece_mesa[416]=24.634 # ol
khuece_mesa[424]=17.687
khuece_mesa[432]=17.0204
khuece_mesa[440]=16.6337
#khuece_mesa[448]=20.8148 # ol
khuece_mesa[456]=16.2872
#khuece_mesa[464]=22.4105 # ol
khuece_mesa[472]=16.0591
khuece_mesa[48]=77.632
#khuece_mesa[480]=21.1149 # ol
khuece_mesa[488]=15.8804
#khuece_mesa[496]=23.4219 # ol
khuece_mesa[504]=15.7731
#khuece_mesa[512]=20.1823 # ol
khuece_mesa[56]=60.1741
khuece_mesa[64]=53.8108
khuece_mesa[72]=53.2676
khuece_mesa[80]=48.6588
khuece_mesa[88]=46.0398
khuece_mesa[96]=42.8827

khuece_mesa_x=[]
khuece_mesa_t=[]
for k in sorted(khuece_mesa.keys()):
  khuece_mesa_x.append(k)
  khuece_mesa_t.append(khuece_mesa[k])

# fit a curve in log space
x = np.log(np.array(khuece_mesa_x))
t = np.log(np.array(khuece_mesa_t))
khuece_mesa_cc = np.polyfit(x,t,2)
khuece_mesa_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
khuece_mesa_tt = np.exp(khuece_mesa_cc[0]*(khuece_mesa_xx**2) + khuece_mesa_cc[1]*khuece_mesa_xx + khuece_mesa_cc[2])

f = mpl.figure()
ax = f.add_subplot(121)
mpl.loglog(np.exp(khbce_mesa_xx), khbce_mesa_tt, 'b-', linewidth=2, label='CPU in-place')
mpl.loglog(np.exp(khbce_gpu_xx), khbce_gpu_tt, 'r-', linewidth=2, label='GPU in-place')
#mpl.loglog(np.exp(khuece_gpu_xx), khuece_gpu_tt, 'g-', linewidth=2, label='NV Quadro 5800 UeCE4k')
#mpl.loglog(np.exp(khuece_mesa_xx), khuece_mesa_tt, 'c-', linewidth=2, label='Gallium llvmpipe UeCE4k')
mpl.legend(prop={'size': 10, 'weight':'bold'})
mpl.loglog(khbce_mesa_x, khbce_mesa_t, 'b+', linewidth=2, label='CPU in-place')
mpl.loglog(khbce_gpu_x, khbce_gpu_t, 'r+', linewidth=2, label='GPU in-place')
#mpl.loglog(khuece_gpu_x, khuece_gpu_t, 'g+', linewidth=2, label='NV Quadro 5800 UeCE4k')
#mpl.loglog(khuece_mesa_x, khuece_mesa_t, 'c+', linewidth=2, label='Gallium llvmpipe UeCE4k')
mpl.title('In-place Decomp. 2D 222 M\nTri. Slice at 2500x1050 res.',fontweight='bold', fontsize=14)
mpl.ylabel('render time (seconds)',fontweight='bold', fontsize=12)
mpl.xlabel('Number of MPI Ranks',fontweight='bold', fontsize=12)
mpl.grid(True,which='both')
mpl.grid(which='major',ls='-')
mpl.grid(which='minor',ls=':')
mpl.xlim([7, 600])
mpl.ylim([8, 200])
mpl.setp(mpl.getp(ax, 'xticklabels'), fontsize=10, weight='bold')
mpl.setp(mpl.getp(ax, 'yticklabels'), fontsize=10, weight='bold')
def tl(x, p):
    return "%d"%(x)
for axis in [ax.get_xaxis(), ax.get_yaxis()]:
  axis.set_major_formatter(FuncFormatter(tl))
#bbox_props = dict(boxstyle='round,pad=0.3', fc='w', ec='b', lw=2)
#t = ax.text(30, 90, 'CPU', bbox=bbox_props, fontweight='bold', color='b')
#if saveFig:
#  fig = mpl.gcf()
#  mpl.savefig('scaling-ce-slice-gpu.png',dpi=200)
#  mpl.savefig('scaling-ce-slice-gpu-sm.png',dpi=80)
#else:
#  mpl.show()




# compositor scaling
pripd_mesa={}
pripd_mesa[104]=6.80178
pripd_mesa[112]=6.71193
pripd_mesa[120]=6.78673
pripd_mesa[128]=6.54333
pripd_mesa[136]=6.59083
pripd_mesa[144]=6.22489
pripd_mesa[152]=5.97461
pripd_mesa[16]=16.9717
pripd_mesa[160]=5.76116
pripd_mesa[168]=5.76604
pripd_mesa[176]=5.59598
pripd_mesa[184]=5.57516
pripd_mesa[192]=5.98787
pripd_mesa[200]=5.74258
pripd_mesa[208]=5.61816
pripd_mesa[216]=5.678
pripd_mesa[224]=5.75246
pripd_mesa[232]=5.39838
pripd_mesa[24]=14.3177
pripd_mesa[240]=5.33441
pripd_mesa[248]=5.25786
pripd_mesa[256]=5.31479
pripd_mesa[264]=5.2702
pripd_mesa[272]=5.18137
pripd_mesa[280]=5.13818
pripd_mesa[288]=5.27303
pripd_mesa[296]=5.18375
pripd_mesa[304]=5.15316
pripd_mesa[312]=5.12089
pripd_mesa[32]=11.5151
pripd_mesa[320]=5.13908
pripd_mesa[328]=5.32752
pripd_mesa[336]=5.25351
pripd_mesa[344]=5.00962
# pripd_mesa[352]=14.335
pripd_mesa[360]=5.05639
pripd_mesa[368]=5.05
pripd_mesa[376]=4.85058
pripd_mesa[384]=5.08312
pripd_mesa[392]=4.8372
pripd_mesa[40]=10.7818
pripd_mesa[400]=5.05626
pripd_mesa[408]=4.88047
pripd_mesa[416]=4.87881
pripd_mesa[424]=4.81901
pripd_mesa[432]=4.89145
pripd_mesa[440]=4.79828
pripd_mesa[448]=4.75134
pripd_mesa[456]=4.66365
# pripd_mesa[464]=8.35888
pripd_mesa[472]=4.87717
pripd_mesa[48]=9.58444
pripd_mesa[480]=4.5743
pripd_mesa[488]=4.5605
#pripd_mesa[496]=9.73865 # ol
pripd_mesa[504]=4.7795
pripd_mesa[512]=4.69257
pripd_mesa[56]=8.71484
pripd_mesa[64]=8.34135
pripd_mesa[72]=8.15055
pripd_mesa[80]=7.50806
pripd_mesa[88]=7.11525
pripd_mesa[96]=6.87599

pripd_mesa_x=[]
pripd_mesa_t=[]
for k in sorted(pripd_mesa.keys()):
  pripd_mesa_x.append(k)
  pripd_mesa_t.append(pripd_mesa[k])

# fit a curve in log space
x = np.log(np.array(pripd_mesa_x))
t = np.log(np.array(pripd_mesa_t))
pripd_mesa_cc = np.polyfit(x,t,2)
pripd_mesa_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
pripd_mesa_tt = np.exp(pripd_mesa_cc[0]*(pripd_mesa_xx**2) + pripd_mesa_cc[1]*pripd_mesa_xx + pripd_mesa_cc[2])

pripd_gpu={}
pripd_gpu[104]=2.44978
pripd_gpu[112]=2.55201
pripd_gpu[120]=2.49491
pripd_gpu[128]=2.70841
pripd_gpu[136]=2.37411
pripd_gpu[144]=2.73817
pripd_gpu[152]=2.37018
pripd_gpu[16]=5.86841
pripd_gpu[160]=2.23043
pripd_gpu[168]=2.24287
pripd_gpu[176]=2.22236
pripd_gpu[184]=2.24579
pripd_gpu[192]=2.26419
pripd_gpu[200]=2.1272
pripd_gpu[208]=2.8394
pripd_gpu[216]=2.74038
pripd_gpu[224]=2.21143
pripd_gpu[232]=2.16795
pripd_gpu[24]=3.8455
pripd_gpu[240]=2.75865
pripd_gpu[248]=2.35237
pripd_gpu[256]=2.30513
pripd_gpu[264]=2.26431
pripd_gpu[272]=2.27814
pripd_gpu[280]=2.4057
pripd_gpu[288]=2.26489
pripd_gpu[296]=2.65033
pripd_gpu[304]=2.28685
pripd_gpu[312]=2.50415
pripd_gpu[32]=3.66871
pripd_gpu[320]=2.40469
#pripd_gpu[328]=3.34952 # ol
#pripd_gpu[336]=4.44124 # ol
pripd_gpu[344]=2.35319
pripd_gpu[352]=2.39121
pripd_gpu[360]=2.38619
pripd_gpu[368]=2.80048
pripd_gpu[376]=2.20264
pripd_gpu[384]=2.30668
pripd_gpu[392]=2.29023
pripd_gpu[40]=3.55046
pripd_gpu[400]=2.75921
pripd_gpu[408]=2.35207
pripd_gpu[416]=2.54002
pripd_gpu[424]=2.32874
pripd_gpu[432]=2.36128
#pripd_gpu[440]=3.61388 # ol
pripd_gpu[448]=2.47441
pripd_gpu[456]=2.59897
pripd_gpu[464]=2.36541
pripd_gpu[472]=2.60754
pripd_gpu[48]=3.34681
pripd_gpu[480]=2.25191
pripd_gpu[488]=2.44475
pripd_gpu[496]=2.34083
pripd_gpu[504]=2.28166
pripd_gpu[512]=2.26758
pripd_gpu[56]=3.22402
pripd_gpu[64]=2.60726
pripd_gpu[72]=2.68853
pripd_gpu[8]=7.08978
pripd_gpu[80]=2.39384
pripd_gpu[88]=2.5065
pripd_gpu[96]=2.90604

pripd_gpu_x=[]
pripd_gpu_t=[]
for k in sorted(pripd_gpu.keys()):
  pripd_gpu_x.append(k)
  pripd_gpu_t.append(pripd_gpu[k])

# fit a curve in log space
x = np.log(np.array(pripd_gpu_x))
t = np.log(np.array(pripd_gpu_t))
pripd_gpu_cc = np.polyfit(x,t,2)
pripd_gpu_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
pripd_gpu_tt = np.exp(pripd_gpu_cc[0]*(pripd_gpu_xx**2) + pripd_gpu_cc[1]*pripd_gpu_xx + pripd_gpu_cc[2])

# avg speedup when using gpu
pripd_gpu_tt_ = np.exp(pripd_gpu_cc[0]*(pripd_mesa_xx**2) + pripd_gpu_cc[1]*pripd_mesa_xx + pripd_gpu_cc[2])
q = (pripd_mesa_tt - pripd_gpu_tt_)/pripd_mesa_tt
pripd_gpu_su = np.sum(q)/len(pripd_mesa_xx)
print 'pripd_gpu_su = %f, %f, %f'%(np.min(q), pripd_gpu_su, np.max(q))




prip_mesa={}
prip_mesa[104]=8.53869
prip_mesa[112]=8.5428
prip_mesa[120]=8.51903
prip_mesa[128]=8.57604
prip_mesa[136]=7.73217
prip_mesa[144]=8.32623
prip_mesa[152]=8.34585
prip_mesa[16]=24.6196
prip_mesa[160]=7.69961
prip_mesa[168]=7.93408
prip_mesa[176]=7.37595
prip_mesa[184]=6.8086
prip_mesa[192]=7.04259
prip_mesa[200]=7.03536
prip_mesa[208]=6.9785
prip_mesa[216]=6.6776
prip_mesa[224]=6.91348
prip_mesa[232]=7.06622
prip_mesa[24]=20.0398
prip_mesa[240]=6.17461
prip_mesa[248]=6.1135
prip_mesa[256]=6.39992
prip_mesa[264]=6.20855
prip_mesa[272]=5.95947
prip_mesa[280]=6.53734
prip_mesa[288]=5.98882
prip_mesa[296]=5.82849
prip_mesa[304]=6.07203
prip_mesa[312]=6.09151
prip_mesa[32]=16.4377
prip_mesa[320]=5.69259
prip_mesa[328]=5.87208
prip_mesa[336]=5.98723
prip_mesa[344]=5.83367
prip_mesa[352]=5.50614
prip_mesa[360]=5.6009
prip_mesa[368]=5.70119
prip_mesa[376]=5.38846
prip_mesa[384]=5.35052
prip_mesa[392]=5.46811
prip_mesa[40]=14.9472
prip_mesa[400]=5.49201
prip_mesa[408]=5.45418
prip_mesa[416]=5.39674
prip_mesa[424]=5.45973
prip_mesa[432]=5.12994
prip_mesa[440]=5.01575
prip_mesa[448]=5.14443
prip_mesa[456]=5.04878
#prip_mesa[464]=9.16913 # ol
prip_mesa[472]=5.06233
prip_mesa[48]=12.6223
#prip_mesa[480]=8.84682 # ol
prip_mesa[488]=4.91487
prip_mesa[496]=4.98957
prip_mesa[504]=5.00703
prip_mesa[512]=5.11834
prip_mesa[56]=11.8381
prip_mesa[64]=11.5226
prip_mesa[72]=10.9887
prip_mesa[80]=10.3413
prip_mesa[88]=9.80519
prip_mesa[96]=9.76479

prip_mesa_x=[]
prip_mesa_t=[]
for k in sorted(prip_mesa.keys()):
  prip_mesa_x.append(k)
  prip_mesa_t.append(prip_mesa[k])

# fit a curve in log space
x = np.log(np.array(prip_mesa_x))
t = np.log(np.array(prip_mesa_t))
prip_mesa_cc = np.polyfit(x,t,2)
prip_mesa_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
prip_mesa_tt = np.exp(prip_mesa_cc[0]*(prip_mesa_xx**2) + prip_mesa_cc[1]*prip_mesa_xx + prip_mesa_cc[2])

prip_gpu={}
prip_gpu[104]=2.85369
prip_gpu[112]=2.52217
prip_gpu[120]=2.6456
prip_gpu[128]=2.88024
prip_gpu[136]=2.53215
prip_gpu[144]=2.68919
prip_gpu[152]=2.20217
prip_gpu[16]=6.64048
prip_gpu[160]=2.3099
prip_gpu[168]=2.56309
prip_gpu[176]=2.4113
prip_gpu[184]=2.37542
prip_gpu[192]=2.37466
#prip_gpu[200]=3.39242 # ol
prip_gpu[208]=2.56754
prip_gpu[216]=2.46089
prip_gpu[224]=2.70724
prip_gpu[232]=2.30437
prip_gpu[24]=5.49536
prip_gpu[240]=2.26742
prip_gpu[248]=2.24417
prip_gpu[256]=2.27731
prip_gpu[264]=2.27421
prip_gpu[272]=2.4054
prip_gpu[280]=2.3738
prip_gpu[288]=2.18982
prip_gpu[296]=2.41289
#prip_gpu[304]=5.38403 # ol
prip_gpu[312]=2.38373
prip_gpu[32]=5.00574
prip_gpu[320]=2.64816
prip_gpu[328]=2.22359
prip_gpu[336]=2.36969
prip_gpu[344]=2.15101
prip_gpu[352]=2.21387
prip_gpu[360]=2.17868
prip_gpu[368]=1.9952
prip_gpu[376]=2.39524
prip_gpu[384]=2.21731
prip_gpu[392]=2.32928
prip_gpu[40]=4.59342
prip_gpu[400]=2.21655
prip_gpu[408]=2.06169
#prip_gpu[416]=2.88972 # ol
prip_gpu[424]=2.10838
prip_gpu[432]=2.06019
prip_gpu[440]=2.19659
prip_gpu[448]=2.42652
prip_gpu[456]=2.15152
prip_gpu[464]=2.04871
prip_gpu[472]=1.9479
prip_gpu[48]=3.82203
prip_gpu[480]=2.05333
prip_gpu[488]=2.23285
prip_gpu[496]=2.18258
prip_gpu[504]=2.1447
prip_gpu[512]=2.24504
prip_gpu[56]=3.73106
prip_gpu[64]=3.46051
prip_gpu[72]=3.57933
prip_gpu[8]=8.84287
prip_gpu[80]=3.11802
prip_gpu[88]=2.8592
prip_gpu[96]=2.92048

prip_gpu_x=[]
prip_gpu_t=[]
for k in sorted(prip_gpu.keys()):
  prip_gpu_x.append(k)
  prip_gpu_t.append(prip_gpu[k])

# fit a curve in log space
x = np.log(np.array(prip_gpu_x))
t = np.log(np.array(prip_gpu_t))
prip_gpu_cc = np.polyfit(x,t,2)
prip_gpu_xx = np.arange(np.min(x), np.max(x)+0.1, 0.1)
prip_gpu_tt = np.exp(prip_gpu_cc[0]*(prip_gpu_xx**2) + prip_gpu_cc[1]*prip_gpu_xx + prip_gpu_cc[2])

# avg speedup when using gpu
prip_gpu_tt_ = np.exp(prip_gpu_cc[0]*(prip_mesa_xx**2) + prip_gpu_cc[1]*prip_mesa_xx + prip_gpu_cc[2])
q = (prip_mesa_tt - prip_gpu_tt_)/prip_mesa_tt
prip_gpu_su = np.sum(q)/len(prip_mesa_xx)
print 'prip_gpu_su = %f, %f, %f'%(np.min(q), prip_gpu_su, np.max(q))

# avg speed up from ipd gpu
q = (prip_gpu_tt - pripd_gpu_tt)/prip_gpu_tt
prip_ipd_su_gpu = np.sum(q)/len(prip_gpu_tt)
print 'prip_ipd_su_gpu = %f, %f, %f'%(np.min(q), prip_ipd_su_gpu, np.max(q))

# avg speed up from ipd cpu
q = (prip_mesa_tt - pripd_mesa_tt)/prip_mesa_tt
prip_ipd_su_mesa = np.sum(q)/len(prip_mesa_tt)
print 'prip_ipd_su_mesa = %f, %f, %f'%(np.min(q), prip_ipd_su_mesa, np.max(q))

#f = mpl.figure()
ax = f.add_subplot(122)
mpl.loglog(np.exp(prip_mesa_xx), prip_mesa_tt, 'b-', linewidth=2, label='CPU in-place')
mpl.loglog(np.exp(pripd_mesa_xx), pripd_mesa_tt, 'c-', linewidth=2, label='CPU disjoint')
mpl.loglog(np.exp(prip_gpu_xx), prip_gpu_tt, 'r-', linewidth=2, label='GPU in-place')
mpl.loglog(np.exp(pripd_gpu_xx), pripd_gpu_tt, 'g-', linewidth=2, label='GPU disjoint')
mpl.legend(prop={'size': 10, 'weight':'bold'})

mpl.loglog(prip_mesa_x, prip_mesa_t, 'b+', linewidth=2, label='CPU in-place')
mpl.loglog(pripd_mesa_x, pripd_mesa_t, 'c+', linewidth=2, label='CPU disjoint')
mpl.loglog(prip_gpu_x, prip_gpu_t, 'r+', linewidth=2, label='GPU in-place')
mpl.loglog(pripd_gpu_x, pripd_gpu_t, 'g+', linewidth=2, label='GPU disjoint')

mpl.title('In-place vs Disjoint Decomp. 3D\n1024^3 box at 1215x1090 res',fontweight='bold', fontsize=14)
mpl.ylabel('render time (seconds)',fontweight='bold', fontsize=12)
mpl.xlabel('Number of MPI Ranks',fontweight='bold', fontsize=12)
mpl.grid(True,which='both')
mpl.grid(which='major',ls='-')
mpl.grid(which='minor',ls=':')
#mpl.grid()
mpl.subplots_adjust(top=0.85)
mpl.xlim([7, 600])
mpl.ylim([1, 30])
mpl.setp(mpl.getp(ax, 'xticklabels'), fontsize=10, weight='bold')
mpl.setp(mpl.getp(ax, 'yticklabels'), fontsize=10, weight='bold')
for axis in [ax.get_xaxis(), ax.get_yaxis()]:
  axis.set_major_formatter(FuncFormatter(tl))
f.set_size_inches(12, 4)
#f.suptitle('CPU vs GPU Scaling')
f.subplots_adjust(bottom=0.15)

if saveFig:
  fig = mpl.gcf()
  #mpl.savefig('scaling-composite-cube-gpu.png',dpi=200)
  #mpl.savefig('scaling-composite-cube-gpu-sm.png',dpi=80)
  mpl.savefig('astronum-2014.png',dpi=200)
  mpl.savefig('astronum-2014-sm.png',dpi=80)
else:
  mpl.show()



#inplace gant
# mesa
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

fig = mpl.figure(figsize=(11,6))
fig.suptitle('INPLACE Compositing Activity by Rank\n1024^3 box 12.6M tris at 1215x1090 res',fontweight='bold',fontsize='14')

mpl.subplot(131)
groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<11:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('Mesa3D Gallium llvmpipe',fontweight='bold',fontsize='12')
mpl.xlabel('MPI Rank', fontweight='bold')
mpl.xlim([-0.75, 15.5])
#mpl.ylim([0, 140])
mpl.ylabel('time (sec)', fontweight='bold')
mpl.grid()

#mpl.legend((groupPlots[0],
#  groupPlots[1],
#  groupPlots[2],
#  groupPlots[3],
#  groupPlots[4],
#  groupPlots[5],
#  groupPlots[6],
#  groupPlots[7],
#  groupPlots[8],
#  groupPlots[9],
#  groupPlots[10]),
#  tuple(groups),
#  prop={'size': 9},
#  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
#mpl.subplots_adjust(top=0.85)
#
#if saveFig:
#  fig = mpl.gcf()
#  mpl.savefig('scaling-gant-inplace-composite-mesa.png',dpi=200)
#  mpl.savefig('scaling-gant-inplace-composite-mesa-sm.png',dpi=80)
#else:
#  mpl.show()


# gpu
ip_ev=['RenderGeometry','GatherVectors','TransformVectors','Integrate1','ContrastEnhance1','EdgeEnahnce','Integrate2','ContrastEnhance2','ComputeLIC','ColorLIC','ContrastEnhanceC','DepthCopy','RenderInternal','DepthCopy','RenderInternal']
#ip_ev=[RenderGeometry,GatherVectors,TransformVectors,Integrate1,ContrastEnhance1,EdgeEnahnce,Integrate2,ContrastEnhance2,ComputeLIC,ColorLIC,ContrastEnhance,DepthCopy,RenderInternal,DepthCopy,RenderInternal]
ip_r0=[1.77957,0.871629,0.0675631,0.398228,1.85473,0.00509691,0.028306,1.13959,3.72624,0.0189431,0.0334148,0.000921965,6.64048,9.799e-05,0.000164032,]
ip_r1=[0.869001,1.78278,0.0471549,0.395343,1.88091,0.00510097,0.0218539,1.14601,3.69689,0.0364749,0.0323751,0.000773907,6.63654,8.98838e-05,0.000152826,]
ip_r2=[0.921624,1.86765,0.034682,0.36549,1.85723,0.00506997,0.02175,1.14614,3.51334,0.0590839,0.0455821,0.000754833,6.63654,0.000100136,0.00016284,]
ip_r3=[1.65244,1.0819,0.238484,0.0809381,1.81199,0.00509691,0.0216448,1.14624,3.59648,0.036813,0.0494888,0.000750065,6.6252,9.89437e-05,0.000160933,]
ip_r4=[0.890389,1.65524,0.031513,0.0450931,2.44805,0.0050981,0.021507,1.14638,3.82074,0.020643,0.019233,0.000773907,6.63654,0.000114918,0.00018096,]
ip_r5=[1.8719,0.844927,0.0471551,0.411425,1.86547,0.00508809,0.020283,1.14761,3.66046,0.0262971,0.013798,0.000754118,6.62512,0.000108957,0.00018096,]
ip_r6=[0.849841,1.94521,0.0548589,0.375053,1.8339,0.00507283,0.0206659,1.14723,3.55882,0.0356419,0.0235841,0.000741005,6.63653,0.00011301,0.00018096,]
ip_r7=[1.71398,0.938363,0.0471499,0.403159,1.87269,0.00509214,0.020704,1.1472,3.71819,0.0314879,0.015476,0.000754118,6.6252,0.000109911,0.000182152,]
ip_r8=[0.954111,1.78636,0.116594,0.328937,1.93688,0.00510502,0.0138621,1.15405,3.66587,0.0346191,0.020097,0.000744104,6.61031,0.000118971,0.000200033,]
ip_r9=[1.81245,0.930721,0.00794911,0.0905972,2.28436,0.00510001,0.013181,1.15473,3.66686,0.037189,0.0137401,0.000757933,6.59952,0.000120163,0.000200033,]
ip_r10=[0.870563,1.86289,0.280492,0.0837379,1.91132,0.00508213,0.0137069,1.15424,3.66577,0.026696,0.015995,0.000769138,6.61031,9.91821e-05,0.000159025,]
ip_r11=[1.8696,0.87696,0.0496271,0.341856,1.98604,0.00509596,0.0131779,1.15475,3.6351,0.0402262,0.0390699,0.000757933,6.59919,0.00012207,0.000200987,]
ip_r12=[1.05146,1.70595,0.28299,0.096483,1.93928,0.00511479,0.0139329,1.15396,3.64693,0.0347471,0.0219619,0.000758171,6.61031,0.000120163,0.000200033,]
ip_r13=[1.8852,2.82913,0.00437689,0.053483,0.355646,0.00510502,0.01423,1.1537,1.66959,0.043499,0.0336111,0.000755072,6.59952,9.5129e-05,0.000159979,]
ip_r14=[1.00595,1.75133,0.2838,0.120439,1.91409,0.00508499,0.013237,1.15471,3.66547,0.0261841,0.012064,0.000766993,6.61031,9.5129e-05,0.000159025,]
ip_r15=[1.86739,0.869932,0.278342,0.111718,1.91914,0.00510192,0.013922,1.15401,3.65572,0.0313601,0.0178411,0.000736952,6.59952,0.000101089,0.000162125,]

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

#fig = mpl.figure()
#fig.suptitle('INPLACE Compositing Activity by Rank')

mpl.subplot(132)
groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<11:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('NVIDIA Quadro 5800',fontweight='bold',fontsize='12')
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
  mpl.savefig('scaling-gant-inplace-composite-gpu-mesa.png',dpi=200)
  mpl.savefig('scaling-gant-inplace-composite-gpu-mesa-sm.png',dpi=80)
else:
  mpl.show()






# inplace disjoint gant
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

fig = mpl.figure(figsize=(11,6))
fig.suptitle('INPLACE_DISJOINT Compositing Activity by Rank\n1024^3 box 12.6M tris at 1215x1090 res',fontweight='bold',fontsize='14')
mpl.subplot(131)

groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<12:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('Mesa3D Gallium llvmpipe',fontweight='bold',fontsize='12')
mpl.xlabel('MPI Rank', fontweight='bold')
mpl.xlim([-0.75, 15.5])
mpl.ylabel('time (sec)', fontweight='bold')
mpl.grid()

#mpl.legend((groupPlots[0],
#  groupPlots[1],
#  groupPlots[2],
#  groupPlots[3],
#  groupPlots[4],
#  groupPlots[5],
#  groupPlots[6],
#  groupPlots[7],
#  groupPlots[8],
#  groupPlots[9],
#  groupPlots[10],
#  groupPlots[11]),
#  tuple(groups),
#  prop={'size': 9},
#  bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
#mpl.subplots_adjust(top=0.85)
#
#if saveFig:
#  fig = mpl.gcf()
#  mpl.savefig('scaling-gant-inplace-disjoint-composite-mesa.png',dpi=200)
#  mpl.savefig('scaling-gant-inplace-disjoint-composite-mesa-sm.png',dpi=80)
#else:
#  mpl.show()

ipd_ev=['RenderGeometry','GatherVectors','TransformVectors','Integrate1','ContrastEnhance1','EdgeEnahnce','Integrate2','ContrastEnhance2','ComputeLIC','ScatterLIC','ColorLIC','ContrastEnhanceC','DepthCopy','RenderInternal','DepthCopy','RenderInternal']
#ipd_ev=[RenderGeometry,GatherVectors,TransformVectors,Integrate1,ContrastEnhance1,EdgeEnahnce,Integrate2,ContrastEnhance2,ComputeLIC,ScatterLIC,ColorLIC,ContrastEnhance,DepthCopy,RenderInternal,DepthCopy,RenderInternal]
ipd_r0=[1.88751,0.714266,0.150271,0.418676,1.17046,0.00510597,0.0201039,0.719209,2.62761,0.242069,0.0259569,0.0343978,0.00075984,5.86841,0.00011611,0.01512,]
ipd_r1=[0.908388,1.69208,0.27955,0.158536,1.10616,0.00509191,0.021333,0.718023,2.68701,0.189187,0.0239379,0.0302439,0.000758886,5.87739,0.00013113,0.015173,]
ipd_r2=[0.882457,1.8285,0.0549431,0.0995591,1.08854,0.00508308,0.0207479,0.718484,2.50381,0.248151,0.04162,0.026176,0.000767946,5.87734,0.000134945,0.0150928,]
ipd_r3=[1.68636,0.917476,0.315307,0.162033,1.11306,0.00511384,0.020869,0.718455,2.64412,0.202765,0.0117068,0.0803621,0.000902891,5.87584,0.000106096,0.0151038,]
ipd_r4=[0.92003,1.68706,0.159557,0.306749,1.1224,0.00510502,0.0264289,0.712933,2.63265,0.225963,0.0415838,0.0244339,0.00075984,5.87739,0.000165939,0.015121,]
ipd_r5=[1.82229,0.706869,0.036175,0.534692,1.25222,0.00511193,0.0199091,0.719432,2.7158,0.230636,0.023833,0.021781,0.000760078,5.86628,0.000133038,0.015173,]
ipd_r6=[1.00298,1.60184,0.153194,0.295245,1.13666,0.0050931,0.021225,0.718011,2.60619,0.250874,0.021585,0.0466011,0.000747919,5.87734,9.89437e-05,0.0151119,]
ipd_r7=[1.7834,0.770854,0.0352061,0.533221,1.25244,0.00510693,0.020263,0.719109,2.73278,0.195326,0.024189,0.0237339,0.000767946,5.86623,9.91821e-05,0.015085,]
ipd_r8=[0.973174,1.68843,0.0819991,0.11175,1.38427,0.00506401,0.014076,0.716258,2.51086,0.255392,0.032475,0.023649,0.000793934,5.86965,0.000102043,0.000169039,]
ipd_r9=[1.80894,0.747266,0.0671899,0.119015,1.37014,0.00506783,0.0143418,0.715999,2.63637,0.216894,0.035979,0.0284331,0.000777006,5.85747,0.000102043,0.000169039,]
ipd_r10=[0.93385,1.62198,0.139271,0.165187,1.42692,0.00510192,0.014915,0.715392,2.61926,0.218732,0.0106061,0.079318,0.000766039,5.86966,0.000101089,0.000168085,]
ipd_r11=[1.83044,0.663261,0.172213,0.184784,1.4535,0.00513601,0.0148959,0.715378,2.70869,0.198483,0.0105469,0.0722899,0.000748873,5.85622,0.000102043,0.000168085,]
ipd_r12=[1.04202,1.51437,0.137553,0.134123,1.45898,0.000160933,0.00870395,0.727476,2.61444,0.249753,0.030206,0.0336139,0.000756979,5.86965,0.000102043,0.000169039,]
ipd_r13=[1.74564,0.820645,0.087291,0.116887,1.38885,0.000119925,0.00829911,0.727986,2.68743,0.172381,0.022054,0.0359049,0.000766993,5.85798,0.000114918,0.000177145,]
ipd_r14=[0.950655,1.69706,0.02601,0.096159,1.35983,0.0050509,0.013932,0.716429,2.54794,0.228047,0.0311711,0.0285401,0.000777006,5.86965,0.000103951,0.000169992,]
ipd_r15=[1.96395,0.492511,0.0443649,0.232914,1.57908,0.00512815,0.014859,0.715378,2.69526,0.254131,0.027328,0.032398,0.000770807,5.85798,0.000101089,0.000168085,]

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


mpl.subplot(132)
groupPlots[0]=mpl.bar(ranks,groupData[0],color=groupColors[0],linewidth=0)
i=1
while i<12:
  groupPlots[i]=mpl.bar(ranks,groupData[i],bottom=groupDataBot[i],color=groupColors[i],linewidth=0)
  i+=1

mpl.subplots_adjust(right=1.125,hspace=0.05)
mpl.title('NVIDIA Quadro 5800',fontweight='bold',fontsize='12')
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
  mpl.savefig('scaling-gant-inplace-disjoint-composite-gpu-mesa.png',dpi=200)
  mpl.savefig('scaling-gant-inplace-disjoint-composite-gpu-mesa-sm.png',dpi=80)
else:
  mpl.show()

# gant


