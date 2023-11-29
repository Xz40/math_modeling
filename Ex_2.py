name="vashkevich timur"
name_upper="_".join(name).upper()
a=[]
b=[]
for symbol in name_upper:
    a.append(int(ord(symbol)))
print(name_upper)
name_lower="_".join(name).lower()
print(name_lower)
print(a)
maxx=max(a)
print(maxx)
minn=min(a)
print(minn)