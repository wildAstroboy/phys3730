#!/usr/plocal/bin/python3
import numpy as np

r = np.array([1,2,3])
s = np.array([-3,2,1])
t = np.cross(r,s)
Ut = t/np.linalg.norm(t)

# Confirming Ut is of unit length 1 and orthogonal
print('Length of unit vector t is:\n',np.sqrt(np.dot(Ut,Ut)))
print('Unit vector t dotted with r:\n',np.dot(Ut,r))          # value is to the order of mag of e-16 so close to zero
print('Unit vector t dotted with s:\n',np.dot(Ut,s))          # value is to the order of mag of e-16 so close to zero

N = 3
O = np.identity(N)
A = np.array([[-1,2,3],[4,-5,6],[7,8,-9]])

prod = np.dot(A,O)
print('A dotted with O:\n',prod)

transpose = A.T
print('A transpose:\n',transpose)

inv = np.linalg.inv(A)
print('A inverse:\n',inv)
prod2 = np.dot(A,inv)
print('Product of A and A inverse:\n', prod2)  # some matrix elements are e-17 so close to zero

w,V = np.linalg.eig(A)
for i in range(0,3):
  eig = np.dot(V[:,i],np.dot(A,V[:,i]))
  print('Eigenvector:',eig,'\nEigenvalues:',w[i])

b = np.array([1,2,3])
x = np.linalg.solve(A,b)
print('Solution to linear system:\n',x)
confirm = np.dot(A,x)
print('Confirming b:\n',confirm)
