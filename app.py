import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

G = 6.674e-11       
Me = 5.972e24  
Mm = 7.384e22
R  = 6.371e6         
S  = 3.844e8   
r_eq = 3.263e8       


def acceleration(r): 
    return -G*Me/r**2 + G*Mm/(S - r)**2



#SECCION 1#

def euler_step(v0, r0, h, max_steps):
    r, v = r0, v0
    r_list = [r]
    v_list = [v]

    for n in range(max_steps):

        a = acceleration(r)
        r = r + v*h
        v = v + a*h

        r_list.append(r)
        v_list.append(v)

        if r >= S:
            return r_list, v_list, True
        if r <= R:
            return r_list, v_list, False

    return r_list, v_list, False


def rk4_step(v0, r0, h, max_steps):
    r, v = r0, v0
    r_list = [r]
    v_list = [v]

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

        r = r + (h/6)*(k1_r + 2*k2_r + 2*k3_r + k4_r)
        v = v + (h/6)*(k1_v + 2*k2_v + 2*k3_v + k4_v)

        r_list.append(r)
        v_list.append(v)

        if r >= S:
            return r_list, v_list, True
        if r <= R:
            return r_list, v_list, False

    return r_list, v_list, False


def heun_step(v0, r0, h, max_steps):
    r, v = r0, v0
    r_list = [r]
    v_list = [v]

    for n in range(max_steps):

        a1 = acceleration(r)
        r_pred = r + v*h
        v_pred = v + a1*h
        a2 = acceleration(r_pred)

        r = r + 0.5*h*(v + v_pred)
        v = v + 0.5*(a1 + a2)

        r_list.append(r)
        v_list.append(v)

        if r >= S:
            return r_list, v_list, True
        if r <= R:
            return r_list, v_list, False

    return r_list, v_list, False


def verlet_step(v0, r0, h, max_steps):
    r, v = r0, v0
    a = acceleration(r)
    r_list = [r]
    v_list = [v]

    for n in range(max_steps):

        r_new = r + v*h + 0.5*a*h*h
        a_new = acceleration(r_new)
        v_new = v + 0.5*(a + a_new)*h

        r, v, a = r_new, v_new, a_new
        r_list.append(r)
        v_list.append(v)

        if r >= S:
            return r_list, v_list, True
        if r <= R:
            return r_list, v_list, False

    return r_list, v_list, False


def bisection_step(integrator, r0, h, max_steps):
    v_escape = np.sqrt(2*G*Me / R)
    v_min = v_escape * 0.5
    v_max = v_escape * 1.2
    tol = 0.01

    for n in range(60):
        v_mid = (v_min + v_max) / 2
        _, _, reached = integrator(v_mid, r0, h, max_steps)

        if reached:
            v_max = v_mid
        else:
            v_min = v_mid

        if abs(v_max - v_min) < tol:
            break

    return (v_min + v_max) / 2


st.title("De la Tierra a la Luna")

methods = {
    "Euler": euler_step,
    "RK4": rk4_step,
    "Heun": heun_step,
    "Verlet": verlet_step
}

st.header("Simulación de soluciones")

st.sidebar.subheader("Parámetros")
h = st.sidebar.number_input("Paso h", value=10.0, min_value=0.1)
r0_km = st.sidebar.number_input("Posición inicial r0[km]", value=6371.0, min_value=6371.0, max_value=384400.0)
r0_input = r0_km * 1000  
selected_method = st.selectbox("Seleccione un método:", ["Euler", "RK4", "Heun", "Verlet"])

if st.button("Calcular velocidad mínima"):

    v_min = bisection_step(methods[selected_method], r0_input, h, 1000000)
    st.success(f"Velocidad mínima crítica: {v_min:.2f} m/s")

    r_list, v_list, reached = methods[selected_method](v_min, r0_input, h, 1000000)

    plt.figure(figsize=(10,6))
    plt.plot(r_list, v_list, label=f'{selected_method}')

    plt.axvline(R, color='green', label="Tierra")
    plt.axvline(S, color='gray',label="Luna")

    plt.xlabel("Distancia r[m]")
    plt.ylabel("Velocidad v[m/s]")
    plt.title(f"Trayectoria con velocidad mínima crítica ({selected_method})")
    plt.legend()
    plt.grid(True)
    plt.ylim(-12000, 13000)

    st.pyplot(plt)





#SECCION 2#

def euler(v0, r0, h, max_steps):
    r = r0
    v = v0

    for _ in range(max_steps):
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


st.header("Comparación de métodos")

hs = [1, 5, 10, 100]
metodos = {
    "Euler": euler,
    "Heun": heun,
    "Verlet": verlet,
    "RK4": rk4
}

tabla = {
    "h": [],
    "Euler": [],
    "Heun": [],
    "Verlet": [],
    "RK4": []
}

for h in hs:
    tabla["h"].append(h)
    for nombre, metodo in metodos.items():
        vcrit = bisection(metodo, R, h, 1_000_000)
        tabla[nombre].append(round(vcrit, 3))

df = pd.DataFrame(tabla)
st.table(df)