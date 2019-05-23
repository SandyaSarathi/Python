s=input()
t=input()
a=s+t
c=1
for i in a:
	if a.count(i)==1:
		c=1
	else:
		c=0
print("complementary" if ((c==1) and (len(a)==26)) else "non-complementary")
