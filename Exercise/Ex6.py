import numpy as np
m,n=map(int,input().split())
a=np.zeros((m,n),int)
c=[]
for i in range(m):
 for j in range(n):
  a[i,j]=int(input())
for i in range(m):
 c.append(a[i,0])
print(max(c))