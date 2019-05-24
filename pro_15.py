n=int(input())
l=[int(i) for i in input().split()]
l.sort(reverse=True)
for i in l:
	print(i)
