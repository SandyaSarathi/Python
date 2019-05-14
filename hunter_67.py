s=list(input().split("#"))
s1=[int(i) for i in s if i.isdigit()]
s1=sum(s1)
t=list(input().split("#"))
t1=[int(i) for i in t if i.isdigit()]
t1=sum(t1)
d={}
d[s[0]]=s1
d[t[0]]=t1
for i in d:
    if d[i]==max(s1,t1):
        print(i)


