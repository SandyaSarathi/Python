n,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=[i for i in l if i!=k]
if t:
	print(*t)
else:
	print("empty")
