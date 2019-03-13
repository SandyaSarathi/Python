n=int(input())
l=[int(i) for i in input().split()]
l1=[]
for i in range(0,len(l)):
  if l[i]==i:
    l1.append(i)
if len(l1)==0:
  print("-1")
else:
  for i in range(0,len(l1)-1):
    print(l1[i],end=" ")
  print(l1[len(l1)-1])
