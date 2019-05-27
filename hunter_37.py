from itertools import combinations
s=input()
c=0
l=list(combinations(s,len(s)-1))
for i in range(len(l)):
	if l[i]==l[i][::-1]:
		print("YES")
		c=1
		break
if c==0:
	print("NO")
