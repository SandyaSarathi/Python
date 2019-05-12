n=int(input())
l=[int(i) for i in input().split()]
t=sorted(l)
r=t[::-1]
l=[]
i,j,n1=0,0,0
while n1!=n:
	if n1%2==0:
		l.append(str(r[i]))
		i=i+1
	else:
		l.append(str(t[j]))
		j=j+1
	n1+=1
print(" ".join(l))
		
	
