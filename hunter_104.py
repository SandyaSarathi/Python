n=list(input())
n=[int(i) for i in n]
s=0
l=[]
for i in n:
	s=s+i
	l.append(s)
print(sum(l))
	
