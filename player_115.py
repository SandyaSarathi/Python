s,t=map(str,input().split())
s1=""
if len(s)!=len(t):
	s1=s[0:len(s)-1]+t
	print(s1)
else:
	s1=s+t
	print(s1)
