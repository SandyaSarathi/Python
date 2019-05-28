n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in l:
	if i<0:
		a.append(i)
print(sum(a))
