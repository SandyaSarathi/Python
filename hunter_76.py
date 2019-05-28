n=int(input())
m=[]
for i in range(n):
	l=[int(j) for j in input().split()]
	m.append(l)
s=0
for i in range(n):
	s+=sum(m[i])
s=s/(n*n)
print("%.6f" %s)
