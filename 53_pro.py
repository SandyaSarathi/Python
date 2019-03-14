s=input()
s=s.lower()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l1=list(str(s))
t=l1
for i in range(len(t)-1,-1,-1):
  if t[i] in l:
    l.remove(t[i])
if len(l)==0:
  print("yes")
else:
  print("no")
