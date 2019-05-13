s,t=map(str,input().split())
t=list(t)
l=[]
for i in range(len(s)):
	if s[i] in t:
		l.append(s[i])
		t.remove(s[i])
if len(l)==0:
	print("no")
else:
	print("yes")
		
