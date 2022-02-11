from time import time

def huge(n,t):
    i=2
    no_period=True
    while i<n+1 and no_period:
        c=(t[i-1]+t[i-2])
        t.append(c%10)
        if c==1 and t[i-1]==0:
            return i-1
        else:
            i=i+1
    return -1
n = int(input())
t=[0,1]
l=huge(n,t)
if (t[len(t)-1])==1 and t[len(t)-2]==0:
    t.pop(len(t)-1)
    t.pop(len(t)-1)

if n==1:
    print(1)


elif l==-1:
    print(sum(t)%10)
else:
    a=0
    s=sum(t)*(n//l)
    for i in range (n%l+1):
        a+=t[i]
    print((s+a)%10)
