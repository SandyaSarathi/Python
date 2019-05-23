# your code goes here
s=input()
i=0
k=""
j=i+1
c=1
while j<len(s):
	if s[i]==s[j]:
		c=c+1
	else:
		k=k+s[i]+str(c)
		i=j
		c=1
 
	j=j+1
k=k+s[i]+str(c)
print(k)
