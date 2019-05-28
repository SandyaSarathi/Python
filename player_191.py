n=int(input())
l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=0
j=n-1
c=1
n=n-1
while n>=0:
	if l[i]==a[j]:
		c=1
	else:
		c=0
		break
	i+=1
	j-=1
	n-=1
print("yes" if c==1 else "no")
