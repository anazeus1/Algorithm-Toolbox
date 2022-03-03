
n = int(input())

num_op=[0,0]+[1000000]*(n-1)
intermediate_numbers=[n]
for i in range(2,n+1):
    a=1000000
    b=1000000
    c=1000000

    a= num_op[i-1]+1
    if i%2==0:
        b= num_op[i//2]+1
    if i%3==0:
        c= num_op[i//3]+1
    num_op[i]= min(a,b,c)
nb=num_op[n]

while n>1:
    if n%3==0 and num_op[n]-1==num_op[n//3]:
        intermediate_numbers.append(int(n/3))
        n=n//3
    elif n%2==0 and num_op[n]-1==num_op[n//2]:
        intermediate_numbers.append(int(n/2))
        n=n//2

    else:
        intermediate_numbers.append(int(n-1))
        n=n-1

print(nb)
for i in range(nb,-1,-1):

    print(intermediate_numbers[i],end=" ")