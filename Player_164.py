n,k=map(int,input().split())
l=[int(i) for i in input().split()]
if k in l:
	print(k)
else:
	for i in l:
		if i<k:
			print(i)
			break
