#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as mpl

n_threads = [0,     2,     4,     8,     16,    20,    24,    28,    32   ]
t_osmesa = [62.07 ,37.46 ,24.58 ,20.26 ,18.12 ,17.83 ,20.39 ,20.75 ,21.43]

t_nvidia = 1.11
nvx = [0, 32]
nvt = [1.11, 1.11]

mpl.plot(nvx, nvt, 'b-', linewidth=2, label='Nvidia GTX 480')
mpl.plot(n_threads,t_osmesa,'ro-',linewidth=2, label='OS Mesa Gallium llvmpipe')
mpl.legend()
mpl.title('SurfaceLICPlanarVectorNormalizeOff',fontweight='bold')
mpl.ylabel('seconds',fontweight='bold')
mpl.xlabel('LP_NUM_THREADS',fontweight='bold')
mpl.grid()
mpl.show()


