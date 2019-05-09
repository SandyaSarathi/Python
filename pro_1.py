n=int(input())
s=[]
for i in range(n):
  s.append(input())
a=s[0]
f=0
s.pop(0)
for i in range(len(a)):
  for j in range(len(s)):
    if a[i]==s[j][i]:
      continue
    else:
      f=1
  if f==1:
    k=i
    print(a[0:k])
    break
if f==0:
  print(a[0:i+1])



