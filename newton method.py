from mpmath import *

def solve(a,b,c,d):
    variance = c
    accuracy = d
    def f(x):
        return eval(a)-eval(b)
    
    def g(x):
        return variance*1.5**(x-50)
    def newton(x,depth):
        if depth == 0:
            return x
        dx = 1000*(f(x+0.001)-f(x))
        if dx == 0:
            return x
        return newton(x-(f(x)+g(depth))/dx,depth-1)
    
    ans = []
    interval = [-5,5,10/accuracy]
    for i in range(round((interval[1]-interval[0])/interval[2])):
        x1 = mpf(interval[0]+i*interval[2])
        l = newton(x1,50)
        k = f(l)
        l = round(l,5)
        k = round(k,5)
        if l not in ans and k == 0:
            ans.append(l)
    return sorted(ans)
