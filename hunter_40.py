a=list(input())
a=[int(i) for i in a]
s=sum(a)
s=str(s)
if s==s[::-1]:
	print("YES")
else:
	print("NO")
