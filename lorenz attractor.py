import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 100000

# Need one more for the initial values
xs = np.empty(num_steps)
ys = np.empty(num_steps)
zs = np.empty(num_steps)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps-1):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

x = np.array([])
y = np.array([])
z = np.array([])

def animate(n):
    global x,y,z
    x = np.append(x,xs[2*n])
    y = np.append(y,ys[2*n])
    z = np.append(z,zs[2*n])
    ax.clear()
    ax.plot(x,y,z)
    ax.set_xlim([-20,20])
    ax.set_ylim([-20,30])
    ax.set_zlim([0,50])

# Plot
ax = plt.figure().add_subplot(projection='3d')
fig = plt.figure()
ax = Axes3D(fig)

#ax.plot(xs,ys,zs,lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
#ani = FuncAnimation(fig, animate, frames=10000, interval=1, repeat=False)
ax.plot(xs,ys,zs,lw=0.1)
plt.show()
