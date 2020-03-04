#!/usr/plocal/bin/python3
import math as m
import numpy as np
import math as m

"""
stirling_1 the version of the formula usually used. It is approximation for ln(n!) has an asymptotic error of 1/1400n**3
"""
def stirling_1(n):
    return (m.e**(n*np.log(n)-n))

def stirling_2(n):
    return (np.sqrt(2*np.pi*n)*(n/m.e)**n)

def fac(n):
    fact = 1
    for i in range(fact,n+1):
        fact = fact * i
    print(fact)

def math_fac(n):
    print(m.factorial(n))

def factorial_values(n):
    print("Stirling_1:")
    print(stirling_1(n))
    print("Stirling_2:")
    print(stirling_2(n))
    print("Fac(n):")
    fac(n)
    print("Math_Fac(n):")
    math_fac(n)

factorial_values(10)
