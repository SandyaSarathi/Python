n=int(input())
l=[int(i) for i in input().split()]
l.remove(min(l))
print(min(l))
