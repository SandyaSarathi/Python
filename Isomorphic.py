#sandya
s,s1=map(str,input().split())
f=1
l=[]
l1=[]
if len(s)!=len(s1):
  print("no")
else:
  for i in range(0,len(s)):
    l.append(s[i])
    l1.append(s1[i])
    if l.count(l[i])==l1.count(l1[i]):
      pass
    else:
      f=0
      print("no")
      break
if f==1:
  print("yes")

  
