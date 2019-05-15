# your code goes here
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
l=l+t
print(*sorted(l))
