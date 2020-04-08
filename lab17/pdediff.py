#!/usr/plocal/bin/python3
import numpy as np
import matplotlib.pyplot as plt

l = 0.1
N = 100
x = np.linspace(0,l,N)
alpha = 2.5e-5
T_hot = 100
T_cool = 0
#dx = l/(N-1)
dx = 0.001
#dt = dx**2/(2*alpha)
dt = 1e-4
u = np.zeros(N)
u[0] = T_hot
u[1:-2] = 20
u[-1] = T_cool
#tmax = l**2/(2*alpha)
tmax = 20
t = 0

while t<tmax:
    du = alpha/dx**2 * (u[:-2]-2*u[1:-1]+u[2:])
    u[1:-1] += dt*du
    t += dt

#print(u)
print('dt =', dt)
plt.plot(x, u, label='t = 20s')
plt.legend()
plt.show()
