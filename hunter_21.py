n,k=map(int,input().split())
l=[]
for i in range(n):
    a=[x for x in input().split()]
    l.append(a)
for i in range(n):
	if '0' in l[i]:
		for j in range(k):
			l[i][j]=0
for i in range(n):
	print(*l[i])
