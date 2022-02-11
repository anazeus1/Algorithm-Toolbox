from time import time


import time
def fib(n):
    a=1
    b=1
    if n==0:
        return 0
    elif n <3:
        return(1)
    else:
        for loop in range (n-2):
            c=a%10+b%10
            a=b%10
            b=c%10

    d=c%10
    return(d)
print(fib(int(input())))