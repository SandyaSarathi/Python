n=int(input())
l=[]
t=[]
l1=[]
l=[int(i) for i in input().split()]
l1=l+l1
while(n>1):
  l=[int(i) for i in input().split()]
  l1=l+l1
  n=n-1
l1=sorted(l1)
for i in range(0,len(l1)-1):
  print(l1[i],end=" ")
print(l1[len(l1)-1])
