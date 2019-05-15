n=int(input())
l=[int(i) for i in input().split()]
t=[1 for i in range(n) for j in range(i+1,n) if l[i]<l[j]]
print(sum(t))
