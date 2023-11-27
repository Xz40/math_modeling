import random
a,b,c=[],[],[]
N=int(input())
for i in range(N):
 a.append(int(random.randint(0,100)))
 b.append(int(random.randint(0,100)))
 c.append(int(random.randint(0,100)))
def max_(a,b,c):
 a1=max(a)
 print(a1)
 b1=max(b)
 c1=max(c)
 a2=max(a1,b1)
 b2=max(b1,c1) 
 return max(a2,b2)
max_(a,b,c)
def sum_(a,b,c):
 a1=sum(a)
 b1=sum(b)
 c1=sum(c)
 print(a1+b1+c1)
sum_(a,b,c)
