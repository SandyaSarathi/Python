a,b=map(int,input().split())
l=[int(i) for i in input().split()]
i=1
j=len(l)-1
while(i<=b):
  l.insert(0,l[j])
  i=i+1
i=len(l)-1
while(i>=a):
  del(l[i])
  i=i-1
print(*l)
