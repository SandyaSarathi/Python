#sandya
a=input()
k=[]
for x in a:
    if(x not in k):
        k.append(x)
k.reverse()
l="".join(map(str,k))
print(l)
