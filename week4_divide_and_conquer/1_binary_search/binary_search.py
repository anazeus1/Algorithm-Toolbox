n=int(input())
t=[int(i) for i in input().split()]
d={
    t[0]:0
}
for i in range(1,n):
    if(t[i]!=t[i-1]):
        d[t[i]]=i

m= int(input())

k=[int(i) for i in input().split()]
def binary_search(t,l,begin,end):

    n= (begin+end)//2



    if begin>end:
        return -1
    elif t[n]==l:

        return n
    else:
        if():
            return binary_search(t,l,n+1,end)
        else:
            return binary_search(t,l,begin,n-1)
def dup(a,b):
    if a==b:
        return
for i in range(m):

    a= binary_search(t,k[i],0,n-1)
    if a!=-1:
        print(d[k[i]],end=" ")
    else:
        print(-1,end=" ")

