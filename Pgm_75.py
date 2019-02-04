s=input()
n=len(s)
s1=""
if n%2!=0:
  for i in range(0,len(s)):
    if i!=(n//2):
      s1=s1+s[i]
    else:
      s1=s1+"*"
else:
  for i in range(0,len(s)):
    if (i+1!=n//2) and (i!=n//2):
      s1=s1+s[i]
    else:
      s1=s1+"*"
    i=i+2
print(s1)
