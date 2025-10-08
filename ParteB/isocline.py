import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def isocline(dy_dx, density, xmin, xmax, ymin, ymax):
    density = 21

    t = np.linspace(xmin, xmax, density)
    z = np.linspace(ymin, ymax, density)

    T, Z = np.meshgrid(t, z)

    dZ_dT = dy_dx(T, Z)

    U = 1 / np.sqrt(1 + dZ_dT**2)
    V = np.abs(dZ_dT) / np.sqrt(1 + dZ_dT**2)

    ax = plt.subplot(1,1,1)
    ax.streamplot(T, Z, U, V, color='gray', linewidth=1, density=1.5, arrowstyle='->', arrowsize=1.5)
    ax.quiver(T, Z, U, V, color='dodgerblue', scale=50, width=0.0015,headwidth=4, headlength=5)
    
    ax.grid(True, color = 'lightgray', linestyle='--', linewidth = 0.5)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
        ax.spines[spine].set_color('black')
        ax.spines[spine].set_linewidth(1.5)

    ax.tick_params(axis='both', which='major', colors='black', labelsize=12)

    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Differential field', fontsize = 16)
    ax.set_xlabel('t')
    ax.set_ylabel('z')
    plt.show()
