#!/usr/plocal/bin/python3
import numpy as np
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ofil = 'tmp.gif'

# the set-up
fig, ax = plt.subplots()
#l = plt.plot([0],[0],'ko',markersize=20)
plt.xlabel('x'); plt.ylabel('y')
L = 2.2
ax = plt.axis([-L/2,L/2,-L/2,L/2])
line, = plt.plot([],[],'b')
line2, = plt.plot([],[],'b')
line3, = plt.plot([],[],'g')
line4, = plt.plot([],[],'g')

# an "artistic" function to call from within the animation code
pltorb,  = plt.plot([], [], 'o')
pltorb2, = plt.plot([], [], 'o')
pltorb3, = plt.plot([], [], 'o')
pltorb4, = plt.plot([], [], 'o')

xdata = []
ydata = []

x2data = []
y2data = []

def init():
  line.set_data([],[])
  return line,

def animate(i): # all we do here is set up pltorb w/data, pass it to the animatoe
    x,y = np.cos(i),np.sin(i)*np.cos(i)
    x2,y2 = -np.cos(i),-np.sin(i)*np.cos(i)
    x3,y3 = np.cos(i)*np.sin(i),np.sin(i)
    x4,y4 = -np.cos(i)*np.sin(i),-np.sin(i)

    pltorb.set_data(x,y)
    pltorb2.set_data(x2,y2)
    pltorb3.set_data(x3,y3)
    pltorb4.set_data(x4,y4)

    t = np.linspace(0, i)
    linex = np.cos(t + i/100)
    liney = np.sin(t+i/100)*np.cos(t+i/100)
    xdata.append(linex)
    ydata.append(liney)

    linex2 = np.cos(t + i/100)*np.sin(t + i/100)
    liney2 = np.sin(t + i/100)

    line.set_data(linex,liney)
    line2.set_data(-linex,-liney)
    line3.set_data(linex2,liney2)
    line4.set_data(-linex2,-liney2)

    return line, line2, line3, line4, pltorb, pltorb2, pltorb3, pltorb4,

# create animation using the animate() function
nfrms = 90 # number of frames
frms = np.linspace(0,2*np.pi,nfrms) # each element corresponds to a frame

myanim = animation.FuncAnimation(fig, animate, init_func=init, frames=frms, blit=True, repeat=True)
# in this funcion, animate(frms[i]) is called for i=0,1,...nfrms-1.

# could do plt.show()
plt.show()
#myanim.save(ofil, writer='imagemagick', fps=30)
