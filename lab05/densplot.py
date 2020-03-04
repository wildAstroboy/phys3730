#!/usr/plocal/bin/python3
import numpy as np
import pylab as pl
from matplotlib import cm

x = np.linspace(0,1,256)
y = np.linspace(0,1,256)
X,Y = np.meshgrid(x,y)
pi = np.pi
Z = (np.sin(4*pi*X)+np.sin(4*pi*Y))
msk = (X > 0.4) & (X < 0.6) | (Y > 0.4) & (Y < 0.6)
Z[msk] = -Z[msk]

pl.imshow(Z,cmap = cm.rainbow)
pl.savefig('denseplot.png')
#pl.show()
