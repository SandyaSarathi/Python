n=int(input())
l=[int(i) for i in input().split()]
l1=[]
for i in range(0,len(l)):
  l1.append(max(l))
  k=l.index(max(l))
  del(l[k])
print(l1)
if any(l1)==0:
  print('0')
else:
  s=""
  for i in l1:
    s=s+str(i)
  print(s)
