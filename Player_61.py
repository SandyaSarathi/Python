n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			print("yes")
			break
