n,k=map(str,input().split())
k=int(k)
i=0
n=list(n)
while k!=0:
	n.append(n[i])
	n.pop(i)
	k=k-1
print("".join(n))

	
