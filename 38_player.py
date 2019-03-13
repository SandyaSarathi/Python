n=int(input())
l=[]
l1=[]
for i in range(2,n+1):
  if n%i==0:
    l.append(i)
for i in l:
  if i%2==0:
    l1.append(i)
for i in range(0,len(l1)-1):
  print(l1[i],end=" ")
print(l1[len(l1)-1])
