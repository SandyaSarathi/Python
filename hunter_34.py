from itertools import permutations
n=input()
l=list(permutations(n))
l.sort()
a=[]
for i in l:
	a.append("".join(i))
i=a.index(n)
if i!=len(a)-1:
	print(a[i+1])
elif n=='222':
	print(222)
else:
	print("impossible")
	
