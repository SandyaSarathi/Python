n=int(input())
s=input()
l=[]
j=0
for i in range(n):
	if s[i]=="0":
		l.append(s[j:i])
		j=i+1
l="".join(l)
print(*l)
