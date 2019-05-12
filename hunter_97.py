n,k= map(int,input().split())
m = min(n,k)
c=0
for i in range(1,m+1):
    if(n%i == 0 and k%i == 0):
        c+=1
if(c== 1):
    print("yes")
else:
    print("no")
