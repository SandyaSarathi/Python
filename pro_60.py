n=int(input())
k=n
t=1
a=3
v=a
while n>1:
	t+=1
	v-=1
	if v==1 and t!=k:
		v=a*2
		t+=1
		a=v
		n-=2
		continue
	n-=1
print(v)
	
