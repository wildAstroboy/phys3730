#!/usr/plocal/bin/python3
import numpy as np
import scipy.integrate as integrate
###############################################
# From Mathematica

print('The exact answer is:',1.71828)

################################################
# Trapezoidal Rule

n = 7
x_i = np.linspace(0,1,n)
dx_i = 1.0/(n-1)
w = np.ones(n)
w[0] = 0.5
w[-1] = 0.5
integral = np.sum(w*np.exp(x_i))*dx_i

print('Trapeziodal Rule:', integral)

################################################
# Simpson's Rule

N = 7
x_j = x_i
dx_j = 1.0/(N-1)
v = np.ones(N)
v[0] = 0.5
v[1] = 2
v[3] = 2
v[5] = 2
v[-1] = 0.5
simpson_integral = np.sum(v*2*np.exp(x_j))*dx_j/3

print("Simpson's Rule:", simpson_integral)

###############################################
# Quad Integrate

def f(x):
  return lambda x: np.exp(x)

def Integrate(x,a,b):
  I = integrate.quad(x,a,b,epsabs=1e-10)
  print('Scipy Quad:', I)

x = 0
Integrate(f(x),0,1)
