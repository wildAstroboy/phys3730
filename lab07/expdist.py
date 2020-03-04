#!/usr/plocal/bin/python3
import matplotlib
import pylab as pl
import numpy as np
from scipy import stats as stats


# generate samples
n = 1000
mu = 2.0 # mean
sig = 0.5 # std dev 
zsamples = np.random.exponential(sig,n)+mu

# generate theoretical probability density function
zgridpts = np.linspace(0,4,n)
pdf = stats.expon(mu,sig).pdf(zgridpts) # theoretical; why not call it 'normal'?

# plot both
pl.hist(zsamples,bins=20,density=True,histtype='step',zorder=1)
pl.plot(zgridpts,pdf,zorder=0)
pl.xlabel('z')
pl.ylabel('p(z)')

#pl.show()
# or
pl.savefig('expdist.png')
