def huge(m,n,t):
    i=2
    no_period=True
    while i<n+1 and no_period:
        c=(t[i-1]+t[i-2])
        t.append(c%m)
        if c==1 and t[i-1]==0:
            return i-1
        else:
            i=i+1
    return -1

n,m=map(int,input().split())
t=[0,1]
l=huge(m,n,t)
if n==0:
    print(0)
else:
    if l==-1:
        print(t[n])
    else:
        k=n%l
        print(t[k])

    




