n,k=input().split()
c=0
for i in range(0,len(n)):
    if n[i]!=k[i]:
        c=c+1
if c>1:
    print("no")
else:
    print("yes")
