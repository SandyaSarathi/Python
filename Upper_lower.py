s=input()
s1=""
for i in s:
  if i.isupper():
    s1=s1+i.lower()
  else:
    s1=s1+i.upper()
print(s1)
