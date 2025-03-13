

def intify(n):
    k = str(n)
    try:
        return int(k)
    except Exception:
        if k[-1] == '.':
            return int(k[:-1])
        if k[-1] == '0' and k[-2] == '.':
            return int(k[:-2])
        return False

def isint(n):
    if intify(n) == False:
        return False
    else:
        return True
    
def stringintify(n):
    return str(intify(n))

def isneg(n):
    n = str(n)
    if n[0] == '-':
        return True
    else:
        return False
#obliterates nth element of a string
def obliterate(l,n):
    if n == -1:
        l = l[:-1]
    else:
        l = ''.join((l[:n],l[n+1:]))
    return l

def create(l,e,n):
    if n == -1:
        l = ''.join((l,e))
        return l
    else:
        l = ''.join((l[:n+1],e,l[n+1:]))
        return l
                
def neg(n):
    n = str(n)
    if isneg(n):
        n = n[1:]
    else:
        n = ''.join(('-',n))
    return n

#seperates number into digits before and after the decimal dot
def seperate(n):
    if not(isinstance(n,str)):
        n = str(n)
    before = n.index('.')
    after = threeminus(threeminus(len(n),before),1)
    return n[:before],before,n[before+1:],after

def max(a,b):
    if threeminus(a,b)[0] == '-':
        return b,1
    else:
        return a,0

def maxi(a,b):
    if minus(a,b)[0] == '-':
        return b,1
    else:
        return a,0
    
def mini(a,b):
    if minus(a,b)[0] == '-':
        return a,0
    else:
        return b,1
    
def floor(n):
    if not(isinstance(n,str)):
        n = str(n)
    before = n.index('.')
    return n[:before]
    

    
def baseadd(a,b):
    a,b = intify(a),intify(b)
    m = [[0,1,2,3,4,5,6,7,8,9],
         [1,2,3,4,5,6,7,8,9,0],
         [2,3,4,5,6,7,8,9,0,1],
         [3,4,5,6,7,8,9,0,1,2],
         [4,5,6,7,8,9,0,1,2,3],
         [5,6,7,8,9,0,1,2,3,4],
         [6,7,8,9,0,1,2,3,4,5],
         [7,8,9,0,1,2,3,4,5,6],
         [8,9,0,1,2,3,4,5,6,7],
         [9,0,1,2,3,4,5,6,7,8]]
    
    r = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,0,1,1,1],
         [0,0,0,0,0,0,1,1,1,1],
         [0,0,0,0,0,1,1,1,1,1],
         [0,0,0,0,1,1,1,1,1,1],
         [0,0,0,1,1,1,1,1,1,1],
         [0,0,1,1,1,1,1,1,1,1],
         [0,1,1,1,1,1,1,1,1,1]]

    return m[a][b],r[a][b]
    
def baseminus(a,b):
    a,b = intify(a),intify(b)
    m = [[0,9,8,7,6,5,4,3,2,1],
         [1,0,9,8,7,6,5,4,3,2],
         [2,1,0,9,8,7,6,5,4,3],
         [3,2,1,0,9,8,7,6,5,4],
         [4,3,2,1,0,9,8,7,6,5],
         [5,4,3,2,1,0,9,8,7,6],
         [6,5,4,3,2,1,0,9,8,7],
         [7,6,5,4,3,2,1,0,9,8],
         [8,7,6,5,4,3,2,1,0,9],
         [9,8,7,6,5,4,3,2,1,0]]

    r = [[0,1,1,1,1,1,1,1,1,1],
         [0,0,1,1,1,1,1,1,1,1],
         [0,0,0,1,1,1,1,1,1,1],
         [0,0,0,0,1,1,1,1,1,1],
         [0,0,0,0,0,1,1,1,1,1],
         [0,0,0,0,0,0,1,1,1,1],
         [0,0,0,0,0,0,0,1,1,1],
         [0,0,0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0,0,0]]

    return m[a][b],r[a][b]

