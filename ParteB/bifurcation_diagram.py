import matplotlib.pyplot as plt
import numpy as np
from differential_equation import dz_dt

def diagram():
    z = 0

    M = np.linspace(-10, 10, 21)

    dZ_dT = dz_dt(M, z)

    print(dZ_dT)