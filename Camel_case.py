s=input()
s=s.split(" ")
for i in s:
  print(i[0].upper()+i[1:].lower(),end=" ")
