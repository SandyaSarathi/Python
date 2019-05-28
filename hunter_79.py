n=int(input())
l=[int(i) for i in input().split()]
while n!=0:
	if n%2==0:
		a=int(n/2)
		b=a-1
		avg=(l[a]+l[b])//2
		print(avg)
		l.remove(l[a])
		l.remove(l[b])
		n=n-2
	else:
		a=(n//2)
		print(l[a])
		l.remove(l[a])
		n=n-1
