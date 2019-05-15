n,k=map(int,input().split())
l=[int(i) for i in input().split()]
l="".join(str(l))
c=l.count(str(k))
if c!=0:
	print("yes",c)
else:
	print("no")
