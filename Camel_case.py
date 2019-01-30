s=input()
s=s.split(" ")
l=[]
for i in s:
  x=i[0].upper()+i[1:].lower()
  l.append(x)
print(" ".join(l))
