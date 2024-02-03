import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1.0
a0 = 1.0
Y = 1.0


v0 = 0.0
t = np.linspace(0, 10, 1000)

def dy_dt(y, t):
    v = y[0]
    dv_dt = a0 - Y * v**2 
    return dv_dt

v = odeint(dy_dt, v0, t)

plt.plot(t, v[:,0], label='график скорости')
plt.xlabel('время, год')
plt.ylabel('скорость')
plt.title('график скорости')
plt.legend()
 
plt.savefig("3")