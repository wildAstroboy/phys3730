#!/usr/plocal/bin/python3
import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('init.dat', unpack=True)

print(x,y)
plt.plot(x,y)
plt.plot(x,y,'-b')
plt.plot(x,y,'.k')
plt.xlim(-.5, 6.5)
#plt.show()
plt.savefig('myplot.png')
