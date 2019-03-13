k=int(input())
n=2
l=[]
l1=[]
for n in range(n,k+1):
  i=2
  while i<n:
    if n%i==0:
      break
    i=i+1
  if n==i:
    l.append(n)
for i in l:
  if k%i==0:
    l1.append(i)
for i in range(0,len(l1)-1):
  print(l1[i],end=" ")
print(l1[len(l1)-1])
