s=input()
l=['a','e','i','o','u']
a=[]
b=[]
for i in s:
	if i in l:
		a.append(i)
	else:
		b.append(i)
print("".join(a+b))
