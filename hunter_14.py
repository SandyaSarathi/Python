# your code goes here
from itertools import permutations
s=input()
s1=list(s)
l=list(permutations(s1))
l=set(l)
l=list(l)
t=""
for i in range(len(l)):
	for j in range(len(l[i])):
		t=t+l[i][j]
	print(t)
	t=""
