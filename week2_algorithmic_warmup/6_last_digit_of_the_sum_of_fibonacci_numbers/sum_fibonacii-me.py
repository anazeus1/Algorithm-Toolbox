from time import time


def fib(n):
    i=2
    t=[0,1]
    for i in range(2,n+1):
        c=(t[i-1]+t[i-2])%10
        t.append(c)
    return t
n=int(input())
if n==0:
    print(0)
else:
    print(sum(fib(n))%10)