a,b,c=map(int,input().split())
D=b**2-4*a*c
if D>0:
    x1=-1*b+D**0.5
    x2=-1*b-D**0.5
    print(x1/2,x2/2)
elif D==0:
    print(-1*b/2*a)
else:
    print('корней нет')
