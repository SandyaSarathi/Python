from itertools import product
n=int(input())
l=list(product([0,1],repeat=n))
t=[]
for i in range(len(l)):
	for j in range(len(l[i])):
		t.append(str(l[i][j]))
	print("".join(t))
	t=[]
		
