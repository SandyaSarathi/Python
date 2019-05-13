from collections import Counter
s=input()
s=list(s)
l=dict(Counter(s))
s=[]
for i in l:
  if l.get(i)<=1:
    s.append(i)
print("".join(s))
