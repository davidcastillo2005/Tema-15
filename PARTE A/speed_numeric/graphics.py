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


def euler(v0, h=100, max_steps=1000000):
    r = R
    v = v0
    trajectory_r = [r]
    trajectory_v = [v]

    for _ in range(max_steps):
        a = acceleration(r)
        r_new = r + v*h
        v_new = v + a*h

        trajectory_r.append(r_new)
        trajectory_v.append(v_new)

        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True, trajectory_r, trajectory_v
        if r <= R:
            return False, trajectory_r, trajectory_v

    return False, trajectory_r, trajectory_v


def rk4(v0, h=100, max_steps=1000000):
    r = R
    v = v0
    trajectory_r = [r]
    trajectory_v = [v]

    for _ in range(max_steps):
        # k1
        a1 = acceleration(r)
        k1_r = v
        k1_v = a1

        # k2
        a2 = acceleration(r + 0.5*h*k1_r)
        k2_r = v + 0.5*h*k1_v
        k2_v = a2

        # k3
        a3 = acceleration(r + 0.5*h*k2_r)
        k3_r = v + 0.5*h*k2_v
        k3_v = a3

        # k4
        a4 = acceleration(r + h*k3_r)
        k4_r = v + h*k3_v
        k4_v = a4

        # Actualizar posición y velocidad
        r_new = r + (h/6)*(k1_r + 2*k2_r + 2*k3_r + k4_r)
        v_new = v + (h/6)*(k1_v + 2*k2_v + 2*k3_v + k4_v)

        trajectory_r.append(r_new)
        trajectory_v.append(v_new)

        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True, trajectory_r, trajectory_v
        if r <= R:
            return False, trajectory_r, trajectory_v

    return False, trajectory_r, trajectory_v


def heun(v0, h=100, max_steps=1000000):
    r = R
    v = v0
    trajectory_r = [r]
    trajectory_v = [v]

    for _ in range(max_steps):
        a1 = acceleration(r)

        r_pred = r + v*h
        v_pred = v + a1*h
        a2 = acceleration(r_pred)

        r_new = r + 0.5*h*(v + v_pred)
        v_new = v + 0.5*h*(a1 + a2)

        trajectory_r.append(r_new)
        trajectory_v.append(v_new)

        r, v = r_new, v_new

        if r >= r_eq or r >= S:
            return True, trajectory_r, trajectory_v
        if r <= R:
            return False, trajectory_r, trajectory_v

    return False, trajectory_r, trajectory_v



def verlet(v0, h=100, max_steps=1000000):

    r = R
    v = v0
    a = acceleration(r)
    
    trayectoria_r = [r]
    trayectoria_v = [v]
    
    for step in range(max_steps):
      
        r_new = r + v*h + 0.5*a*h**2
        
        a_new = acceleration(r_new)
        
        v_new = v + 0.5*(a + a_new)*h
        
      
        trayectoria_r.append(r_new)
        trayectoria_v.append(v_new)
        
       
        r, v, a = r_new, v_new, a_new
        
        if r >= r_eq:
            return True, trayectoria_r, trayectoria_v
        if r <= R:
            return False, trayectoria_r, trayectoria_v
        if r >= S:
            return True, trayectoria_r, trayectoria_v
    
    return False, trayectoria_r, trayectoria_v



def bisection(metodo, h, max_steps):
    v_escape = np.sqrt(2*G*Me/R)
    v_min = v_escape * 0.5
    v_max = v_escape * 1.2
    tol = 0.01
    
    for n in range(50):
        v_mid = (v_min + v_max)/2
        alcanza, _, _ = metodo(v_mid, h, max_steps)

        
        if alcanza:
            v_max = v_mid
        else:
            v_min = v_mid
            
        if abs(v_max - v_min) < tol:
            break
    
    velocidad_critica = (v_min + v_max)/2
    return velocidad_critica



v0 = 11000            
tmax = 100000        
h = 100          

alcanzo_euler, r_euler, v_euler = euler(v0, h, tmax)
alcanzo_heun, r_heun, v_heun = heun(v0, h, tmax)
alcanzo_verlet, r_verlet, v_verlet = verlet(v0, h, tmax)
alcanzo_rk4, r_rk4, v_rk4 = rk4(v0, h, tmax)


plt.figure(figsize=(10,7))
plt.title("Simulación de la trayectoria radial desde la Tierra: comparación de métodos")
plt.plot(np.array(r_euler)/1e6, v_euler, alpha=0.7, label="Euler")
plt.plot(np.array(r_heun)/1e6, v_heun, alpha=0.7, label="Heun (RK2)")
plt.plot(np.array(r_verlet)/1e6, v_verlet, alpha=0.7, label="Verlet")
plt.plot(np.array(r_rk4)/1e6, v_rk4, 'purple', alpha=0.8, label="RK4")
plt.xlabel("Distancia desde el centro de la Tierra (x10⁶ m)")
plt.ylabel("Velocidad (m/s)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()