n=int(input())
t=n
s=0
while(t!=0):
  r=t%10
  t=t//10
  s=s+r
print(s)
