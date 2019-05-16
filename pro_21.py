n=int(input())
l=list(map(int,input().split()))
a=int(n/2)
t=[]
t.append(l[0:a])
t.append(l[a:])
a,b=sum(t[0])//len(t[0]),sum(t[1])//len(t[1])
print("yes" if a==b else "no")
