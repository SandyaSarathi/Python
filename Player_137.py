n=int(input())
b=bin(n)
b=b[2:]
b=str(b[::-1])
for i in b:
	if i=='1':
		print(b.index(i)+1)
		break
