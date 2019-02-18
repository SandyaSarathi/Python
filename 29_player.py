a,b=map(int,input().split())
c=0
for i in range(a,b):
  s=i**0.5
  if s==int(s):
    c=c+1
print(c)
    

