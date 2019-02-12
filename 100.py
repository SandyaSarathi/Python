n=int(input())
s=1
t=n
while t!=0:
    r=t%10
    s=s*r
    t=t//10
print(s)
