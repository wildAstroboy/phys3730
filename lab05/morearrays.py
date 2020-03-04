#!/usr/plocal/bin/python3
import numpy as np

a = [0,1,3,-4]
b = [z**2 for z in a]

for ai in a:
    print(ai)

[print(bi) for bi in b]

x = np.array(a)
y = np.array(b)

for i in range(len(x)):
    print(x[i],y[i])
for xi,yi in zip(x,y):
    print(xi,yi)

xis = np.argsort(x)
xs = x[xis]

yis = np.argsort(y)
ys = y[yis]

for i in range(len(x)):
    print("(x,y)=", xs[i],",",ys[i])

A = np.array([[0,3,-1],[9,0,1]])

print(A)

for i in range(len(A)):
    for j in range(len(A)+1):
        print(A[i][j])

print(A[:,0], A[1,:], A[:,:])

for i in range(len(A)+1):
    A[0][i] = -99
    z = np.array([1,2,3])
    A[1][i] = z[i]
    new_values = ((A+A)/4)

for i in range(len(new_values)):
    for j in range(len(new_values)+1):
        new_values[i][j] *= 10

print(new_values)

Z = np.zeros((4,4))
O = np.ones((4,4))
D = np.diag(np.ones(4))
B = np.linspace(0,15,16)
B = B.reshape((4,4))
print(B)
print("Summing:", np.sum(B))
print("Dot Product:")
print(np.dot(B, B))


n = 4
x = np.linspace(0, n-1, n)
y = np.linspace(0, n-1, n)
X,Y = np.meshgrid(x,y)

print(X.shape)
