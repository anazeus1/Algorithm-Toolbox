def money_change(n):
    s=0
    while n>0:
        if n>=10:
            s+= n//10
            n= n%10
        elif n>=5:
             s+=n//5
             n= n%5
        else:
            s+=n
            n= 0
    return s

n= int(input())
print(money_change(n))
