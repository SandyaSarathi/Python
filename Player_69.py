n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(n-1,n-k-1,-1):
	l.remove(l[i])
print(*l)
