import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

initial_angle = -np.pi/2
initial_speed = 1
length = 1
gravity = 9.8
dimensions = 2
damping = 1

def animate(n):
    x1=[0,length*np.sin(y[500*(n-1)])]
    y1=[0,-length*np.cos(y[500*(n-1)])]
    ax.clear()
    ax.plot(x1,y1,marker='o',markersize=20)
    ax.set_xlim([-dimensions,dimensions])
    ax.set_ylim([-dimensions,dimensions])
 
    
steps = 1000000
xvalue = 100

x = np.zeros(steps+1)
y = np.zeros(steps+1)
dy = np.zeros(steps+1)
d2y = np.zeros(steps)

x[0],y[0],dy[0] = 0,initial_angle,initial_speed

for i in range(steps):
    x[i+1] = x[i] + xvalue/steps
    d2y[i] = -gravity/length*np.sin(y[i])-damping*dy[i]/length
    dy[i+1] = dy[i]+ xvalue*d2y[i]/steps
    y[i+1] = y[i] + xvalue*dy[i]/steps
    
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

time1 = time.time()
ani = FuncAnimation(fig, animate, frames=1000, interval=50, repeat=False)

plt.show()
time2 = time.time()
print(time2-time1)
