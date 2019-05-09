n=int(input())
l1=[int(i) for i in input().split()]
l1=l1[::-1]
for i in range(len(l1)-1):
	print(str(l1[i])+'->',end="")
print(l1[len(l1)-1])
