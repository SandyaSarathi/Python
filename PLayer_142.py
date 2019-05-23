n,k=map(int,input().split())
l=[]
for i in range(n):
	l.append(input())
c=0
for i in range(n-k+1):
	t=l[i:k+1]
	for j in t:
		if j==l[i]:
			c=1
		else:
			c=0
			break
	if c==1:
		print("yes")
		break
if c==0:
	print("no")
	
	
