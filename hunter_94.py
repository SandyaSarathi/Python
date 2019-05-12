s=input()
l=list(s.split(" "))
t=[]
for i in range(len(l)):
	t.append(l[i][::-1])
print(" ".join(t))
