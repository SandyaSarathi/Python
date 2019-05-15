s=list(map(int,(input().split("/"))))
if len(s)!=8:
	print("no")
else:
	print("yes" if s[0]<=31 and s[1]<=12 else "no")
