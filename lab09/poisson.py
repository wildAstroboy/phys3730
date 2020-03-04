#!/usr/local/bin/python3

import numpy as np
from scipy import stats
import matplotlib
import pylab as pl
from scipy import stats


mu = 20.0
N = 1000
n= np.random.poisson(mu, N)

xt = np.arange(9,35)
yt = stats.poisson(mu).pmf(xt)

print(np.size(np.where(n> 30))/N)

pl.plot(xt,yt)
pl.hist(n, bins= np.arange(10,30), density = True)
pl.show()


