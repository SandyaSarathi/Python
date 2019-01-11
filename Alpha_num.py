s=input()
a,d=0,0
for i in s:
  if i.isalpha():
    a=1
  elif i.isdigit():
    d=1
  if (a==1) & (d==1):
    print("Yes")
    break
if (a==0) or (d==0):
  print("No")
