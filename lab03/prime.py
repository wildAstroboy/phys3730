#!/usr/plocal/bin/python3

for num in range(2,1001):
    if all(num%i!=0 for i in range(2,num)):
       print(num)
