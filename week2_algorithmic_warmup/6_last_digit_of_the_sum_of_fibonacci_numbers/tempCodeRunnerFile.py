
l=huge(n,t)

if (t[len(t)-1])==1 and t[len(t)-2]==0:
    t.pop(len(t)-1)
    t.pop(len(t)-1)

print(t)
if l==-1:
    print(sum(t)%10)
else:
    s=sum(t)*(n//l)