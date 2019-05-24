s,t=map(str,input().split())
s=list(s)
t=list(t)
m=min(len(s),len(t))
c=0
for i in range(m):
	if s[i]!=t[i]:
		s[i]=t[i]
		c+=1
print(c+abs(len(t)-len(s)))
