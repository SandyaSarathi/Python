#sandya
n=int(input())
s=input()
f=0
for i in range(0,len(s)):
  for j in range(i+1,len(s)):
    if s[i]==s[j]:
      f=1
      break
  if f==0:
    print(s[i])
  break
