import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

G = 1
Mm = 2
Me = 1
S = 1

def f(r):
    return (-1 * (Me / r ** 2) + (Mm / (S - r) ** 2))

R0 =  S
R1 = -1 * (Me + sqrt(Me * Mm)) / (Mm - Me)
R2 = (sqrt(Me * Mm) - Me) / Mm - Me

Mm = Mm
Me = Me 
S = S

x = np.linspace(1e-10, 1e2, 100000000)
y = f(x)

plt.plot(x, y)
plt.savefig('test.png')
plt.show
print(f(R1))