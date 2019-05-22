n1=int(input())
l=[int(x) for x in input().split()]
a=sorted(l)
b=[]
for i in range(0,len(a)):
	for j in range(len(a)):
		if l[i]==a[j]:
			b.append(j)
for i in range(len(b)):
	b[i]=b[i]+1
print(*b)
