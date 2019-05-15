n,k=map(str,input().split())
k=int(k)
i=0
n=list(n)
while k!=0:
	n.insert(i,n[len(n)-1])
	n.pop(len(n)-1)
	k=k-1
print("".join(n))

	
