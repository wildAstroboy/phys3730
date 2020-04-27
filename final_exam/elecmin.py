#!/usr/plocal/bin/python3
import numpy as np
from scipy import optimize as opt
import pylab as pl

def f(r):
  x,y,z = r
  f = -np.exp(-(0.5*(x-0.5)**2+(y-2)**2+(z+1)**2)/2**2) # electron cloud
  f += (x**2 + y**2 + z**2)/100                         # molecular potential
  return f

X0 = np.array([0,0,0])
resfn = opt.minimize(f,X0,method='Nelder-Mead',tol=1e-4)
print('Function xmin, ymin, zmin:',resfn.x)
print('fmin:', resfn.fun)
