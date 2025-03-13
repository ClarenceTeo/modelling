from mpmath import *


def solve(a,b):
    def f(x):
        return eval(a)-eval(b)

    def binary(x1,x2,depth):
        if depth == 0 or f(x1) == 0:
            return float(x1)
        if f(x2) == 0:
            return float(x2)
        m = (x1+x2)/2
        if f(m)>0:
            return binary(x1,m,depth-1)
        else:
            return binary(m,x2,depth-1)
    
    ans = []
    interval = [-10,10,0.01]
    for i in range(round((interval[1]-interval[0])/interval[2])):
        x1 = mpf(interval[0]+i*interval[2])
        x2 = mpf(interval[0]+(i+1)*interval[2])
        if f(x1)==0:
            ans.append(float(x1))
        if f(x1)<0 and f(x2)>0:
            ans.append(binary(x1,x2,10))
        if f(x1)>0 and f(x2)<0:
            ans.append(binary(x2,x1,10))
    return ans
