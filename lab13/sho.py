#!/usr/plocal/bin/python3
import numpy as np
import matplotlib.pyplot as plt

t, x, v, e = np.loadtxt('sho.txt', unpack=True)

plt.plot(t,x, 'r', label='Position')
plt.plot(t,v, 'b', label='Velocity')
plt.plot(t,e, 'g', label='Energy')
plt.xlabel('Time')
plt.ylabel('Position/Velocity')

plt.legend()

#plt.show()
plt.savefig('sho.png')
