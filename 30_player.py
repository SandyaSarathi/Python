n,k,a=map(str,input().split())
a=int(a)
c=0
for i in range(0,len(n)):
  if n[i]!=k[i]:
    c=c+1
if c!=a:
  print("no")
else:
  print("yes")
