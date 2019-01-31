n,k=map(int,input().split())
c=0
f=0
for i in range(n,k+1):
    for j in range(2,i+1):
        if ((i%j)==0) & (i!=j):
            f=1
            break
        else:
            f=0
    if f==0:
        c=c+1
print(c)
