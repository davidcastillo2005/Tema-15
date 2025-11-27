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

ax.set_xlabel('z(t)', loc = 'right')
ax.set_ylabel('mu', loc = 'top')

ax.grid(True)

mu_points = np.linspace(-3, 3, 15)
z_points = np.linspace(-3, 3, 15)
mu_meshgrid, z_meshgrid = np.meshgrid(mu_points, z_points)

U = 1 / np.sqrt(1 + dz_dt(mu_meshgrid, z_meshgrid)**2)
V = dz_dt(mu_meshgrid, z_meshgrid) / np.sqrt(1 + dz_dt(mu_meshgrid, z_meshgrid)**2)

magnitude = np.sqrt(U**2 + V**2)
V = V / magnitude
U = U / magnitude

ax.quiver(mu_meshgrid, z_meshgrid, U, V, 
          angles='xy', 
          scale_units='xy', 
          scale=3, 
          width = 0.005, 
          headwidth = 3, 
          headlength = 6, 
          headaxislength = 4, 
          color='blue', 
          alpha=0.8)

plt.savefig('CampoDireccional2.png')
plt.show()