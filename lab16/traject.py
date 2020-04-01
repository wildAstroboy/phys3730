import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import matplotlib
import pylab as pl

def freefall(Y,t): return [Y[1],-9.8]
# here, Y = [y,vy], returns [dy/dt, dvy/dt]
# where dy/dt = vy (by definition in kinematics!)
# and dvy/dt is acceleration, define here as g = -9.8, grav accel in the lab.

n = 100 # number of time samples
tmax = 20 # max time
t = np.linspace(0,tmax,n) # these are the time samples
y0, v0 = 1000.0, 0.0      # initial conditions
sol = odeint(freefall, [y0,v0], t) # solve!
# sol[:,0] are y(t), sol[:,1] are vy(t)

altfn = interp1d(t,sol[:,0])
timefn = interp1d(sol[:,0],t)
print(altfn(tmax))
print('Time to reach altitude of 800m:', timefn(800),'seconds')

# here on in, just plotting..
print(t.shape,sol.shape)
pl.plot(t,sol[:,0],'-k')
pl.xlabel('time (s)')
pl.ylabel('value (a.u.)')

imfil = 'tmp.png'er
pl.savefig(imfil)

# could stop here,
import os
os.system('convert '+imfil+' ~/www/tmp.jpg')


