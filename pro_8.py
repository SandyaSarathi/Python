import gcd from math
import reduce from functools
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
for i in range(l):
	a,b=t[i][0],t[i][1]
	g=reduce(gcd,l[a:b])
