a=input()
from itertools import permutations
perm = permutations(a) 
perm=set(perm)
for i in list(perm): 
    print ("".join(i)) 
