n=int(input())
l1=[]
l=[int(i) for i in input().split()]
for i in range(0,len(l)-1):
  if l[i]>l[i+1]:
    l1.append(l[i+1])
  else:
    l1.append(-1)
print(*l1,end=" ")
print(-1)


