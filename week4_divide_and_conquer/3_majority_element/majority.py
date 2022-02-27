from collections import Counter
n=int(input())
t=[int(i) for i in input().split()]
dict={}

def majority(t):
    for item in t:
        dict[item]=dict.get(item,0)+1
       
        if dict[item]>n/2:
            return 1
   
    return 0
print(majority (t))
        





 


