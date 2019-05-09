s=input()
t=""
l=[]
for i in range(0,len(s)):
  if s[i]!=" ":
    t=t+s[i]
  else:
    l.append(t)
    print(l)
    t=""
l.append(t)
s1=""
for i in range(0,len(l)):
  s1=s1+l[i][::-1]+" "
print(s1)

