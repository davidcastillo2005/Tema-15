import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

G = 6.674e-11       
Me = 5.972e24  
Mm = 7.384e22
R = 6.371e6         
S = 3.844e8   
r_eq = 3.263e8      

def acceleration(r):
    return -G*Me/r**2 + G*Mm/(S - r)**2

def euler(v0, r0, h, max_steps):
    r = r0
    v = v0

    for n in range(max_steps):
        a = acceleration(r)
        r_new = r + v*h
        v_new = v + a*h
        r, v = r_new, v_new

        if r >= S:
            return True
        if r <= R:
            return False

    return False

def rk4(v0, r0, h, max_steps):
    r = r0
    v = v0

    for n in range(max_steps):
        a1 = acceleration(r)
        k1_r = v
        k1_v = a1

        a2 = acceleration(r + 0.5*h*k1_r)
        k2_r = v + 0.5*h*k1_v
        k2_v = a2

        a3 = acceleration(r + 0.5*h*k2_r)
        k3_r = v + 0.5*h*k2_v
        k3_v = a3

        a4 = acceleration(r + h*k3_r)
        k4_r = v + h*k3_v
        k4_v = a4

        r_new = r + (h/6)*(k1_r + 2*k2_r + 2*k3_r + k4_r)
        v_new = v + (h/6)*(k1_v + 2*k2_v + 2*k3_v + k4_v)

        r, v = r_new, v_new

        if r >= S:
            return True
        if r <= R:
            return False

    return False

def heun(v0, r0, h, max_steps):
    r = r0
    v = v0

    for _ in range(max_steps):
        a1 = acceleration(r)
        r_pred = r + v*h
        v_pred = v + a1*h
        a2 = acceleration(r_pred)
        r_new = r + 0.5*h*(v + v_pred)
        v_new = v + 0.5*h*(a1 + a2)
        r, v = r_new, v_new

        if r >= S:
            return True
        if r <= R:
            return False

    return False

def verlet(v0, r0, h, max_steps):
    r = r0
    v = v0
    a = acceleration(r)
    
    for step in range(max_steps):
        r_new = r + v*h + 0.5*a*h**2
        a_new = acceleration(r_new)
        v_new = v + 0.5*(a + a_new)*h
        r, v, a = r_new, v_new, a_new
        
        if r <= R:
            return False
        if r >= S:
            return True
    
    return False

def bisection(metodo, r0, h, max_steps):
    v_escape = np.sqrt(2*G*Me/R)
    v_min = v_escape * 0.5
    v_max = v_escape * 1.2
    tol = 0.01
    
    for n in range(50):
        v_mid = (v_min + v_max)/2
        alcanza = metodo(v_mid, r0, h, max_steps)
        
        if alcanza:
            v_max = v_mid
        else:
            v_min = v_mid
            
        if abs(v_max - v_min) < tol:
            break
    
    velocidad_critica = (v_min + v_max)/2
    return velocidad_critica



methods = [
    ("Euler", euler),
    ("Heun", heun),
    ("Verlet", verlet),
    ("RK4", rk4)
]


h_values = [1, 5, 10, 100]
results = []

for h in h_values:
    row = {"h (s)": h}
    
    for method_name, method_func in methods:
        v_critica = bisection(method_func, R, h, 1000000)
        row[method_name] = v_critica
    
    results.append(row)

df = pd.DataFrame(results)
pd.set_option('display.precision', 2)
pd.set_option('display.width', 100)
pd.set_option('display.max_columns', None)

print("\n" + "="*70)
print("TABLA DE RESULTADOS - VELOCIDADES CRÍTICAS (m/s)")
print("="*70)

print("\n" + df.to_string(index=False))
print("\n" + "-"*70)