s=input()
l=[]
for i in range(len(s)):
	if s[i].isdigit():
		l.append(s[i-1]*(int(s[i])-1))
	else:
		l.append(s[i])
print("".join(l))
		
