s=input()
c=0
t=""
for i in range(len(s)-1):
	if s[i].isdigit() and c==0:
		t+=s[i]
		c+=1
	elif s[i].isdigit() and s[i+1].isdigit():
		t+=s[i-1]*(int(s[i]+s[i+1])-1)
		if i+1==len(s)-1:
			c=1
	elif s[i].isdigit():
		t+=s[i-1]*(int(s[i])-1)
	else:
		t+=s[i]
if s[len(s)-1].isdigit() :
	t+=s[len(s)-2]*(int(s[len(s)-1])-1)
print(t)		
