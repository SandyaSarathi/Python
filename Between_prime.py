#sandya
n,k=map(int,input().split(" "))
l=[]
for n in range(n+1,k):
  i=2
  while i<n:
    if n%i==0:
      break
    i=i+1
  if n==i:
    l.append(n)
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1])
