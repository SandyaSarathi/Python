#sandy
s=input()
s1=list(s)
l=['d','h','o','n','i']
for i in s1:
  if i in l:
    l.remove(i)
    s1.remove(i)
if l and s1:
  print("no")
else:
  print("yes")
