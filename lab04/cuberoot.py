#!/usr/plocal/bin/python3
import numpy as np

def cube_root(x):
    y = x**(1/3)
    return y


a = 1000
b = 0.027
c = 1.0e6
d =  [0.0, 10.0, 30.1]
e = np.array(d)
print(cube_root(a))
print(cube_root(b))
print(cube_root(c))
print(cube_root(e))
