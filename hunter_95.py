k=int(input())
l=[]
f=0
if k==2:
    l.append(str(0))
else:
    for i in range(2,k+1):
        for j in range(2,i+1):
            if ((i%j)==0) & (i!=j):
                f=1
                break
            else:
                f=0
        if f==0:
            l.append(str(i))
print(" ".join(l))
