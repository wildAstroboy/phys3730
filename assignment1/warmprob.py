#!/usr/plocal/bin/python3
import math as m

x = 129
y = 6

def C(n,r):
    result = m.factorial(n)/(m.factorial(r)*(m.factorial(n-r)))
    return result

print('Number of Combinations are:')
print(C(x,y))
print('Probability that the last six years were the hottest:')
print(1/C(x,y))
