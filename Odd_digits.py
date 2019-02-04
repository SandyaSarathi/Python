n=input()
n1=[]
s=""
for i in n:
  n1.append(int(i))
for i in range(0,len(n1)):
  if (n1[i]%2!=0):
    s=s+str(n1[i])+" "
print(s.strip())