def basemultiply(a,b):
    a,b = intify(a),intify(b)
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,1,2,3,4,5,6,7,8,9],
         [0,2,4,6,8,0,2,4,6,8],
         [0,3,6,9,2,5,8,1,4,7],
         [0,4,8,2,6,0,4,8,2,6],
         [0,5,0,5,0,5,0,5,0,5],
         [0,6,2,8,4,0,6,2,8,4],
         [0,7,4,1,8,5,2,9,6,3],
         [0,8,6,4,2,0,8,6,4,2],
         [0,9,8,7,6,5,4,3,2,1]]

    r = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,1,1,1,1],
         [0,0,0,0,1,1,1,2,2,2],
         [0,0,0,1,1,2,2,2,3,3],
         [0,0,1,1,2,2,3,3,4,4],
         [0,0,1,1,2,3,3,4,4,5],
         [0,0,1,2,2,3,4,4,5,6],
         [0,0,1,2,3,4,4,5,6,7],
         [0,0,1,2,3,4,5,6,7,8]]

    return m[a][b],r[a][b]


def threeminus(a,b):
    a,b,c,remainder = stringintify(a),stringintify(b),'',0
    for i in range(baseminus(3,len(a))[0]):
        a = ''.join(('0',a))
    for i in range(baseminus(3,len(b))[0]):
        b = ''.join(('0',b))
    for i in range(1,4): 
        n = baseminus(a[-i],b[-i])
        num = baseminus(n[0],remainder)
        c = ''.join((str(num[0]),c))
        remainder = n[1]+num[1]
    if remainder == 1:
        c = ''.join(('-',c))
        return stringintify(c)
    else:
        return stringintify(c)



def basicadd(a,b):
    a,b,c = str(a),str(b),''
    if '.' not in a:
        a = ''.join((a,'.0'))
    if '.' not in b:
        b = ''.join((b,'.0'))
    n1,n2 = seperate(a),seperate(b)
    #aligns the 2 numbers for addition
    m1 = max(n1[1],n2[1])
    if m1[1] == 0:
        for i in range(intify(threeminus(n1[1],n2[1]))):
            b = ''.join(('0',b))
    else:
        for i in range(intify(threeminus(n2[1],n1[1]))):
            a = ''.join(('0',a))
    m2 = max(n1[3],n2[3])
    if m2[1] == 0:
        for i in range(intify(threeminus(n1[3],n2[3]))):
            b = ''.join((b,'0'))
    else:
        for i in range(intify(threeminus(n2[3],n1[3]))):
            a = ''.join((a,'0'))
    remainder = 0
    for i in range(1,len(a)+1):
        if a[-i] == '.':
            c = ''.join(('.',c))
        else:
            n = baseadd(a[-i],b[-i])
            num = baseadd(n[0],remainder)
            c = ''.join((str(num[0]),c))
            remainder = baseadd(n[1],num[1])[0]
    if remainder == 1:
        c = ''.join(('1',c))
    return c


def basicminus(a,b):
    a,b,c = str(a),str(b),''
    if '.' not in a:
        a = ''.join((a,'.0'))
    if '.' not in b:
        b = ''.join((b,'.0'))
    n1,n2 = seperate(a),seperate(b)
    #aligns the 2 numbers for addition
    m1 = max(n1[1],n2[1])
    if m1[1] == 0:
        for i in range(intify(threeminus(n1[1],n2[1]))):
            b = ''.join(('0',b))
    else:
        for i in range(intify(threeminus(n2[1],n1[1]))):
            a = ''.join(('0',a))
    m2 = max(n1[3],n2[3])
    if m2[1] == 0:
        for i in range(intify(threeminus(n1[3],n2[3]))):
            b = ''.join((b,'0'))
    else:
        for i in range(intify(threeminus(n2[3],n1[3]))):
            a = ''.join((a,'0'))
    remainder = 0
    for i in range(1,len(a)+1):
        if a[-i] == '.':
            c = ''.join(('.',c))
        else:
            n = baseminus(a[-i],b[-i])
            num = baseminus(n[0],remainder)
            c = ''.join((str(num[0]),c))
            remainder = baseadd(n[1],num[1])[0]
    #if the answer is neg
    if remainder == 1:
        c = ''
        remainder = 0
        for i in range(1,len(a)+1):
            if a[-i] == '.':
                c = ''.join(('.',c))
            else:
                n = baseminus(b[-i],a[-i])
                num = baseminus(n[0],remainder)
                c = ''.join((str(num[0]),c))
                remainder = baseadd(n[1],num[1])[0]
        while c[0] == '0' and c[1] != '.':
            c = obliterate(c,0)
        return neg(c)
    while c[0] == '0' and c[1] != '.':
        c = obliterate(c,0)
    return c


