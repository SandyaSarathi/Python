k,n=map(int,input().split())
for i in range(k,10000):
  if (i%n==0) & (i%k==0):
    print(i)
    break
