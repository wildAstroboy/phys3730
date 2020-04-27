#!/usr/plocal/bin/python3
# this code calculates trajectories of Earth and a satellite (or space ship)
# orbiting the Sun, and prints out how close they came to each other.

import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import pylab as pl
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import scipy.optimize as opt

AU = 1.496e11       # 1 astronomical unit in meters
G = 6.67384E-11     # MKS
Msun = 1.988500E+30 # kg
Mearth = 5.9726E+24
Rearth = 6371.0E+03 # meters

def gravaccel(p,t):
    # this is for an ODE solver! It sets derivaties (vel and acceration)
    # for a satellite (xs,ys, vxs,vys) and the Earth (xe, ye, vxe, vye)
    # as they orbit the Sun. NOte that the satellite feels the gravity of both
    # Sun and Earth.
    xs,ys,xe,ye,vxs,vys,vxe,vye = p # positions and velocities
    # earth first:
    re = np.sqrt(xe**2+ye**2)
    dvex = -G*Msun*xe/re**3 # accel of Earth from Sun
    dvey = -G*Msun*ye/re**3 #
    # satellite next:
    rs = np.sqrt(xs**2+ys**2) # rel to Sun
    dx,dy = xs-xe, ys-ye # satellite in Earth frame
    dr = np.sqrt(dx**2+dy**2)
    dvsx = -G*Msun*xs/rs**3 - G*Mearth*dx/dr**3
    dvsy = -G*Msun*ys/rs**3 - G*Mearth*dy/dr**3
    return np.array([vxs,vys,vxe,vye,dvsx,dvsy,dvex,dvey])

# satellite position and velocity (units: m, m/s)
xs0, ys0 = 1.37801793e+11, 2.31478719e+11
vxs0, vys0 = -8490.32975, -14063.6905

# earth position and velocity
xe0, ye0 = 1.4959787e+11, 0
vxe0, vye0 = 0, 29784.3405

p0 = np.array([xs0,ys0,xe0,ye0,vxs0,vys0,vxe0,vye0]) # starting conditions

nsamp = 100000  # need a lot of points to resolve a close encounter with the Earth
year = 365.25*24*3600 # year in seconds
t = np.linspace(0,0.3*year,nsamp)
p = odeint(gravaccel,p0,t)
xs,ys,xe,ye,vxs,vys,vxe,vye = p.T  # note the transpose cuz time index is first in p

def closest(xs,ys,xe,ye,t):
    dx = xs-xe
    dy = ys-ye
    dr = np.sqrt(dx*dx+dy*dy)
    return dr.min() # just return the min of the array! need good sampling!!

a0 = np.array([10, 50])
def optfun(a):
  dvx, dvy = a
  retval = opt.minimize(gravaccel,[p0,t], method='Nelder-Mead')
  return retval

print('Optimization is:', optfun(a0))

print('closest approach (Earth radii):',closest(xs,ys,xe,ye,t)/Rearth)

# if you want to plot this...
pl.plot(xs0,ys0,'ob',xe0,ye0,'ok') # startin points plotted as circles
pl.plot(p[:,0],p[:,1],'-b',p[:,2],p[:,3],'-k')
pl.plot(xs,ys,'-b',xe,ye,'-k')
pl.savefig('satellite.png')
