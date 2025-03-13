from arithmetic import *
from exponential import *

def mod(a,b):
    return basicdivide(a,b)[1]

def gcd(a,b):
    if a == b:
        return a
    n = maxi(a,b)
    if n[0] == a:
        a = mod(a,b)
        if a == '0':
            return b
        return gcd(a,b)
    else:
        b = mod(b,a)
        if b == '0':
            return a
        return gcd(a,b)

def lcm(l):
    if len(l) == 1:
        return l[0]
    l[0] = basicdivide(multiply(l[0],l[1]),gcd(l[0],l[1]))[0]
    l.pop(1)
    return lcm(l)

