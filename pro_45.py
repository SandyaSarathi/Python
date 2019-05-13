s=input()
if s==s[::-1]:
	print("yes")
else:
	a=s.strip("0")
	if a==a[::-1]:
		print("yes")
	else:
		a=s.lstrip("0")
		if a==a[::-1]:
			print("yes")
		else:
			print("no")
