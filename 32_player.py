#sandya
n,k=map(int,input().split())
f=0
l=[int(i) for i in input().split()]
for i in l:
  if i==k:
    f=1
if f==1:
  print("Yes")
else:
  print("No")
