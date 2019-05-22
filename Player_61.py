n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			break
		else:
			c=1
	if c==0:
		break
print("yes" if c==0 else "no")
	
