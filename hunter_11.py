s=input()
t=""
l=[]
for i in range(0,len(s)):
  if s[i]!=" ":
    t=t+s[i]
  else:
    l.append(t)
    t=""
l.append(t)
s1=""
for i in range(0,len(l)-1):
  s1=s1+l[i][::-1]+" "
print(s1+l[len(l)-1][::-1])

