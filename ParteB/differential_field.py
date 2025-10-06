import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from differential_equation import dz_dt

def from_radians_to_degrees(rad):
    return (rad * 180) / pi

def from_degrees_to_radians(deg):
    return (deg * pi) / 180

def plot_quiver(t, z, f,start_t, start_z, xmin, xmax, ymin, ymax, n, m):
    t0, z0 = start_t, start_z
    X = []
    Y = []
    while True:
        t1 = t0 - 1
        t2 = t0 + 1

        z1 = z0 - 1
        z2 = t0 + 1

        break
    return

def run():
    n, m = 51,  51
    xmin, xmax = -10, 10
    ymin, ymax = -10, 10

    t = np.linspace(xmin, xmax, n)
    z = np.linspace(ymin, ymax, m)

    T, Z = np.meshgrid(t, z)

    dZ_dT = dz_dt(10, T, Z)

    U = 1 / np.sqrt(1 + dZ_dT**2)
    V = np.abs(dZ_dT) / np.sqrt(1 + dZ_dT**2)

    plt.quiver(T, Z, U, V, scale = 60)
    plt.grid()
    plt.show()

run()
