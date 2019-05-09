a=list(input())
a=[int(i) for i in a]
s1=0
for i in range(len(a)):
	s1=s1+a[i]**i
print(s1)
