from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def system(s, x):
    y, z = s
    dy_dx = y**2*z 
    dz_dx = z / x - y * z**2
    return dy_dx, dz_dx
z0 = -3  # Начальные значения
y0 = 1

x = np.arange(-5, 5, 0.1)  # Интервал времени

s0 = y0, z0

y = odeint(system, s0, x)

# Строим решение в виде графика
plt.plot(x, y[:, 0],)

plt.savefig('fig_2.png')