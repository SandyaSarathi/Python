s=list(input().split())
l=[s[0]]
if len(s)==1:
	print(*l)
else:
	for i in range(1,len(s)-1):
		l.append(s[i][::-1])
	l.append(s[len(s)-1])
	print(*l)
	
	