def basicmultiply(a,b):
    a,b,c = str(a),str(b),''
    remainder = 0
    for i in range(len(a)):
        n = basemultiply(a[-i-1],b)
        if isneg(stringintify(listadd([n[0],remainder,-10]))):
            num = stringintify(add(n[0],remainder))
            c = ''.join((num,c))
            remainder = 0
        else:
            num = stringintify(listadd([n[0],remainder,-10]))
            c = ''.join((num,c))
            remainder = 1
        remainder = intify(add(remainder,n[1]))
    remainder = stringintify(remainder)
    c = ''.join((remainder,c))
    return str(c)


def basicmultiplyv2(a,b,dpoint):
    l = []
    a,b,c = str(a),str(b),''
    if '.' not in a:
        a = ''.join((a,'.0'))
    if '.' not in b:
        b = ''.join((b,'.0'))
    n1,n2 = seperate(a),seperate(b)
    deci = intify(add(n1[3],n2[3]))
    try:
        a = obliterate(a,n1[1])
    except Exception:
        a = stringintify(a)
    try:
        b = obliterate(b,n2[1])
    except Exception:
        b = stringintify(b)
    while a[-1] == '0':
        a = obliterate(a,-1)
        deci = minus(deci,1)
    while b[-1] == '0':
        b = obliterate(b,-1)
        deci = minus(deci,1)
    while a[0] == '0':
        a = obliterate(a,0)
    while b[0] == '0':
        b = obliterate(b,0)
    for i in range(len(b)):
        n = basicmultiply(a,b[-i-1])
        for j in range(i):
            n = ''.join((stringintify(n),'0'))
        l.append(n)
    c = listadd(l)
    c = stringintify(c)
    if isneg(deci):
        for i in range(intify(neg(deci))):
            c = create(c,'0',-1)
            deci = add(deci,1)
    elif deci != '0':
        for i in range(intify(deci)):
            c = ''.join(('0',c))
    while isneg(minus(dpoint,deci)) or c[-1] == 0:
        c = obliterate(c,-1)
        deci = minus(deci,1)
    deci = intify(neg(add(deci,1)))
    c = create(c,'.',deci)
    while c[0] == '0' and c[1] != '.':
        c = obliterate(c,0)
    return c


def basicdivide(a,b):
    a = stringintify(a)
    b = stringintify(b)
    if a == b:
        return '1','0'
    if isneg(minus(a,b)):
        return '0',a
    n = ''.join((b,'0'))
    num = ''
    ans = ''
    bool = 0
    for i in range(len(a)):
        num = ''.join((num,a[i]))
        if not(isneg(minus(num,b))) and isneg(minus(num,n)):
            bool = 1
        if bool == 1:
            for j in range(10):
                
                num1 = intify(multiply(b,j+1))
                if isneg(minus(num,num1)):
                    ans = ''.join((ans,str(j)))
                    num = stringintify(add(b,minus(num,num1)))
                    break
    return str(ans),num

                    
