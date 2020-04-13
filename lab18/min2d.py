#!/usr/plocal/bin/python3
import numpy as np
from scipy import optimize as opt
import matplotlib
#matplotlib.use("Agg") # comment out this line if running w/o X or remote desktop
import pylab as pl
import os

ofil = "min2d.png" # output file

np.random.seed(193423)

def func(r):
    x,y = r
    f = 1-np.exp(-((x-1.23)**2+(y+0.678)**2)/(8.0)) # one dip
    return f

def func_ugh(r):
    x,y = r
    r2 = x*x+y*y
    f = np.sin(2*np.pi*r2/20.0)*np.sin(x/6.0)/(r2+1)
    return f


def plotfunc(func,L):
    # func(r) where r=[x,y], 2-d position and L = width of plot region about origin.
    xmin, xmax, ymin, ymax, nbins = -L/2, L/2, -L/2, L/2, 250
    xi, yi = np.mgrid[xmin:xmax:nbins*1j, ymin:ymax:nbins*1j]
    xy = np.vstack([xi.flatten(), yi.flatten()])
    zi = func(xy)
    cc=pl.cm.jet
    pl.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=cc, zorder=0)
    pl.colorbar()
    # C = pl.contour(xi, yi, zi.reshape(xi.shape),colors='k')
    # pl.clabel(C)
    pl.xlabel('x'); pl.ylabel('y')
    pl.xlim(xmin,xmax); pl.ylim(ymin,ymax)

# insert min finder here!!!
X0 = np.array([0,0])
X1 = np.array([4,0])

# Minimize of function 1
resfn = opt.minimize(func,X0,method='Nelder-Mead',tol=1e-4)
print('Function 1 xmin, ymin:',resfn.x)
print('fmin:', resfn.fun)

# Minimize of function 2
resugh_x0 = opt.minimize(func_ugh,X0,method='Nelder-Mead',tol=1e-4)
resugh_x1 = opt.minimize(func_ugh,X1,method='Nelder-Mead',tol=1e-4)
print('Function 2 with X = [0,0], xmin, ymin:', resugh_x0.x)
print('fmin:', resugh_x0.fun)
print('Function 2 with X = [4,0], xmin, ymin:', resugh_x1.x)
print('fmin:', resugh_x1.fun)

L = 10 # width of plot region
#plotfunc(func,L) # Function 1
plotfunc(func_ugh,L) # Plotting Function 2

#pl.savefig(ofil)


#pl.show() # uncomment if in X windows/remote desktop.

#print('dumping image file to tmp dir...')

#os.system("convert "+ofil+" ~/public_html/tmp.jpg")
