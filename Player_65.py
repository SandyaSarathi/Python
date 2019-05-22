n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in l:
	if i<n:
		a.append(str(i))
print(" ".join(sorted(a)))
