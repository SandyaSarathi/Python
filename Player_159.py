n,k=map(int,input().split())
b=str(bin(n*k)[2:])
print(b.count('1'))
