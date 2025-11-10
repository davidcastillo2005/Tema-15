from differential_equation import dz_dt
import matplotlib.pyplot as plt
import numpy as np

t_points = np.linspace(0, 1, 1)
z_points = np.linspace(-3, 3, 7)
t, z = np.meshgrid(t_points, z_points)

dt = np.zeros_like(t)
dz = dz_dt(t, z)      

magnitud = np.sqrt(dt**2 + dz**2)
dt_norm = dt / magnitud
dz_norm = dz / magnitud

fig, ax = plt.subplots(figsize=(6, 6))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')

ax.spines['left'].set_position('zero')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_visible(False)

ax.quiver(t, z, dt_norm, dz_norm, 
           angles='xy', 
           scale_units='xy', 
           scale=2, 
           width = 0.005, 
           headwidth = 3, 
           headlength = 6, 
           headaxislength = 4, 
           color='blue', 
           alpha=0.8)

ax.set_xlabel('t', loc = 'right')
ax.set_ylabel('z(t)', loc = 'top')
plt.savefig('CampoDireccional1')