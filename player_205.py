s=input()
t=""
for i in s:
	if i.isupper():
		t+=i.lower()
	else:
		t+=i.upper()
print(t)
