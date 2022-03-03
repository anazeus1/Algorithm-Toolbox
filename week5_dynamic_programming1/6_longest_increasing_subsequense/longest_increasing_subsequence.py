
A=[1,2,1,5,6,25,3,25,0]
t=[]
def LIS_iterative(A):
    t=[None]*len(A)
    for i in range(len(A)):
        t[i]=1
        for j in range(i):
            if A[j]<A[i] and t[i]<t[j]+1 :
                t[i]=t[j]+1
    return(max(t))
T=dict()
def LIS_recursive(A,n):
    
    if A[n] not in T:
        T[A[n]]=1
        for j in range(n):
            if A[j]<A[n]:
                T[A[n]]=max(T[A[n]],LIS_recursive(A,j)+1)
    
    return T[A[n]]
    
print(max(LIS_recursive(A,i) for i in range(len(A))))
print(T)