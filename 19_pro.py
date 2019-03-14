n=int(input())
l=[int(i) for i in input().split()]
l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
l3=l1+l2+l
l3=sorted(l3)
for i in range(0,len(l3)-1):
  print(l3[i],end=" ")
print(l3[len(l3)-1])

