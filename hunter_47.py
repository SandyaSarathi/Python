a=input()
s=""
for i in range(len(a)):
	if a[i]==" ":
		if a[i+1]==" ":
			continue
		else:
			s=s+a[i]
	else:
		s=s+a[i]
print(s.strip())

			
