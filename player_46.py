import math
n=int(input())
if n==90:
	print(1)
else:
	n=math.radians(n)
	print(round(math.sin(n),1))
