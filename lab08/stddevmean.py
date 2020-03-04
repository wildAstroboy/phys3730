#!/usr/plocal/bin/python3
import numpy as np
import scipy.stats as stats

mu, sigma = 0.0, 1.0
N,M = 10, 1000
#np.random.seed(54321)
x = np.random.normal(mu,sigma,(M,N))
xmean = np.mean(x, axis=1)
#xstd = np.sqrt(np.sum(x-xmean)**2/(N-1))
xstd = stats.tstd(xmean)
#print(sigma/np.sqrt(N))

print(xstd)
print(np.mean(x))
