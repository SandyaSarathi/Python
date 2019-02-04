n=input()
n1=[]
for i in n:
  n1.append(int(i))
for i in range(0,len(n1)-1):
  if n1[i]%2!=0:
    print(n1[i],end=" ")
if n1[len(n1)-1]%2!=0:
  print(n1[len(n1)-1])
