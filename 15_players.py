#sandya
s=input()
l=[]
l1=[]
c=1
for i in range(0,len(s)):
  for j in range(i+1,len(s)):
    if s[i]==s[j]:
      c=c+1
  l.append(c)
  l1.append(s[i])
  c=1
m=l.index(max(l))
print(l1[m])

