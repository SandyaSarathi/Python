a,b=map(int,input().split())
l=[int(i) for i in input().split()]
i=len(l)-1
j=0
while(i>=b):
  l.insert(len(l),l[j])
  del(l[j])
  i=i-1
print(*l)
