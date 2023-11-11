import numpy as np
m,n=map(int,input().split())
a=np.zeros((m,n),int)
c=[]
d=[]
for i in range(m):
 for j in range(n):
  a[i,j]=int(input())
print(a)
for i in range(m):
  c=[]
  for j in range(n):
    c.append(a[j,i])
  print(max(c))
  