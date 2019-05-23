n,k=map(int,input().split())
l=[int(i) for i in input().split()]
l.append(k)
l=set(l)
l=list(sorted(l))
a=l.index(k)
print(l[a+1])
