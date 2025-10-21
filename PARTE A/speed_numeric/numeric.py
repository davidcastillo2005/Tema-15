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
    r = r0
    v = v0

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

def rk4(v0, r0, h, max_steps):
    r = r0
    v = v0

    for _ in range(max_steps):
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

        if r >= r_eq or r >= S:
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

        if r >= r_eq or r >= S:
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
        
        if r >= r_eq:
            return True
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


print("-.-.-h=1-.-.-")
print(f"Euler → {bisection(euler,R,1,1000000)}")
print(f"Heun → {bisection(heun,R,1,1000000)}")
print(f"Verlet → {bisection(verlet,R,1,1000000)}")
print(f"RK4 → {bisection(rk4,R,1,1000000)}")
print("-.-.-h=5-.-.-")
print(f"Euler → {bisection(euler,R,5,1000000)}")
print(f"Heun → {bisection(heun,R,5,1000000)}")
print(f"Verlet → {bisection(verlet,R,5,1000000)}")
print(f"RK4 → {bisection(rk4,R,5,1000000)}")
print("-.-.-h=10-.-.-")
print(f"Euler → {bisection(euler,R,10,1000000)}")
print(f"Heun → {bisection(heun,R,10,1000000)}")
print(f"Verlet → {bisection(verlet,R,10,1000000)}")
print(f"RK4 → {bisection(rk4,R,10,1000000)}")
print("-.-.-h=100-.-.-")
print(f"Euler → {bisection(euler,R,100,1000000)}")
print(f"Heun → {bisection(heun,R,100,1000000)}")
print(f"Verlet → {bisection(verlet,R,100,1000000)}")
print(f"RK4 → {bisection(rk4,R,100,1000000)}")