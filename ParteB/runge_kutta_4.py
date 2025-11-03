import numpy as np
import matplotlib.pyplot as plt

def pend(dy_dx, x, y, h):
    k1 = dy_dx(x, y)
    k2 = dy_dx(x + h * 0.5, y + k1 * h * 0.5)
    k3 = dy_dx(x + h * 0.5, y + k2 * h * 0.5)
    k4 = dy_dx(x + h, y + k3 * h)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6

def rk4(dy_dx, x0, y0, x_final, n, h = 0, ):
    if n == 0:
        aux = h
    else:
        aux = (x_final - x0) / n

    X = np.arange(x0, x_final + aux, aux)
    Y = np.zeros(len(X))
    Y[0] = y0

    for i in range(len(X) - 1):
        p = pend(dy_dx, X[i], Y[i], aux)
        Y[i + 1] = Y[i] + aux * p / 6

    return X, Y

def plt_rk4(X, Y):
    ax = plt.subplot(1,1,1)
    ax.grid(True, color = 'lightgray', linestyle='--', linewidth = 0.5)
    # ax.set_aspect('equal', adjustable='box')
    ax.set_title('Differential field', fontsize = 16)
    ax.set_xlabel('t')
    ax.set_ylabel('z')
    ax.plot(X, Y)
    plt.show()