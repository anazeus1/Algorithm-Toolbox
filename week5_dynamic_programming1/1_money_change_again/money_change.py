n = int(input())
k=[i for i in range(n+1)]
d={0:0,1:1,2:2}
i=3
while (i<=n):
    d[i]=[150]
 
    for j in range(i):
    
    
        if k[i]==k[j]+3 :
          
            d[i].append(d[j]+1)
            
                        
        elif k[i]==k[j]+4 :
            
            d[i].append(d[j]+1)
        
            
            
            
        elif k[i]==k[j]+1 :
            
            d[i].append(d[j]+1)

    a = min(d[i])

   
    d[i] = a
        
        
    
    i+=1
print(d[n])
