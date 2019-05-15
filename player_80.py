n=int(input())
l=[int(i) for i in input().split()]
m1=min(l)
l.remove(m1)
print(min(l)-m1)
