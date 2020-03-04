#!/usr/plocal/bin/python3
import matplotlib
import pylab as pl
import numpy as np
import scipy.stats as stats

n = 10
np.random.seed(123456)
x = np.random.uniform(0,1,n)
umean = stats.uniform.mean()
ustd = stats.uniform.std()

npmean = np.mean(x)
npstd = np.std(x)
print(x)

#pl.hist(x)
#pl.savefig('rndintro.png')

print(umean, npmean)
print(ustd, npstd)
