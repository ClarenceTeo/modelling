from arithmetic import *
import time
import numpy as np
from rational import *


def betterlistmultiply(l,dpoint=10):
    l2 = []
    if len(l) == 1:
        return l[0]
    while len(l) != 0 and len(l) != 1:
        l2.append(multiply(l[0],l[1]))
        l.pop(0)
        l.pop(0)
    if len(l) == 1:
        l2.append(l[0])
        return betterlistmultiply(l2,dpoint)
    return betterlistmultiply(l2,dpoint)

def horners(px,x,n,dpoint):
    if n == intify(minus(len(px),1)):
        return px[-1]
    return add(px[n],multiply(x,horners(px,x,intify(add(n,1)),dpoint),dpoint))

def ln(x,dpoint=10):
    num = 0
    e = 2.71828182845904523536
    while isneg(minus(1.45,x)):
        x = divide(x,e,dpoint)
        num = add(num,1)
    x = minus(x,1)
    ans = listadd([30,1,neg(multiply(30,x,dpoint))])
    for i in range(30):
        a = minus(30,i)
        ans = listadd([a,multiply(minus(1,a),x,dpoint),divide(listmultiply([a,a,x],dpoint),ans,dpoint)])
    print(x,ans,divide(x,ans,dpoint))
    return add(num,divide(x,ans,dpoint))
'''
    x = minus(1,x)
    ans = 0
    for i in range(2,dpoint):
        l.append(divide(1,i,dpoint))
    ans = horners(l,x,0,dpoint)
    return minus(num,ans)
'''
def exp(x,n=10,dpoint=10):
    ans = listadd([n,1,x])
    for i in range(intify(n)):
        a = minus(n,i)
        ans = listadd([a,x,neg(divide(multiply(x,a,dpoint),ans,dpoint))])
    return divide(1,minus(1,divide(x,ans,dpoint)),dpoint)


def power(a,b,dpoint=10):
    if isint(b):
        l = ''
        num = b
        a1 = a
        while num != '1':
            if mod(num,2) == '0':
                l = ''.join(('^',l))
                num = basicdivide(num,2)[0]
            else:
                l = ''.join(('*',l))
                num = minus(num,1)
        print(l)
        for i in range(len(l)):
            if l[i] == '*':
                a = multiply(a,a1)
            else:
                a = multiply(a,a)
        return a
    ans = 1
    l = []
    e = 2.71828182845904523536
    n = multiply(ln(a,dpoint),b,dpoint)
    for i in range(intify(floor(add(n,0.5)))):
        l.append(e)
        n = minus(n,1)
    d = exp(n,10,dpoint) 
    ans = betterlistmultiply(l,dpoint)
    ans = multiply(ans,d)
    
    
    return ans

    
def continuedfraction(l):
    if len(l) == 1:
        return 1/l[0]
    return l[0]+1/continuedfraction(l[1:])



    
def comparison(n1,n2):
    t1 = time.process_time()
    print(basicmultiplyv2(n1,n2))
    
    t2 = time.process_time()
    print(basicmultiplyv3(n1,n2))
    t3 = time.process_time()
    print(n1*n2)
    t4 = time.process_time()
    return t2-t1,t3-t2,t4-t3



'''

    
def factorial2(n):
    ans = 1
    for i in range(1,intify(add(n,1))):
        if i%100 == 0:
            print(i)
        ans = multiply(i,ans)
    return ans
    




def ex(x,terms):
    t1 = time.process_time()
    l = []
    for i in range(terms):
        l.append(divide(1,factorial2(i),intify(multiply(2,i))))
    n = horners(l,x,0)
    t2 = time.process_time()
    return n,t2-t1
        
def ex2(x,terms):
    c = 0
    for i in range(terms):
        c = add(c,divide(power(x,i),factorial(i),multiply(2,i)))
    return c
'''
