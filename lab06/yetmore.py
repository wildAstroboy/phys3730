#!/usr/plocal/bin/python3
import numpy as np

I = 2 * np.ones((4,6), dtype=int)

B = np.ones((4,6), dtype=bool)

F = np.zeros((5,5,3), dtype=float)
F[:,:,2] = -99

print(I,B,F)

z = 2.0 + 3.0j
z_conj = np.conj(z)
z_real = np.real(z_conj)
z_imag = np.imag(z_conj)
z_abs = np.abs(z)
z_sum = z + z_conj
print(z_conj, z_real, z_imag, z_abs)
print('Sum of z and z conjugate:', z_sum)

a = 2
b = 3
rho = np.sqrt(a*a+b*b)
phi = np.arctan2(b,a)
print(z,rho*np.exp(1j*phi))
print(np.real(z) + np.imag(z), np.real(rho*np.exp(1j*phi)) + np.imag(rho*np.exp(1j*phi)), rho*(np.cos(phi) + np.sin(phi)))

pi = np.pi

phi = [0, pi/4, pi/2, 3*pi/2, 2*pi] 

for i in range(len(phi)):
    print(np.exp(1j*phi[i]))
