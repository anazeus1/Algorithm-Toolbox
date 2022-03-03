import random

def money_change(i,k):
    if i ==1 or i == 4 or i==3:
        return 1
    if i==2 :
        return 2
    else:
        return k+min(money_change(i-1,k),money_change(i-3,k),money_change(i-4,k))

def optimal(n):
    k=[i for i in range(n+1)]
    d={0:0,1:1,2:2}
    i=3
    while (i<=n):
        d[i]=[1500]
    
        for j in range(i):
            if k[i]==k[j]+3 :
                 d[i].append(d[j]+1)
                            
            elif k[i]==k[j]+4 :
                d[i].append(d[j]+1)
                
            elif k[i]==k[j]+1 :
                d[i].append(d[j]+1)
        a = min(d[i])
        d[i] = a
        i+=1
    return d[n]

n=int(input())
print(optimal(n))

