s,t=map(str,input().split())
s=list(s)
t=list(t)
c=0
for i in range(len(s)):
	if s[i]!=t[i]:
		s[i]=t[i]
		c+=1
print(c+len(t)-len(s))
		
