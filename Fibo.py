n=int(input())
a=1
b=1
l=[]
if n>=1:
  l.append(b)
if n>1:
  l.append(a)
for i in range(2,n):
  f=a+b
  a=b
  b=f
  l.append(f)
for i in range(0,len(l)-1):
  print(l[i],end=" ")
print(l[len(l)-1])
