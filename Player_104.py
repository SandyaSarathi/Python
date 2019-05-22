n=int(input())
l=[int(i) for i in input().split()]
s=0
for i in range(0,n-1):
	s=s+l[i]+l[i+1]
print(s)
