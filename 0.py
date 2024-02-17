from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

e = np.e

def system(s, t):
    y, x = s
    dx_dt = 3 * x - 2 * y + (e**3*t)/e**t + 1
    dy_dt = x - (e**3*t)/e**t + 1
    return dx_dt, dy_dt
x0 = 5  # Начальные значения
y0 = -7
s0 = y0, x0

t = np.arange(-1, 1, 0.1)  # Интервал времени

y = odeint(system, s0, t)

# Строим решение в виде графика
plt.plot(t, y[:, 0],)

plt.savefig('fig_1.png')