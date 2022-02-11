from random import randint


n = int(input())
t=[int(item)for item in input().split()]
"""for i in range(n):
    t.append(randint(2,200)*1000)#"""



def maxpair(t,n):
    
    Max1=0
    Max2=0
    for i in range (n):
        if t[i]>Max1:
            Max2=Max1
            Max1=t[i]

        elif t[i]>Max2:
            Max2= t[i]
    return(Max1*Max2)
print(maxpair(t,n))
