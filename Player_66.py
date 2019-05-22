n,k=map(int,input().split())
l=[i for i in input().split()]
for i in l:
	if l.count(str(i))==k:
		print(i)
		break
