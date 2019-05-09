n=list(input())
n=[int(i) for i in n]
s=0
l=[]
for j in n:
	s=s+j
	l.append(s)
print(sum(l))
	
