from itertools import product
k=int(input())
l=list(product([0,1],repeat=k))
t=[]
for i in range(len(l)):
	for j in range(len(l[i])):
		t.append(str(l[i][j]))
	print("".join(t))
	t=[]
		
