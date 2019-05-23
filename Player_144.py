n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(n-1):
	if l[i+1]%l[i]==0:
		a.append(l[i+1])
print(*a)
