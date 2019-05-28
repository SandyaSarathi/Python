l=list(input().split())
a=[]
for i in range(len(l)):
	a.append(sorted(l[i]))
s=""
for i in a:
	s+="".join(i)+" "
print(s.strip())
	
