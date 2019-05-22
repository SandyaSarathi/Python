#san
n=int(input())
l=list(map(int,input().split()))
m=max(l)
c=0
g=[]
for i in range(1,m+1):
    c=0
    for j in range(0,len(l)):
        if l[j]%i==0:
            c+=1
    if c==len(l):
        g.append(i)
s=max(g)
print(s)
