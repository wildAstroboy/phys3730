#!/usr/plocal/bin/python3
import numpy as np
import pylab as pl
from matplotlib import cm

ninter = 25
x = np.linspace(-2,1,256)
y = np.linspace(-1,1,256)
mandset = np.zeros([256,256])

for i in range(len(x)):
  for j in range(len(y)):
    Z = 0
    C = x[j] + 1j*y[i]
    for k in range(ninter):
      Z = Z**2 + C
      if np.absolute(Z)>2:
        mandset[i,j] = k
        break


pl.imshow(mandset,extent=[-2,1,-1,1],cmap = 'plasma')
pl.savefig('mandelbrot.png')
#pl.show()
