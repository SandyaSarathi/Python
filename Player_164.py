n,k=map(int,input().split())
l=[int(i) for i in input().split()]
if k in l:
	print(k)
else:
	l.append(k)
	l.sort()
	a=l.index(k)
	print(l[a-1])
