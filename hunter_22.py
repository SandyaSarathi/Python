n=int(input())
l=[int(i) for i in input().split()]
a=[]
p=1
for i in range(n):
	for j in range(n):
		if i!=j:
			p*=l[j]
	a.append(p)
	p=1
print(*a)
