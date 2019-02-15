s=input()
l=list(s)
s1=""
for i in range(0,len(l)-1,2):
  s1=s1+l[i+1]+l[i]
print(s1)
