l=list(input().split())
for i in range(len(l)):
	l[i]=sorted(l[i])
print(*l)
