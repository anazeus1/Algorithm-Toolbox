def fib(n):
    a=1
    b=1
    if n==0:
        return 0
    elif n <3:
        return(1)
    else:
        for loop in range (n-2):
            c=a+b
            a=b
            b=c
    return(c)
n = int(input())
print(fib(n))