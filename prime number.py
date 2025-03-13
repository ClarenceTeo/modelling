def sieve(n):
    l = []
    j = 0
    for i in range(2,n+1):
        l.append(i)
    while j<len(l):
        print(j,len(l))
        p = l[j]
        for i in range(2,n//p+2):
            try:
                l.remove(i*p)
            except Exception:
                pass
        j = j+1
    return l

print(sieve(100))
