s=list(input())
t=list(input())
l=[]
for i in s:
	if i in t:
		t.remove(i)
	else:
		l.append(i)
print("".join(l))
