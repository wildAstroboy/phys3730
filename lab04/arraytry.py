#!/usr/plocal/bin/python3
import numpy as np

n = 10
x = np.linspace(0, 10, n)

for i in range(n):
    x[i] = i
print(x)

for i in range(n):
    if x[i] > 4.5:
        x[i] = -99
print(x)

for i in range(n):
    if x[i] == -99:
        x[i] = np.linspace(i,i,1)
print(x)

#print(len(x))
#print(x[-1], x[2:4], x[8:], x[::-1], x[::2])

        
#y = x.copy()
#y[-1] = -99
y = np.sin(x)
print(x,y)

#np.copy creates a new array from a previous array. You are able to maniipulate the data in array 2 with out affecting the data in array 2.


