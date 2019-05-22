n=list(map(int,input().split()))
k=n[len(n)-1]
l=[i for i in input().split()]
for i in l:
	if l.count(str(i))==k:
		print(i)
		break
