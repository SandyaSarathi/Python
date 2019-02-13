n=int(input())
l=[int(i) for i in input().split()]
j=0
for i in range(1,n+1):
  if l[j]!=i:
    print(j)
    break
  j=j+1
