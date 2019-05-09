a=list(input())
a=[int(i) for i in a]
s=0
for i in range(len(a)):
	s=s+a[i]**i
print(s)
