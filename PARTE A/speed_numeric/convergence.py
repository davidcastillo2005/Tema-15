import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
Me = 5.972e24       
Mm = 7.384e22     
R = 3.84e8          
r0 = 6.371e6        
v0 = 11000         
t_final = 10000    


def a(r):
    return -G * Me / r**2 + G * Mm / (R - r)**2

def euler(h):
    n = int(t_final / h)
    r, v = r0, v0
    for _ in range(n):
        v += h * a(r)
        r += h * v
    return r

def heun(h):
    n = int(t_final / h)
    r, v = r0, v0
    for _ in range(n):
        k1_v = a(r)
        k1_r = v
        k2_v = a(r + h * k1_r)
        k2_r = v + h * k1_v
        v += h/2 * (k1_v + k2_v)
        r += h/2 * (k1_r + k2_r)
    return r

def verlet(h):
    n = int(t_final / h)
    r, v = r0, v0
    a_actual = a(r)
    for _ in range(n):
        r += v * h + 0.5 * a_actual * h**2
        a_nueva = a(r)
        v += 0.5 * (a_actual + a_nueva) * h
        a_actual = a_nueva
    return r

def rk4(h):
    n = int(t_final / h)
    r, v = r0, v0
    for _ in range(n):
        k1_r = v
        k1_v = a(r)
        k2_r = v + 0.5 * h * k1_v
        k2_v = a(r + 0.5 * h * k1_r)
        k3_r = v + 0.5 * h * k2_v
        k3_v = a(r + 0.5 * h * k2_r)
        k4_r = v + h * k3_v
        k4_v = a(r + h * k3_r)
        r += (h / 6) * (k1_r + 2*k2_r + 2*k3_r + k4_r)
        v += (h / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)
    return r


def calcular_orden(metodo, h1, h2, ref):
    r1 = metodo(h1)
    r2 = metodo(h2)
    e1 = abs(r1 - ref)
    e2 = abs(r2 - ref)
    return np.log(e2 / e1) / np.log(h2 / h1)


h1, h2 = 5, 10
ref = rk4(0.1)  

metodos = {
    "Euler": euler,
    "Heun": heun,
    "Verlet": verlet,
    "RK4": rk4
}

print("===== Resultados finales =====")
for nombre, metodo in metodos.items():
    orden = calcular_orden(metodo, h1, h2, ref)
    print(f"{nombre:7s}: orden ≈ {orden:.3f}")
