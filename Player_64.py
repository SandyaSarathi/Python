n,k=map(int,input().split())
l=[int(i) for i in input().split()]
a=[]
for i in l:
	if i<k:
		a.append(str(i))
print(" ".join(sorted(a)))
