#!/usr/plocal/bin/python3
import numpy as np
import sys

n = 5 # Default value for the number of coin flips

#If the user inputs a value greater than 1 in the command line, otherwise ask the user for input
if len(sys.argv)>1:
    n = int(sys.argv[1])
else:
    print('Enter the number of times to flip the coin: ',end='')
    userinput = input()
    n = int(userinput)

print(np.random.randint(2, size=n))


