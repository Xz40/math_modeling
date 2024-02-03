import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m_0 = m1_0 = 1
k = 2
t1 = 0

while m1_0 <= 10*m_0:
    t1+=1
    m1_0 *= k
    print(m1_0)

m_0 = 1

t = np.arange(0, 10, 10**-3)

def bact(m, t):
    dmdt = k * m
    return dmdt



	
m_t = odeint(bact, m_0, t)

print(f'бактерий станет больше в 10 раз через {t1} секунд(ы)')

# Построение решения в виде графика функции
plt.plot(t, m_t[:,0], label='Размножение бактерий')
plt.xlabel('секунды')
plt.ylabel('масса бактерий')
plt.title('Размножение бактерий')
plt.legend()
 
plt.savefig("1")