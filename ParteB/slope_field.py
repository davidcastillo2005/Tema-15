import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def slope_field(dy_dx, density, xmin, xmax, ymin, ymax):
    m = np.linspace(xmin, xmax, density)
    t = np.linspace(ymin, ymax, density)

    M, T = np.meshgrid(m, t)

    dZ_dT = dy_dx(M, T)

    U = 1 / np.sqrt(1 + dZ_dT**2)
    V = dZ_dT / np.sqrt(1 + dZ_dT**2)

    return M, T, U, V

def plt_slope_field(X, Y, U, V):
    ax = plt.subplot(1,1,1)
    ax.streamplot(X, Y, U, V, color='gray', linewidth=1, density=1.5, arrowstyle='->', arrowsize=1.5)
    ax.quiver(X, Y, U, V, color='dodgerblue', scale=50, width=0.0015,headwidth=4, headlength=5)
    
    ax.grid(True, color = 'lightgray', linestyle='--', linewidth = 0.5)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
        ax.spines[spine].set_color('black')
        ax.spines[spine].set_linewidth(1.5)

    ax.tick_params(axis='both', which='major', colors='black', labelsize=12)

    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Slope field', fontsize = 16)
    ax.set_xlabel('t')
    ax.set_ylabel('z')
    plt.show()