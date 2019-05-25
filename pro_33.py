from itertools import combinations
s=input()
l=[]
for i in range(len(s)):
	l.append(list(combinations(s,i)))
k=max(l)
print("".join(k[len(k)-1]))
