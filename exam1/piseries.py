#!/usr/plocal/bin/python3
import numpy as np

a = np.sqrt(12)
n = 21
total = 0
for i in np.arange(0,n,1):
   total += (-1.0/3.0)**(i)/((2.0*i)+1.0)
   
   
print(a*total)
