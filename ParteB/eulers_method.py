def dy_dx(x, y):
    return x

def euler(dy_dx, x0, y0, x1, n):
    h = (x1 - x0)/n

    x = x0
    y = y0
    while x != x1:
        x = x + h
        y = y + h* dy_dx(0, y)

    return y