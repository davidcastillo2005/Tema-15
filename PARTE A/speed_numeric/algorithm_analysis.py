import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11       
Me = 5.972e24     
Mm = 7.384e22       
R = 6.371e6        
S = 3.844e8         
r_eq = 3.263e8      

def acceleration(r):
    return -G*Me/r**2 + G*Mm/(S - r)**2

def euler(v0, r0, h, max_steps):
    r, v = r0, v0
    for _ in range(max_steps):
        a = acceleration(r)
        r_new = r + v*h
        v_new = v + a*h
        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True
        if r <= R:
            return False
    return False

def heun(v0, r0, h, max_steps):
    r, v = r0, v0
    for _ in range(max_steps):
        a1 = acceleration(r)
        r_pred = r + v*h
        v_pred = v + a1*h
        a2 = acceleration(r_pred)
        r_new = r + 0.5*h*(v + v_pred)
        v_new = v + 0.5*h*(a1 + a2)
        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True
        if r <= R:
            return False
    return False

def verlet(v0, r0, h, max_steps):
    r, v, a = r0, v0, acceleration(r0)
    for _ in range(max_steps):
        r_new = r + v*h + 0.5*a*h**2
        a_new = acceleration(r_new)
        v_new = v + 0.5*(a + a_new)*h
        r, v, a = r_new, v_new, a_new

        if r >= r_eq or r >= S:
            return True
        if r <= R:
            return False
    return False

def rk4(v0, r0, h, max_steps):
    r, v = r0, v0
    for _ in range(max_steps):
        a1 = acceleration(r)
        k1_r, k1_v = v, a1

        a2 = acceleration(r + 0.5*h*k1_r)
        k2_r, k2_v = v + 0.5*h*k1_v, a2

        a3 = acceleration(r + 0.5*h*k2_r)
        k3_r, k3_v = v + 0.5*h*k2_v, a3

        a4 = acceleration(r + h*k3_r)
        k4_r, k4_v = v + h*k3_v, a4

        r_new = r + (h/6)*(k1_r + 2*k2_r + 2*k3_r + k4_r)
        v_new = v + (h/6)*(k1_v + 2*k2_v + 2*k3_v + k4_v)
        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True
        if r <= R:
            return False
    return False

def bisection(metodo, r0, h, max_steps):
    v_escape = np.sqrt(2*G*Me/R)
    v_min = v_escape * 0.5
    v_max = v_escape * 1.2
    tol = 0.01

    for _ in range(50):
        v_mid = (v_min + v_max)/2
        alcanza = metodo(v_mid, r0, h, max_steps)
        if alcanza:
            v_max = v_mid
        else:
            v_min = v_mid
        if abs(v_max - v_min) < tol:
            break
    return (v_min + v_max)/2


def backward_analysis(metodo, v_crit_metodo, r0_original, h, max_steps, tol=1.0):
    r_min, r_max = r0_original - 1000.0, r0_original + 1000.0
    
    for _ in range(50):
        r_mid = (r_min + r_max) / 2
        
        alcanza = metodo(v_crit_metodo, r_mid, h, max_steps)
        
        if alcanza:
            r_max = r_mid  
        else:
            r_min = r_mid  
            
        if abs(r_max - r_min) < tol:
            break
            
    r_critico = (r_min + r_max) / 2
    delta_r = r_critico - r0_original
    return delta_r


print("=== ANÁLISIS FORWARD - Diferentes altitudes de lanzamiento ===\n")

v_tests = np.array([11000, 11070, 11072, 11075])
r_tests = np.array([6371000, 6571000, 6771000, 7171000, 7371000])
h_forward = 1
max_steps_forward = 1000000

forward_results = []

for r0 in r_tests:
    altitud_km = (r0 - 6371000) / 1000
    print(f"r0 = {r0} m ({altitud_km:.0f} km altitud)")
    
    v_euler = bisection(euler, r0, h_forward, max_steps_forward)
    v_heun = bisection(heun, r0, h_forward, max_steps_forward)
    v_verlet = bisection(verlet, r0, h_forward, max_steps_forward)
    v_rk4 = bisection(rk4, r0, h_forward, max_steps_forward)
    
    forward_results.append({
        'r0': r0,
        'altitud_km': altitud_km,
        'euler': v_euler,
        'heun': v_heun,
        'verlet': v_verlet,
        'rk4': v_rk4
    })
    
    print(f"Euler:  {v_euler:.2f} m/s")
    print(f"Heun:   {v_heun:.2f} m/s")
    print(f"Verlet: {v_verlet:.2f} m/s")
    print(f"RK4:    {v_rk4:.2f} m/s")
    print("-" * 40)


print("\n=== ANÁLISIS BACKWARD - Diferentes pasos temporales ===\n")

h_values = [1, 5, 10, 100]
max_steps_backward = 10000000

backward_results = []

for h in h_values:
    print(f"\n--- h = {h} s ---")
    
    r0 = R

    v_euler = bisection(euler, r0, h, max_steps_backward)
    v_heun = bisection(heun, r0, h, max_steps_backward)
    v_verlet = bisection(verlet, r0, h, max_steps_backward)
    v_rk4 = bisection(rk4, r0, h, max_steps_backward)
        
    delta_r_euler = backward_analysis(euler, v_euler, R, h, max_steps_backward)
    delta_r_heun = backward_analysis(heun, v_heun, R, h, max_steps_backward)
    delta_r_verlet = backward_analysis(verlet, v_verlet, R, h, max_steps_backward)
    delta_r_rk4 = backward_analysis(rk4, v_rk4, R, h, max_steps_backward)
        
    backward_results.append({
        'h': h,
        'euler': {'v': v_euler, 'delta_r': delta_r_euler},
        'heun': {'v': v_heun, 'delta_r': delta_r_heun},
        'verlet': {'v': v_verlet, 'delta_r': delta_r_verlet},
        'rk4': {'v': v_rk4, 'delta_r': delta_r_rk4}
    })
    
    print(f"Euler:  v = {v_euler:.2f} m/s, delta_r = {delta_r_euler:.3f} m")
    print(f"Heun:   v = {v_heun:.2f} m/s, delta_r = {delta_r_heun:.3f} m")
    print(f"Verlet: v = {v_verlet:.2f} m/s, delta_r = {delta_r_verlet:.3f} m")
    print(f"RK4:    v = {v_rk4:.2f} m/s, delta_r = {delta_r_rk4:.3f} m")