import mpmath
from mpmath import *
import matplotlib.pyplot as plt


equation = 'abs(x)'
def integrator(x1,x2,dx,equation):
    A = 0
    for i in range(round((x2-x1)/dx)):
        x = x1+i*dx
        y1 = eval(equation)
        x = x1+(i+1)*dx
        y2 = eval(equation)
        A += dx*min(y1,y2)+dx*abs(y1-y2)*0.5
    return A

def innerproduct(x,y,L):
    equation = '('+x+')*('+y+')'
    return integrator(-L,L,0.01,equation)/L

def fourierseries(f,deg,L):
    s = innerproduct(f,'1/2',L)
    series = str(s)
    coeffs = [s]
    for i in range(1,deg):
        sinterm = 'sin('+str(i*pi/L)+'*x)'
        costerm = 'cos('+str(i*pi/L)+'*x)'
        sincoeff = innerproduct(f,sinterm,L)
        coscoeff = innerproduct(f,costerm,L)
        sincoeff = nstr(sincoeff,n=4)
        coscoeff = nstr(coscoeff,n=4)
        sinterm = str(sincoeff)+'*'+sinterm
        costerm = str(coscoeff)+'*'+costerm
        series = series + '+' + sinterm + '+' + costerm
        coeffs.append(sincoeff)
        coeffs.append(coscoeff)
    print(coeffs)
    #print(series)
    xlist = []
    y1 = []
    y2 = []
    for i in range(200):
        x = -L+L*i/100
        xlist.append(x)
        y1.append(eval(f))
        y2.append(eval(series))
    plt.plot(xlist,y1)
    plt.plot(xlist,y2)
    plt.show()

fourierseries(equation,10,1)
    





                 
                 
    
    
