import matplotlib.pyplot as plt
import numpy as np
a,b,N=input().split()
def parabolla(a,b,N):
    a=int(a)
    b=int(b)
    N = int(N)
    if a > b:
        a,b=b,a
    x=np.arange(a,b,1/N)
    x.(0)
    y = 1/x
    plt.plot(x,y)
parabolla(a,b,N)
plt.axis('equal')
plt.savefig("pic_2")