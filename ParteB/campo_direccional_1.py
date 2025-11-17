from differential_equation import dz_dt
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlabel('t', loc = 'right')
ax.set_ylabel('z(t)', loc = 'top')

ax.grid(True)

t_points = np.linspace(-3, 3, 11)
z_points = np.linspace(-3, 3, 11)
t, z = np.meshgrid(t_points, z_points)

U = 1 / np.sqrt(1 + dz_dt(0, z)**2)
V = dz_dt(0, z) / np.sqrt(1 + dz_dt(0, z)**2)

magnitude = np.sqrt(U**2 + V**2)
V = V / magnitude
U = U / magnitude

ax.quiver(t, z, U, V, 
          angles='xy', 
          scale_units='xy', 
          scale=3, 
          width = 0.005, 
          headwidth = 3, 
          headlength = 6, 
          headaxislength = 4, 
          color='blue', 
          alpha=0.8)

plt.savefig('CampoDireccional1')
plt.show()