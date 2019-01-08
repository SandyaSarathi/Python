#sandya
n=int(input())
k=int(input())
l=[]
for i in range(0,n):
  l.append(int(input()))
j=0
s=0
while (j<k):
    s=s+l[j]
    j=j+1
print(s)
    
