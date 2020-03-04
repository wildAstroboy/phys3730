#!/usr/plocal/bin/python3
import numpy as np
from scipy import stats

N = 500
S = 0
C = 1
R = 2
F = 4
x = np.zeros(N, dtype='int')
x[0] = 1
t = 100

for k in range(t):
    for i in range(N):
        if (x[i] == C):
            y = np.random.randint(0, N, F)
            for j in range(F):
                if (x[y[j]] == S):
                    P = np.random.randint(0,2)
                    #print('probability: ', P)
                    if (P == 1):
                        x[y] = C
                        x[i] = R
                    else:
                        x[i] = R

print(x)
