s=input()
l=list(s)
f=0
for i in s:
  d=s.count(i)
  if d>1:
    if len(l)>=(d-1)+d:
      print("yes")
      f=0
      break
    else:
      print("no")
      break
  else:
    f=1
if f==1:
  print("yes")

