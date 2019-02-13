s=input()
s1=""
s1=s[0].upper()
i=1
while i<=len(s)-1:
  if s[i]==" ":
    s1=s1+" "+s[i+1].upper()
    i=i+2
  else:
    s1=s1+s[i]
    i=i+1
print(s1)
