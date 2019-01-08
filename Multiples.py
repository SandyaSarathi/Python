n=int(input())
l=[]
for i in range(1,6):
  l.append(n*i)
k=[print(l[i],end=" ") for i in range(0,len(l)-1)]
print(l[len(l)-1])
