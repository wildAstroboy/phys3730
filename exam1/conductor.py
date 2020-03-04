#!/usr/plocal/bin/python3
import numpy as np
import pylab as pl
from matplotlib import cm


x = np.linspace(-1,1,256)
y = np.linspace(-1,1,256)

X, Y = np.meshgrid(x,y)

r = 4 * np.pi
R = np.sqrt((X)**2+(Y)**2)

phi = 1/R
msk = (r > R)|(r <= R)
phi[msk]=-phi[msk]

pl.imshow(phi, cmap=cm.rainbow)
#pl.show()
pl.savefig('conductor.png')
