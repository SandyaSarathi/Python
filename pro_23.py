s=input()
c=0
for i in s:
	if i=='G':
		c+=1
	elif i=='L':
		c-=1
	elif i=='R':
		c-=2
print("yes" if c==1 else "no")
