#!/usr/plocal/bin/python3
import numpy as np
import sys

n = 10
ntrials = 1000000

x = np.random.randint(0,2,(ntrials,n))
y = np.sum(x,axis=1)
z = np.where(y>=n-1,1,0)
prob = np.sum(z)/ntrials
print(prob*100,'%')
#print(np.size(z))
#print(x)
#print(y)
#print(z)
