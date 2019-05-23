n,k=map(int,input().split())
a=str(bin(n|k)[2:])
print(a.count('1'))
