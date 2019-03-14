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
l.reverse()
print(*l)
