import numpy as np

n = 100000000
y = np.arange(1,n)
msk = y % 2 == 0
y[msk] *= -1


print(np.sum(1/y))
