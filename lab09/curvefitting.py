#!/usr/local/bin/python3

import numpy as np
from scipy import stats
import matplotlib
import pylab as pl
from scipy import stats
from scipy import optimize as opt

def foo(x, y0=7,m=.33):
    return m * x + y0


N =10
x = np.linspace(0,1,N)
uncertainty = .1
noise = np.random.normal(0,uncertainty, N)
y = foo(x) + noise

popt, pcov = opt.curve_fit(foo,x,y)
#print(popt, pcov)

xf = np.linspace(0,1,250)
yf = foo(xf, popt[0], popt[1])

chi2 = np.sum((y-foo(x,popt[0], popt[1]))**2 / uncertainty **2)
print(chi2)
print(chi2/N)
gof = stats.chi2(N-2).sf(chi2)
print(gof)

pl.plot(xf,yf, 'k')

pl.plot(x,y, 'om', zorder=99)
pl.errorbar(x,y, yerr= np.ones(N)*uncertainty)
#pl.plot(x,y,'-k', zorder =1)
pl.show()

