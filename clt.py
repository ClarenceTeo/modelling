import numpy as np
import random
import matplotlib.pyplot as plt

l = np.zeros(100000)
for i in range(100000):
    a = random.uniform(0,100)
    b = a**2
    l[i] = b

def samplemean(l,n):
    list1 = []
    for i in range(n):
        a = np.random.randint(1,len(l))
        list1.append(l[a])
    return sum(list1)/n
        
    
def distribution(l):
    size = len(l)
    list1 = np.zeros(1000)
    for i in range(1000):
        a = samplemean(l,1000)
        b = int(np.floor(a/10))
        list1[b] += 1
    plt.plot(sorted(l))
    plt.plot(list1)
    plt.show()

distribution(l)
