import numpy as np
import matplotlib.pyplot as plt
import random
from random import *



def selectionsort(x,y):
    x1 = []
    y1 = []
    for i in range(len(x)):
        k = x.index(min(x))
        x1.append(x[k])
        y1.append(y[k])
        x.pop(k)
        y.pop(k)
    return x1,y1

def fit(x,y,deg):
    x,y = selectionsort(x,y)
    x = np.array([x])
    
    A = np.array([np.add(np.zeros(len(y)),1)])
    for i in range(1,deg+1):
        n = np.power(x,i)
        A = np.concatenate((A,n),axis=0)
    
    ata = np.linalg.inv(np.matmul(A,np.transpose(A)))
    aty = np.matmul(A,y)
    u = np.matmul(ata,aty)
    fl = [float(i) for i in u]
    print(u)
    print(fl)
    def f(x):
        
        ans = 0
        for i in range(deg+1):
            ans += u[i]*np.power(x,i)
        return ans
        
    c = np.linspace(min(x[0]),max(x[0]),1000)
    d = np.zeros(1000)
    for i in range(1000):
        d[i] = f(c[i])

    plt.plot(c,d,c='blue')
    '''
    for i in range(len(y)):
        plt.plot(x[0][i],y[i],marker='o',c='red')
        '''
    plt.plot(x[0],y,c='red')
    plt.show()
    


print(fit([1,2,3,4,5,6,7,8,9,10],[1,22,30,29,24,18,13,10,7,3],4))




