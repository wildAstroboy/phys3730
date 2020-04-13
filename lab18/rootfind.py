#!/usr/plocal/bin/python3
import numpy as np
from scipy.optimize import root
from scipy.optimize import brentq

def fn(x):
  return np.sqrt(1+x**2)-x * np.tan(x)

root = brentq(fn, 0,1)

print('Root of your function is:', root)
