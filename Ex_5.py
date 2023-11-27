name="vashkevich timur"
a=[]
b=[]
d=[]
c=[]
for i in range(len(name)):
    a.append(name[i].upper())
for i in range(len(name)):
    b.append(name[i].lower())
    d.append(ord(a[i]))
    e=sum(d)
    c.append(ord(b[i]))
    f=sum(c)
print(*a)
print(*b)
print(e+f)