#sandya
t=input()
p=['/','%']
for i in t:
	if i in p:
		if(i=='/'):
			a=int(t.split(i)[0])
			b=int(t.split(i)[1])
			print(a//b)
		else:
			a=int(t.split(i)[0])
			b=int(t.split(i)[0])
			print(a%b)
