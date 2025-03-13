import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


#differential equation
def orbit(t,state,gravitational_constant,mass):
    x,y,z,w = state

    dx = z
    dy = w
    dz = -gravitational_constant * mass * x/((x**2+y**2)**1.5)
    dw = -gravitational_constant * mass * y/((x**2+y**2)**1.5)

    return [dx,dy,dz,dw]

#parameters
gravitational_constant = 1
mass = 1
p = (gravitational_constant,mass)
x_pos = 0
y_pos = 1
x_speed = 1.414
y_speed = 0
y0 = [x_pos,y_pos,x_speed,y_speed]
t_span = (0,100000000)
t = np.linspace(0,100000000,num=100000)

result= solve_ivp(orbit, t_span, y0, args=p, method='DOP853',t_eval=t)

fig, ax = plt.subplots()
line, = ax.plot(result.y[0],result.y[1])
ax.set_xlim([-50,500])
ax.set_ylim([-50000,100])

fig.subplots_adjust(bottom=0.25)

axspeed = fig.add_axes([0.25, 0.1, 0.65, 0.03])
speed_slider = Slider(
    ax=axspeed,
    label='Speed',
    valmin=1.414,
    valmax=1.415,
    valinit=x_speed,
)

resultlist = []
interval = speed_slider.valmax-speed_slider.valmin

for i in range(300):
    yes = speed_slider.valmin+i*interval/300
    result = solve_ivp(orbit, t_span, [0,1,yes,0], args=p, method='DOP853',t_eval=t)
    resultlist.append([result.y[0],result.y[1]])
    
def update(val):
    yes = speed_slider.valmax-speed_slider.valmin
    no = round((speed_slider.val-speed_slider.valmin)*300/yes)
    line.set_xdata(resultlist[no][0])
    line.set_ydata(resultlist[no][1])

speed_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    speed_slider.reset()
button.on_clicked(reset)

plt.show()

    
