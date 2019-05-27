n=int(input())
l=[int(i) for i in input().split()]
a,b=map(int,input().split())
i=l.index(a)
j=l.index(b)
print(abs(i-j))
	
