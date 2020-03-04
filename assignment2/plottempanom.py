#!/usr/plocal/bin/python3
import numpy as np
import pylab as pl
from scipy import stats

x = np.loadtxt('/u/course/p6720/data/tempanom.dat', usecols=0) # Year
y = np.loadtxt('/u/course/p6720/data/tempanom.dat', usecols=3) # Anom

a = stats.linregress(x,y)
slope = a[0]
intercept = a[1]
func = slope*x + intercept

pl.plot(y, 'o', label='Original Data')
pl.plot(func, 'r', label='Fitted Line')
pl.title('Temperature Anomolies vs Time')
pl.xlabel('Time')
pl.ylabel('Average Temp Anomolies')
pl.legend()
#pl.show()
pl.savefig('tempanom.png')
