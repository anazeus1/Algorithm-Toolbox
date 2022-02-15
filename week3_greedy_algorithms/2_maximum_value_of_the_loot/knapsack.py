from audioop import reverse
import numpy
def knapsack(n,W):
    dict={}
    ratio=[]
    
    for i in range(n):
        l=[]
        a,b=map(int,input().split())
        ratio.append(a/b)
        dict[ratio[i]]=a,b
    ratio.sort()
    ratio.reverse()

    s=0
    i=0
    while  i <n and W>0:
        if dict[ratio[i]][1]<=W:
            
            s+= dict[ratio[i]][0]
            W-=dict[ratio[i]][1]
        else:
            

            s+= ratio[i]*W
            W=0
        i+=1
    return s

n,W=map(int,input().split())
print(knapsack(n,W))
