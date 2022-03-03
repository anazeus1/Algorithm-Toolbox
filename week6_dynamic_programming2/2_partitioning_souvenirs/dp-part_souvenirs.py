
def part_souvenirs(w, n, souvenirs):
    
    count = 0 
    value =[ [0 for i in range(n+1)]for i in range(w+1)]

    for i in range(1, w+1):
        for j in range(1, n+1):

            value[i][j] = value[i][j-1]

            if souvenirs[j-1]<=i:

                temp = value[i-souvenirs[j-1]][j-1] + souvenirs[j-1]
                if temp > value[i][j]:
                
                    value[i][j] = temp

            if value[i][j] == w: 
                count += 1

    if count < 3: 
        return 0
    else: 
        return 1
n= int(input())
souvenirs=[int(i) for i in input().split()]
w= sum(souvenirs)
if n<3 or  w%3 != 0:
    print('0')
else:
    print(part_souvenirs(w//3,n,souvenirs))