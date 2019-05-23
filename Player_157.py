n,k=map(int,input().split())
a=n*k
a=str(bin(a)[2:])
a=a[::-1]
for i in range(len(a)-1,-1,-1):
	if a[i]=='1':
		print(a.index(a[i])+1)
		break
