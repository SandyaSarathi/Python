n,k=map(int,input().split())
if n==1 and k==0:
	print("YES")
else:
	l=[]
	for i in range(k):
		l.append(list(map(int,input().split())))
	s=0
	d={}
	for i in range(len(l)):
		if l[i][0] in d:
			d[l[i][0]]+=l[i][1]
		else:
			s=s+l[i][1]
			d[l[i][0]]=s
			s=0
	l=d.keys()
	c=0
	for i in d:
		if d[i]==i:
			print("YES")
			c=1
			break
	if c==0:
		print("NO")
