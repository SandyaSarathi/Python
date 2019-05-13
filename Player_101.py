# your code goes here
n=int(input())
l=[int(i) for i in input().split()]
s=0
for i in range(1,len(l)):
	s+=l[i]
print(s)
