w,n =map(int,input().split())
t=[int(i) for i in input().split()]


def Knapsack(w, t,n):
    d = [[True] + [False] * w]
    for i in range(n):
        d.append(d[-1][:])
        for j in range(t[i], w + 1):
    
            d[-1][j] = d[-2][j] or d[-2][j - t[i]]
        
        d = d[-1:]
    for i in range(w, -1, -1):
      
        if d[-1][i]:
            return i
if n<3 or 
        print('0')
elif total_weight%3 != 0: 
        print('0')
else:
    print(Knapsack(w,t,n))