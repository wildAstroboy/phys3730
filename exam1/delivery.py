#!/usr/plocal/bin/python3
import numpy as np

d = 90
mu_v = 30
sig_v = 6
n=5000
v = np.random.uniform(mu_v-sig_v,mu_v+sig_v,n)

def tavg(x):
    return d/x

print('average time: ',np.mean(tavg(v)))

