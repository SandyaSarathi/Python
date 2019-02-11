s=input()
l=list(s)
l1=[]
f=0
for i in l:
    l1.append(i)
    l.remove(i)
    print(l)
    if i in l:
        f=1
        break
if f==1:
    print("No")
else:
    print("Yes")
    
