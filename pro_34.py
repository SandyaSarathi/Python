n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
	l.append(list(input()))
for i in range(n):
	for j in range(k-1):
		if l[i][j]=='R':
			if l[i][j+1]=='R':
				a=l[i].index('G')
				l[i][j+1]=l[i][a]
				l[i][a]=l[i][j]
				c+=5
			else:
				continue
		elif l[i][j]=='G':
			if l[i][j+1]=='G':
				a=l[i].index('R')
				l[i][j+1]=l[i][a]
				l[i][a]=l[i][j]
				c+=3
			else:
				continue
print(c)
