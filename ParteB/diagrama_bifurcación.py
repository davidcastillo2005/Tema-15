import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.grid(True)

plt_mu_1 = np.linspace(-3, 0, 2)
plt_mu_2 = np.linspace(0, 3, 71)
plt_mu_3 = np.linspace(0, 3, 71)
plt_mu_4 = np.linspace(0, 3, 2)

plt_z_1 = np.zeros_like(plt_mu_1)
plt_z_2 = np.sqrt(plt_mu_2)
plt_z_3 = -1 * np.sqrt(plt_mu_3)
plt_z_4 = np.zeros_like(plt_mu_4)

ax.plot(plt_mu_1, plt_z_1, color='blue', linewidth=3)
ax.plot(plt_mu_2, plt_z_2, color='blue', linewidth=3)
ax.plot(plt_mu_3, plt_z_3, color='blue', linewidth=3)
ax.plot(plt_mu_4, plt_z_4, color='blue', linestyle=':', linewidth=3)

plt.savefig('DiagramaBifurcación.png')
plt.show()