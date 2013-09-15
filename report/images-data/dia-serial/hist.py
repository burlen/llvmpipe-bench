import matplotlib.pyplot as mpl
import matplotlib.image as mplim
import numpy as np

lic1 = mplim.imread('lic-1-masked.png')
lic1v = []
r = 0
while(r < lic1.shape[0]):
  c = 0
  while(c < lic1.shape[1]):
    rgba = lic1[r,c]
    if (rgba[3]==1):
      lic1v.append(rgba[0])
    c += 1
  r += 1
nlic1v = min(lic1v)
xlic1v = max(lic1v)
print nlic1v
print xlic1v


lic1ce = mplim.imread('lic-1ce-masked.png')
lic1cev = []
r = 0
while(r < lic1ce.shape[0]):
  c = 0
  while(c < lic1ce.shape[1]):
    rgba = lic1ce[r,c]
    if (rgba[3]==1):
      lic1cev.append(rgba[0])
    c += 1
  r += 1
nlic1cev = min(lic1cev)
xlic1cev = max(lic1cev)
print nlic1cev
print xlic1cev



fig = mpl.Figure()

ax = mpl.subplot(221)
mpl.imshow(lic1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

mpl.title('LIC1', fontsize=12, fontweight='bold')
mpl.subplot(222)
mpl.grid()
mpl.hist(lic1v, bins=50, range=(0,1), facecolor=(0.45,0.45,0.45), alpha=1.0, histtype='stepfilled', linewidth=2)
mpl.plot([nlic1v, nlic1v],[0, 9000],'k--',linewidth=2)
mpl.plot([xlic1v, xlic1v],[0, 9000],'k--',linewidth=2)
mpl.ylim([0,9000])
mpl.title('LIC1 Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

ax = mpl.subplot(223)
mpl.imshow(lic1ce)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
mpl.title('CE1', fontsize=12, fontweight='bold')
mpl.subplot(224)
mpl.grid()
mpl.hist(lic1cev, bins=50, range=(0,1), facecolor=(0.45,0.45,0.45), alpha=1.0, histtype='stepfilled', linewidth=2)
mpl.plot([nlic1cev, nlic1cev],[0, 9000],'k--',linewidth=2)
mpl.plot([xlic1cev, xlic1cev],[0, 9000],'k--',linewidth=2)
mpl.ylim([0,9000])
mpl.title('CE1 Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

mpl.subplots_adjust(hspace=.35)

fig = mpl.gcf()
mpl.savefig('gray-ce1-curves.png',dpi=200)
mpl.savefig('gray-ce1-curves-sm.png',dpi=80)

mpl.show()




aa = mplim.imread('lic-2-aa-masked.png')
aav = []
r = 0
while(r < aa.shape[0]):
  c = 0
  while(c < aa.shape[1]):
    rgba = aa[r,c]
    if (rgba[3]==1):
      aav.append(rgba[0])
    c += 1
  r += 1
naav = min(aav)
xaav = max(aav)
print naav
print xaav

lic2ce = mplim.imread('lic-2-ce-masked.png')
lic2cev = []
r = 0
while(r < lic2ce.shape[0]):
  c = 0
  while(c < lic2ce.shape[1]):
    rgba = lic2ce[r,c]
    if (rgba[3]==1):
      lic2cev.append(rgba[0])
    c += 1
  r += 1
nlic2cev = min(lic2cev)
xlic2cev = max(lic2cev)
print nlic2cev
print xlic2cev


fig = mpl.Figure()

ax = mpl.subplot(221)
mpl.imshow(aa)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

mpl.title('AA', fontsize=12, fontweight='bold')
mpl.subplot(222)
mpl.grid()
mpl.hist(aav, bins=50, range=(0,1), facecolor=(0.45,0.45,0.45), alpha=1.0, histtype='stepfilled', linewidth=2)
mpl.plot([naav, naav],[0, 2000],'k--',linewidth=2)
mpl.plot([xaav, xaav],[0, 2000],'k--',linewidth=2)
mpl.ylim([0,2000])
mpl.title('AA Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('gray scale intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

ax = mpl.subplot(223)
mpl.imshow(lic2ce)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
mpl.title('CE2', fontsize=12, fontweight='bold')
mpl.subplot(224)
mpl.grid()
mpl.hist(lic2cev, bins=50, range=(0,1), facecolor=(0.45,0.45,0.45), alpha=1.0, histtype='stepfilled', linewidth=2)
#mpl.plot([nlic2cev, nlic2cev],[0, 2000],'k--',linewidth=2)
#mpl.plot([xlic2cev, xlic2cev],[0, 2000],'k--',linewidth=2)
mpl.ylim([0,2000])
mpl.title('CE2 Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('gray scale intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

mpl.subplots_adjust(hspace=.35)

fig = mpl.gcf()
mpl.savefig('gray-ce2-curves.png',dpi=200)
mpl.savefig('gray-ce2-curves-sm.png',dpi=80)

mpl.show()




clic1 = mplim.imread('pslic-lic-rgb-masked.png')
clic1vr = []
clic1vg = []
clic1vb = []
r = 0
while(r < clic1.shape[0]):
  c = 0
  while(c < clic1.shape[1]):
    rgba = clic1[r,c]
    if (rgba[3]==1):
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

clic2 = mplim.imread('pslic-lic-rgb-new-masked.png')
clic2vr = []
clic2vg = []
clic2vb = []
r = 0
while(r < clic2.shape[0]):
  c = 0
  while(c < clic2.shape[1]):
    rgba = clic2[r,c]
    if (rgba[3]==1):
      clic2vr.append(rgba[0])
      clic2vg.append(rgba[1])
      clic2vb.append(rgba[2])
    c += 1
  r += 1
#nclic2v = min(lic1v)
#xclic2v = max(lic1v)
#print nclic2v
#print xclic2v

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
mpl.plot([nclic1vr, nclic1vr],[0, 1700],'r--',linewidth=2)
mpl.plot([xclic1vr, xclic1vr],[0, 1700],'r--',linewidth=2)
mpl.plot([nclic1vg, nclic1vg],[0, 1700],'g--',linewidth=2)
mpl.plot([xclic1vg, xclic1vg],[0, 1700],'g--',linewidth=2)
mpl.plot([nclic1vb, nclic1vb],[0, 1700],'b--',linewidth=2)
mpl.plot([xclic1vb, xclic1vb],[0, 1700],'b--',linewidth=2)
mpl.ylim([0,1700])
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
#mpl.plot([nclic2v, nclic2v],[0, 2000],'k--',linewidth=2)
#mpl.plot([xclic2v, xclic2v],[0, 2000],'k--',linewidth=2)
mpl.ylim([0,1700])
mpl.title('CCE Distribution', fontsize=12, fontweight='bold')
mpl.xlabel('channel intensity', fontsize=10, fontweight='bold')
mpl.ylabel('pixel count', fontsize=10, fontweight='bold')

mpl.subplots_adjust(hspace=.35)

fig = mpl.gcf()
mpl.savefig('color-ce-curves.png',dpi=200)
mpl.savefig('color-ce-curves-sm.png',dpi=80)

mpl.show()
