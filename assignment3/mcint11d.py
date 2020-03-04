#!/usr/plocal/bin/python3
import numpy as np

# Define our unit hypersphere
def hypersphere(x):
    return 1 if np.dot(x,x) < 1.0 else 0

# Number of samples to take
n = 10**6
# Our Dimension
d = 11
# Our multiplying factor since we are only getting samples from a quarter of our hypersphere, changes per dimension
m = 2**d

# Random numbers uniformly sampled
x = np.random.uniform(0, 1, (n, d))

# Creating an array of zeros that are the size of our number of samples
f = np.zeros(n)

# Take a sample and check to see if it's within our unit boundary
for i in range(n):
    f[i] = hypersphere(x[i])

print('Volume of an 11-D unit Hypersphere: ', m * np.mean(f), '+/-', m * np.std(f) / np.sqrt(n), 'Actual is: ', (64 * np.pi ** 5) / 10395)
