d=int(input())
m=int(input())
n=int(input())

t=[int(i)for i in input().split()]


def refill(d,m,n,t):
    current=0
    nb=0
    last=0
    if m>d:
        return 0
    
    while current<n-1 and current<d :
        last=current
        
        
        while t[current+1]-t[last]<=m and current<n-2:
            current+=1
            print(current)
        if current==last:
            return -1
        if current<n-1:
        
            nb+=1
    return(nb)
print(refill(d,m,n,t))