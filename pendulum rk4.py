import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_angle = -np.pi/2
initial_speed = 0
length = 1
gravity = 9.8
dimensions = 2
damping = 0

def animate(n):
    x1=[0,length*np.sin(y[n-1])]
    y1=[0,-length*np.cos(y[n-1])]
    ax.clear()
    ax.plot(x1,y1,marker='o',markersize=20)
    ax.set_xlim([-dimensions,dimensions])
    ax.set_ylim([-dimensions,dimensions])

steps = 2000
xvalue = 100
h = xvalue/steps

x = np.zeros(steps+1)

y = np.zeros(steps+1)
z = np.zeros(steps+1)

def dy(x,y,z):
    return z

def dz(x,y,z):
    return -gravity/length*np.sin(y)-damping/length*z

def rk4(x,y,z):
    k1 = h*dy(x,y,z)
    l1 = h*dz(x,y,z)
    k2 = h*dy(x+h/2,y+k1/2,z+l1/2)
    l2 = h*dz(x+h/2,y+k1/2,z+l1/2)
    k3 = h*dy(x+h/2,y+k2/2,z+l2/2)
    l3 = h*dz(x+h/2,y+k2/2,z+l2/2)
    k4 = h*dy(x+h/2,y+k3,z+l3)
    l4 = h*dz(x+h/2,y+k3,z+l3)
    return [(k1+2*k2+2*k3+k4)/6,(l1+2*l2+2*l3+l4)/6]
 
x[0],y[0],z[0]= 0,initial_angle,initial_speed

for i in range(steps):
    x[i+1] = x[i] + h
    y[i+1] = y[i] + rk4(x[i],y[i],z[i])[0]
    z[i+1] = z[i] + rk4(x[i],y[i],z[i])[1]
    
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

plt.plot(x,z)
#ani = FuncAnimation(fig, animate, frames=10000, interval=50, repeat=False)

plt.show()

#print(time2-time1)