def basicdividev2(a,b,dpoint):
    a1,b1 = a,b
    a,b,c = str(a),str(b),''
    if '.' not in a:
        a = ''.join((a,'.0'))
    if '.' not in b:
        b = ''.join((b,'.0'))
    l = []
    if a == b:
        return '1'
    n1,n2 = seperate(a),seperate(b)
    deci = minus(n2[3],n1[3])
    try:
        a = obliterate(a,n1[1])
    except Exception:
        a = stringintify(a)
    try:
        b = obliterate(b,n2[1])
    except Exception:
        b = stringintify(b)
    while a[-1] == '0':
        a = obliterate(a,-1)
        deci = add(deci,1)
    while b[-1] == '0':
        b = obliterate(b,-1)
        deci = minus(deci,1)
    while a[0] == '0':
        a = obliterate(a,0)
    while b[0] == '0':
        b = obliterate(b,0)
    #if a<b (answer in form 0.00....)
    if isneg(minus(a1,b1)):
        deci1 = listadd([dpoint,neg(deci),multiply(len(b),2),neg(len(a))])
        deci2 = listadd([dpoint,neg(deci),len(b),neg(len(a))])
        for i in range(mini(len(a),len(b))[0]):
            if b[i] == a[i]:
                continue
            if isneg(minus(b[i],a[i])):
                deci2 = minus(deci2,1)
                break
            else:
                break
        for i in range(intify(deci1)):
            a = ''.join((a,'0'))
        c = stringintify(basicdivide(a,b)[0])
        while isneg(minus(dpoint,len(c))):
            c = obliterate(c,-1)
        for i in range(intify(listadd([deci2,neg(dpoint),1]))):
            c = ''.join(('0',c))
        c = create(c,'.',0)
        return c
    #if a>b
    else:
        deci = listadd([deci,dpoint])
        for i in range(intify(deci)):
            a = ''.join((a,'0'))
        c = stringintify(basicdivide(a,b)[0])
        for i in range(intify(minus(dpoint,deci))):
            c = ''.join(('0',c))
        c = str(create(c,'.',intify(neg(add(1,dpoint)))))
        return c

    
def add(a,b):
    if not(isneg(a)):
        if not(isneg(b)):
            return basicadd(a,b)
        else:
            if neg(b) == str(a):
                return '0.0'
            return neg(basicminus(neg(b),a))
    else:
        if not(isneg(b)):
            if neg(a) == str(b):
                return '0.0'
            return basicminus(b,neg(a))
        else:
            return neg(basicadd(neg(a),neg(b)))


def minus(a,b):
    if not(isneg(a)):
        if not(isneg(b)):
            return basicminus(a,b)
        else:
            return basicadd(a,neg(b))
    else:
        if not(isneg(b)):
            return neg(basicadd(neg(a),b))
        else:
            return basicminus(neg(b),neg(a))


def multiply(a,b,dpoint=10):
    if stringintify(a) == '0' or stringintify(b) == '0':
        return '0.0'
    if not(isneg(a)):
        if not(isneg(b)):
            return basicmultiplyv2(a,b,dpoint)
        else:
            return neg(basicmultiplyv2(a,neg(b),dpoint))
    else:
        if not(isneg(b)):
            return neg(basicmultiplyv2(neg(a),b,dpoint))
        else:
            return basicmultiplyv2(neg(b),neg(a),dpoint)

def divide(a,b,dpoint=10):
    if str(a) == '0.0' or str(b) == '0.0':
        return '0.0'
    if not(isneg(a)):
        if not(isneg(b)):
            return basicdividev2(a,b,dpoint)
        else:
            return neg(basicdividev2(a,neg(b),dpoint))
    else:
        if not(isneg(b)):
            return neg(basicdividev2(neg(a),b,dpoint))
        else:
            return neg(basicdividev2(neg(b),neg(a),dpoint))

        

def listadd(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return add(l[0],l[1])
    else:
        return add(l[0],listadd(l[1:]))

def listmultiply(l,dpoint):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return multiply(l[0],l[1],dpoint)
    else:
        return multiply(l[0],listmultiply(l[1:],dpoint),dpoint)
