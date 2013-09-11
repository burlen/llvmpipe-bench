import matplotlib.pyplot as mpl
import matplotlib.image as mplim
import numpy as np

clic1 = mplim.imread('B-2_0088.png')
clic1vr = []
clic1vg = []
clic1vb = []
r = 0
while(r < clic1.shape[0]):
  c = 0
  while(c < clic1.shape[1]):
    rgba = clic1[r,c]
    #if (rgba[3]==1):
    clic1vr.append(rgba[0])
    clic1vg.append(rgba[1])
    clic1vb.append(rgba[2])
    c += 1
  r += 1
nclic1vr = min(clic1vr)
xclic1vr = max(clic1vr)
print nclic1vr
print xclic1vr
nclic1vg = min(clic1vg)
xclic1vg = max(clic1vg)
print nclic1vg
print xclic1vg
nclic1vb = min(clic1vb)
xclic1vb = max(clic1vb)
print nclic1vb
print xclic1vb
clic1 = mplim.imread('B-2_0088-lg.png')

clic2 = mplim.imread('B_0088.png')
clic2vr = []
clic2vg = []
clic2vb = []
r = 0
while(r < clic2.shape[0]):
  c = 0
  while(c < clic2.shape[1]):
    rgba = clic2[r,c]
    #if (rgba[3]==1):
    clic2vr.append(rgba[0])
    clic2vg.append(rgba[1])
    clic2vb.append(rgba[2])
    c += 1
  r += 1
#nclic2v = min(lic1v)
#xclic2v = max(lic1v)
#print nclic2v
#print xclic2v

clic2 = mplim.imread('B_0088-lg.png')
fig = mpl.Figure()

ax = mpl.subplot(221)
mpl.imshow(clic1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

mpl.title('LIC RGB', fontsize=12, fontweight='bold')
mpl.subplot(222)
mpl.grid()
mpl.hist(clic1vr, bins=50, range=(0,1), edgecolor='r', facecolor='r', alpha=0.3, histtype='stepfilled', linewidth=2)
mpl.hist(clic1vg, bins=50, range=(0,1), edgecolor='g', facecolor='g', alpha=0.3, histtype='stepfilled', linewidth=2)
mpl.hist(clic1vb, bins=50, range=(0,1), edgecolor='b', facecolor='b', alpha=0.3, histtype='stepfilled', linewidth=2)
mpl.hist(clic1vr, bins=50, range=(0,1), edgecolor='r', facecolor='r', alpha=1.0, histtype='step', linewidth=2)
mpl.hist(clic1vg, bins=50, range=(0,1), edgecolor='g', facecolor='g', alpha=1.0, histtype='step', linewidth=2)
mpl.hist(clic1vb, bins=50, range=(0,1), edgecolor='b', facecolor='b', alpha=1.0, histtype='step', linewidth=2)
mpl.plot([nclic1vr, nclic1vr],[0, 55000],'r--',linewidth=2)
mpl.plot([xclic1vr, xclic1vr],[0, 55000],'r--',linewidth=2)
mpl.plot([nclic1vg, nclic1vg],[0, 55000],'g--',linewidth=2)
mpl.plot([xclic1vg, xclic1vg],[0, 55000],'g--',linewidth=2)
mpl.plot([nclic1vb, nclic1vb],[0, 55000],'b--',linewidth=2)
mpl.plot([xclic1vb, xclic1vb],[0, 55000],'b--',linewidth=2)
mpl.ylim([0,55000])
mpl.title('LIC RGB Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('channel intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

ax = mpl.subplot(223)
mpl.imshow(clic2)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
mpl.title('CCE', fontsize=12, fontweight='bold')
mpl.subplot(224)
mpl.grid()
mpl.hist(clic2vr, bins=50, range=(0,1), edgecolor='r', facecolor='r', alpha=1.0, histtype='step', linewidth=2)
mpl.hist(clic2vg, bins=50, range=(0,1), edgecolor='g', facecolor='g', alpha=1.0, histtype='step', linewidth=2)
mpl.hist(clic2vb, bins=50, range=(0,1), edgecolor='b', facecolor='b', alpha=1.0, histtype='step', linewidth=2)
mpl.hist(clic2vr, bins=50, range=(0,1), edgecolor='r', facecolor='r', alpha=0.3, histtype='stepfilled', linewidth=2)
mpl.hist(clic2vg, bins=50, range=(0,1), edgecolor='g', facecolor='g', alpha=0.3, histtype='stepfilled', linewidth=2)
mpl.hist(clic2vb, bins=50, range=(0,1), edgecolor='b', facecolor='b', alpha=0.3, histtype='stepfilled', linewidth=2)
#mpl.plot([nclic2v, nclic2v],[0, 5500],'k--',linewidth=2)
#mpl.plot([xclic2v, xclic2v],[0, 5500],'k--',linewidth=2)
mpl.ylim([0,55000])
mpl.title('CCE Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('channel intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

mpl.subplots_adjust(hspace=.35,wspace=0.35)

fig = mpl.gcf()
mpl.savefig('color-ce-curves-khB.png',dpi=200)
mpl.savefig('color-ce-curves-khB-sm.png',dpi=80)

mpl.show()
