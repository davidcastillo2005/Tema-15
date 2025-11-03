#%%
import matplotlib.pyplot as plt
from math import e
from differential_equation import dz_dt
from runge_kutta_4 import rk4, plt_rk4
from slope_field import slope_field as slopes, plt_slope_field as plt_slopes

def dy_dx(x, y):
    return y + x

M, T, U, V = slopes(dz_dt, 21, -10, 10, -10, 10)
plt_slopes(M, T, U, V)
#%%