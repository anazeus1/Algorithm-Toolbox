A= [a for a in input()]
B= [a for a in input()]


d= [[0 for col in range(len(A)+1)] for row in range(len(B)+1)]


for i in range(len(B)+1):
    d[i][0]=i
    for j in range(len(A)+1):
        d[0][j]=j
for i in range(1,len(B)+1):
    
    for j in range(1,len(A)+1):
        delete = d[i][j-1]+1
        insert=d[i-1][j]+1
        mismatch=d[i-1][j-1]+1
        match=mismatch-1
        if A[j-1]==B[i-1]:
            d[i][j]=d[i-1][j-1]
        else:
            d[i][j]=min(mismatch,delete,insert)

print(d[len(B)][len(A)])




