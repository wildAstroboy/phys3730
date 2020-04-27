#!/usr/plocal/bin/python3
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import matplotlib
import pylab as pl

#def pend(Theta, t):
# return -g/L*np.sin(Theta) - C/L/M*np.sin(dThetadt)


def pend(theta,t,M,L,C,g):
  theta1 = theta[0]
  theta2 = theta[1]
  dtheta1_dt = theta2
  dtheta2_dt = -g/L*np.sin(theta1) - C/L/M*np.sin(theta2)
  dtheta_dt = [dtheta1_dt, dtheta2_dt]

  return dtheta_dt

M = 1.0
L = 1
C = 0.5
g = 9.8
theta_0 = [np.pi/4,0] # initial conditions
tmax = 20 # max time
n = 240 # number of time samples
t = np.linspace(0,tmax,n) # these are the time samples
theta = odeint(pend, theta_0, t, args=(M,L,C,g)) # solve!
# sol[:,0] are y(t), sol[:,1] are vy(t)
T = 2* np.pi * np.sqrt(L/g)

print('Period is:', T)

# here on in, just plotting..

#print(t.shape,sol.shape)
pl.plot(t,theta[:,0],'-b', label='Displacement')
pl.plot(t,theta[:,1], '--', label='Velocity')
pl.xlabel('Time (s)')
pl.ylabel('Value')
pl.legend()
#pl.show()
imfil = 'pendulum.png'
pl.savefig(imfil)


