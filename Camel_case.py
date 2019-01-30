s=input()
t=""
if s[0].isupper():
  pass
else:
  t=t+s[0].upper()
for i in range(1,len(s)):
  if s[i]==" ":
    t=t+s[i]
    t=t+s[i+1].upper()
  else:
    t=t+s[i]
print(t)
