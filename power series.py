from mpmath import *
import matplotlib.pyplot as plt

mp.dps=10
def sine(x,n):
    yes = mpf(0)
    for i in range(n):
        yes += ((-1)**i)*(mpf(x)**(2*i+1))/fac(2*i+1)
    return yes

def arctan(x,n):
    yes = mpf(0)
    for i in range(n):
        yes += ((-1)**i)*(mpf(x)**(2*i+1))/(2*i+1)
    return yes

def ex(x,n):
    yes = mpf(0)
    for i in range(n):
        yes += mpf(x)**i/fac(i)
    return yes

def ex3(x,n):
    x = mpf(x)
    n = mpf(n)
    ans = mpf(x+n+1)
    for i in range(int(n)):
        a = n-i

        ans = a+x-x*a/ans
    return 1/(1-x/ans)

def ln(x,n):
    ans = 0
    a = mpf(1-x)
    for i in range(1,n):
        ans += a**i/i
    return -ans

def ln2(x,n):
    num = 0
    while x>1.45:
        x = x/exp(1)
        num += 1
    x = x-1
    ans = mpf(n+1-n*x)
    for i in range(n):
        a = n-i
        print(a,ans)
        ans = a-(a-1)*x+a*a*x/ans
    print(x,ans,x/ans)
    return num+x/ans
        
    

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
domain = [0.5,1.5]
iterations = 200
n = 1
print(ln2(22.5,30))
'''
for i in range(iterations-2):
    k = (domain[1]-domain[0])*(i+1)/iterations+domain[0]
    diff = abs(log(k)-ln2(k,n))
    list4.append(i)
    while diff >= 0.00000000001:
        n+=1
        diff = abs(log(k)-ln2(k,n))
    list1.append(log(k))
    list2.append(ln2(k,n))
    list3.append(diff)
    list5.append(k)
    list6.append(n)
print(n)


plt.plot(list5,list6)
plt.show()
plt.plot(list4,list1,label='original')
plt.plot(list4,list2,label='approximation')
plt.legend(loc="upper right")
plt.show()
plt.plot(list4,list3,label='error')
plt.show()
'''
