n=int(input())
s=input()
l=['a','e','i','o','u']
s1=""
for i in s:
  if i.lower() in l:
    pass
  else:
    s1=s1+i
print(s1[::-1])
