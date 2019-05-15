n,k=map(int,input().split())
l=[int(i) for i in input().split()]
t=l[0:n]
s=l[n:]
l=[ i for i in t if i in s]
print(*set(l))
