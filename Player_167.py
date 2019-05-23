#san
a=input()
c=0
prime=0
for i in range(0,len(a)):
    if a[i]!=" ":
        c=c+1
for i in range(2,c):
    if c%i==0:
        prime=prime+1 
        break
if prime >0:
    print("no")
else:
    print("yes")
