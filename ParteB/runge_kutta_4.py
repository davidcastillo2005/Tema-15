from math import e

def dy_dx(x, y):
    return e**x

def pend(dy_dx, xi, yi, h):
    k1 = dy_dx(xi, yi)
    k2 = dy_dx(xi + h / 2, yi + k1 * h / 2)
    k3 = dy_dx(xi + h / 2, yi + k2 * h / 2)
    k4 = dy_dx(xi + h, yi + k3 * h)
    return h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

def rk4(dy_dx, x0, y0, x1, n):
    h = (x1 - x0)/n

    x = x0
    y = y0
    while x != x1:
        x = x + h
        y = y + h* dy_dx(x, y)

    return y

print(rk4(dy_dx, 0, 0, 5, 5))