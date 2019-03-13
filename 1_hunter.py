n=int(input())
l=[int(i) for i in input().split()]
l1=[]
for i in range(0,len(l)):
  for j in range(i+1,len(l)):
    if l[i]==l[j]:
      if l[i] not in l1:
        l1.append(l[i])
      break
l1=sorted(l1)
if len(l1)==0:
  print("unique")
else:
  for i in range(0,len(l1)-1):
    print(l1[i],end=" ")
  print(l1[len(l1)-1])
