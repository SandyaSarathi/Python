n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,len(l)):
  m=l[i]
  del(l[i])
  if m not in l:
    print(m)
    break

    

