import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

summ4 = 0
m_0 = m1_0 = 1000
k = 0.008
t1 = 0

for i in range(4):
    m1_0 = m1_0 - m1_0 * k
    summ4+=m1_0

t = np.arange(0, 100, 10**-2)

def money(m, t):
    dmdt = m_0 * -k
    return dmdt

m_t = odeint(money, m_0, t)

print(f'сумма инвестиций за 4 года: {summ4} денежных единиц')

# Построение решения в виде графика функции
plt.plot(t, m_t[:,0], label='получаемые инвестиции')
plt.xlabel('время, год')
plt.ylabel('денежная масса')
plt.title('количество инвестиций')
plt.legend()
 
plt.savefig("2")