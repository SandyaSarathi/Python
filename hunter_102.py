a=list(input())
a=[int(i) for i in a]
l=[]
for i in a:
	l.append(i*i)
print(sum(l))
