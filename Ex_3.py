import time
n,m=map(int,input().split())
count=0
for i in range(m):
 for j in range(n):
  count+=1
  print(count)
  time.sleep(1)