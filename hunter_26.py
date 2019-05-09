n=int(input())
l=[int(i) for i in input().split()]
l=l[::-1]
for i in range(len(l)-1):
	print(str(l[i])+'->',end="")
print(l[len(l)-1])
