n=int(input())
l=[int(x) for x in input().split()]
s=[]
for i in range(0,len(l)):
	l1=l[i:]
	m=max(l1)
	if l[i]==m:
		s.append(l[i])
print(*s)
print(max(l))
#s
