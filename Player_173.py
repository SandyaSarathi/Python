#sa
s=input()
r=input()
g=[]
if (s.isalpha() or " " in s) and (r.isalpha() or " " in r):
    s=list(s.split(" "))
    r=list(r.split(" "))
    for i in s:
        if s.count(i) > r.count(i) and i not in g:
            g.append(i)
    for i in r:
        if r.count(i)>s.count(i) and i not in g:
            g.append(i)
    print(*g)
else:
    for i in s:
        if s.count(i)>r.count(i) and i not in g:
            g.append(i)
    for i in r:
        if r.count(i)>s.count(i) and i not in g:
            g.append(i)
    print(*g)
