#!/usr/plocal/bin/python3
import numpy as np
import math as m

rho = 2500  # kg/m^3
G = 6.673e-11  # Gravitational constant
M = 5.972e24  # Mass of Earth in kg
a = 6378.137  # Equitorial radius of Earth in km
b = 6356.752  # Polar radius of Earth in km
phi = np.radians(40.764996)  # degrees on polar angle
rho = 2500  # kg/m^3

Re = m.sqrt(((a ** 2 * np.cos(phi)) ** 2 + (b ** 2 * np.sin(phi)) ** 2) / ((a * np.cos(phi)) ** 2 + (b * np.sin(phi)) ** 2))
#Re = 6371 # Earths mean radius in km

# Calculate g per each 1x1x1 block and sum them up. From there subtract it from actual acceleration.
r = 49.5  # Furthest distance to our point masses in meters
dw = 1  # Width element of our cube.
volume_cube = 20**3  # Cube of side length 20 meters
d_cube = dw**3  # Volume element of our cube, 1x1x1.
g = -(G * M) / (1000 * Re) ** 2

print('Radius of the Earth as the University of Utah is:', Re, 'km')
print('The Acceleration due to Gravity at the University is:', g, 'm/s^2')

M_cube = rho * volume_cube  # Mass of our 20x20x20 cube
dm_cube = rho * d_cube # Mass of our 1x1x1 cube element
print('Mass of the 20x20x20 cube chamber is:', M_cube)
print('Mass of the 1x1x1 cube chamber is:', dm_cube)

#
def accel_earth(x):
  return -(G * x) / (1000 * Re) ** 2

def accel_cube(x):
  return -(G * x) / (50) ** 2

def accel_cube2(x):
  for i in np.arange(0, 21, 1):
    accel = -(G * x) / (r - i) ** 2
    #print(accel)
    accel += accel
  return(accel)

first_est = accel_earth(M) - accel_cube(M_cube)
sec_est = accel_earth(M) - accel_cube2(dm_cube)
print("Acceleration at Presidents' Circle:\n", accel_earth(M))
print('First Estimate of dg using 20x20x20:\n', first_est)
print('Second Estimate of dq using 1x1x1:\n', sec_est)

print('Difference in estimate is:\n', first_est-sec_est)

print(accel_cube(M_cube), accel_cube2(dm_cube))
