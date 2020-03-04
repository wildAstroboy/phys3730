#!/usr/plocal/bin/python3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

sigma = 1.0
N = 1000
slope = 0.5
x = np.random.normal(0,sigma,N)
y = np.random.normal(0,sigma,N)
yc = np.random.normal(0,sigma,N) + slope * x
ya = np.random.normal(0,sigma,N) - slope * x

a = stats.linregress(x, y)
b = stats.linregress(x, ya)
c = stats.linregress(x, yc)

print('slope:', a[0], b[0], c[0])
print('intercept', a[1], b[1], c[1])
print('p_values:', a[3], b[3], c[3])

plt.plot(x, y,'b.')
plt.plot(x, a[0]*x+a[1])
plt.plot(x, ya, 'r.')
plt.plot(x, b[0]*x+b[1])
plt.plot(x, yc,'b.')
plt.plot(x, c[0]*x+c[1])
plt.savefig('linregress.png')
#plt.show()
