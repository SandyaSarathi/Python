s=input()
s1=list(s)
t=s1
l=['d','h','o','n','i']
if len(s1)>len(l):
  print("no")
else:
  for i in range(0,len(s1)):
    if l[i] in s1:
      t.remove(l[i])
      l[i]=0
  if len(l)!=l.count(0):
    print("no")
  else:
    print("yes")
