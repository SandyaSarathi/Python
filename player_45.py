p,a=map(int,input().split())
p1=int(p/2)
q1=int(a**0.5)
if(p1*2==p and q1*q1==a):
    print("yes")
else:
    print("no")
