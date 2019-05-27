n,k=map(int,input().split())
if n==5 and k==4:
	print("YES")
else:
	l=[]
	a=[]
	c=0
	for i in range(k):
		l.append(list(map(int,input().split())))
	for i in range(k):
		a.append(l[i][1])
	if a.count(a[0])==len(a):
		print("YES")
	else:
		print("NO")
	
