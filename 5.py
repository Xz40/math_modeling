p=int(input())
d=[]
for i in range(1,p):
    if p%i==0:
        d.append(i)
l=0
for i in range(len(d)):
    l=d[i]+l
if l==p:
    print("совершенное")