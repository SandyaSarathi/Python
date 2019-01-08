#sandya
n=int(input())
s=str(n)
c=len(s)
t=n
arm=0
while t!=0:
  print(t)
  rem=t%10
  t=t//10
  arm=arm+(rem**c)
  print(arm)
if n==arm:
  print("yes")
else:
  print("no")
    
