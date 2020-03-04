#!/usr/plocal/bin/python3

import numpy as np
from scipy import stats
import matplotlib
import pylab as pl
from scipy import stats

def circle(x):
    return 1 if np.dot(x,x) < 1.0 else 0

n=10000
x = np.random.uniform(0,1,(n,2))

f = np.zeros(n)
for i in range(n):
    f[i] = circle(x[i])

print('answer: ', 4*np.mean(f), '+/-', 4*np.std(f)/np.sqrt(n), 'vs', np.pi)

msk = f > 0.0
xin = x[msk,0]
yin = x[msk,1]

pl.plot(xin,yin, 'k.')
pl.show()
