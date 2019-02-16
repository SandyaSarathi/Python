a,b=map(int,input().split())
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
if (a==a1==a2) or (b==b1==b2):
  print("yes")
elif (a==b) and (a1==b1) and (a2==b2):
  print("yes")
else:
  print("no")
