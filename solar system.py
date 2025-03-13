import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#differential equation
def orbit(t,state,gravitational_constant,mass):
    x,y,z,w = state

    dx = z
    dy = w
    dz = -gravitational_constant * mass * x/((x**2+y**2)**1.5)
    dw = -gravitational_constant * mass * y/((x**2+y**2)**1.5)

    return [dx,dy,dz,dw]

#parameters
gravitational_constant = 6.674*(10**-11)
mass = 1.989*(10**30)

p = (gravitational_constant,mass)
x_pos = 0
y_pos = 148.16*(10**9)
x_speed = 29780
y_speed = 0
y0 = [x_pos,y_pos,x_speed,y_speed]
t_span = (0,10000000000)
t = np.linspace(0,10000000000,num=1000000)

#equation solver
def solution(dist,speed):
    y0 = [0,dist,speed,0]
    result_solve_ivp = solve_ivp(orbit, t_span, y0, args=p, method='DOP853',t_eval=t)
    x = result_solve_ivp.y[0]
    y = result_solve_ivp.y[1]
    return [x,y]

#running the solver
mercury = solution(69.818*(10**9),38860)
venus = solution(108.941*(10**9),34790)
earth = solution(152.100*(10**9),29200)
mars = solution(249.261*(10**9),21970)
jupiter = solution(816.363*(10**9),12440)
saturn = solution(1506.527*(10**9),9090)
uranus = solution(3001.390*(10**9),6490)
neptune = solution(4558.857*(10**9),5370)
pluto = solution(7304.326*(10**9),3710)

#animation
def animate(n):
    ax.clear()
    ax.set_facecolor("black")
    yes = 8*(10**12)
    ax.set_xlim([-0.8*yes,0.8*yes])
    ax.set_ylim([-0.7*yes,yes])
    ax.plot(mercury[0],mercury[1],color='gray')
    ax.plot(venus[0],venus[1],color='orange')
    ax.plot(earth[0],earth[1],color='green')
    ax.plot(mars[0],mars[1],color='red')
    ax.plot(jupiter[0],jupiter[1],color='papayawhip')
    ax.plot(saturn[0],saturn[1],color='wheat')
    ax.plot(uranus[0],uranus[1],color='darkturquoise')
    ax.plot(neptune[0],neptune[1],color='royalblue')
    ax.plot(pluto[0],pluto[1],color='bisque')

    speed = 2000
    ax.plot(mercury[0][speed*n],mercury[1][speed*n],marker='o',markersize=5,color='gray')
    ax.plot(venus[0][speed*n],venus[1][speed*n],marker='o',markersize=5,color='orange')
    ax.plot(earth[0][speed*n],earth[1][speed*n],marker='o',markersize=5,color='green')
    ax.plot(mars[0][speed*n],mars[1][speed*n],marker='o',markersize=5,color='red')
    ax.plot(jupiter[0][speed*n],jupiter[1][speed*n],marker='o',markersize=5,color='papayawhip')
    ax.plot(saturn[0][speed*n],saturn[1][speed*n],marker='o',markersize=5,color='wheat')
    ax.plot(uranus[0][speed*n],uranus[1][speed*n],marker='o',markersize=5,color='darkturquoise')
    ax.plot(neptune[0][speed*n],neptune[1][speed*n],marker='o',markersize=5,color='royalblue')
    ax.plot(pluto[0][speed*n],pluto[1][speed*n],marker='o',markersize=5,color='bisque')
    
    ax.plot(0,0,marker='o',markersize=5,color='yellow')

#set up 
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ani = FuncAnimation(fig, animate, frames=10000, interval=10, repeat=False)

plt.show()
