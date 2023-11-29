import time
def func(x1):
    x1=5*x1**4+4*x1**3+3*x1**2+2*x1+1
    return x1
a=[]
def clear(a):
    for i in range(1000000):
        a.append(i)
clear(a)
print("start")
start=time.time()
a=list(map(func, a))
end=time.time() - start
print(end)
clear(a)
print('start')
start_1=time.time()
for i in range(1,len(a)+1):
    a.append(func(a[i]-1))
end_1=time.time() - start_1
print(end_1)
