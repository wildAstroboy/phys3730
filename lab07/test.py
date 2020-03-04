import matplotlib
import pylab as pl
import numpy as np
from scipy import stats as stats


# generate samples
n = 1000
mu = 0.0 # mean
sig = 1.0 # std dev 
zsamples = np.random.normal(0,1.0,n)

# generate theoretical probability density function
zgridpts = np.linspace(-4,4,1000)
pdf = stats.norm(mu,sig).pdf(zgridpts) # theoretical; why not call it 'normal'?

# plot both
pl.hist(zsamples,bins=20,density=True,histtype='step',zorder=1)
pl.plot(zgridpts,pdf,zorder=0)
pl.xlabel('z')
pl.ylabel('p(z)')

pl.show()
# or
#pl.savefig('plot.png')
