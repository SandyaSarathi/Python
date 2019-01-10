s=input()
l=list(s)
f=1
for i in l:
  if i==".":
    pass
  elif i.isdigit():
    pass
  else:
    f=0
    break
if f==1:
  print("yes")
else:
  print("no")
