s=input()
n=len(s)
s=list(map(int,s.split("/")))
if n!=10:
	print("no")
else:
	print("yes" if ((s[0]<=31) and (s[1]<=12)) else "no")
