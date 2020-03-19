#!/usr/plocal/bin/python3

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
x = np.arange(-2*pi, 2*pi, 0.01)
y = np.cos(x)**2
plt.plot(x, y, label='cos(x)^2')
plt.legend()
#plt.show()
plt.savefig('cosX_sqr.pdf')
