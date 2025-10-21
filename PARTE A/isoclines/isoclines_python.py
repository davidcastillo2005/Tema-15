import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

Me = 5.972e24
G = 6.674e-11
Mm = 7.384e22
S = 3.844e8
R = 6.371e6

def f(r, v):
    return (-G*Me/r**2 + G*Mm/(S-r)**2) / v

x = np.linspace(1.01*R, S*1.3, 80)
y = np.linspace(-12, 12, 40)
X, Y = np.meshgrid(x, y)

M = f(X, Y)
U = np.ones_like(M)
V = M
N = np.sqrt(U**2 + V**2)
U, V = U/N, V/N

plt.figure(figsize=(14, 8))

plt.quiver(X, Y, U, V, scale=80, headwidth=3, headlength=4, headaxislength=3, color='lightgray', alpha=0.6)

r_vals = np.linspace(R*1.01, S*0.99, 1000)

# =============================================================================
# ISOCLINA 1: Pendiente CERO (k = 0)
# =============================================================================
def acceleration(r):
    return -G*Me/r**2 + G*Mm/(S-r)**2

r_eq = fsolve(acceleration, S)[0]
plt.axvline(x=r_eq, color='navy', linestyle='-', linewidth=2.5, label='Isoclina k=0 (a=0)')

# =============================================================================
# ISOCLINA 2: Pendiente INFINITA
# =============================================================================

plt.axhline(y=0, color='mediumblue', linestyle='-', linewidth=2.5, label='Isoclina k=∞ (v=0)')

# =============================================================================
# ISOCLINA 3: Pendiente k = 1
# =============================================================================

k = 1
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'blue', linewidth=2, label='Isoclina k=1')

# =============================================================================
# ISOCLINA 4: Pendiente k = 5
# =============================================================================

k = 5
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'royalblue', linewidth=2, label='Isoclina k=5')

# =============================================================================
# ISOCLINA 5: Pendiente k = -1
# =============================================================================

k = -1
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'dodgerblue', linewidth=2, label='Isoclina k=-1')

# =============================================================================
# ISOCLINA 6: Pendiente k = -5
# =============================================================================

k = -5
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'lightskyblue', linewidth=2, label='Isoclina k=-5')

# =============================================================================
# ISOCLINA 7: Pendiente k = 0.5
# =============================================================================

k = 0.5
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'lightblue', linewidth=2, label='Isoclina k=0.5')

# =============================================================================
# ISOCLINA 8: Pendiente k = -0.5
# =============================================================================

k = -0.5
aceleracion = -G*Me/r_vals**2 + G*Mm/(S - r_vals)**2
v_isoclina = aceleracion / k
mask = (np.abs(v_isoclina) < 12) & (r_vals > R) & (r_vals < S)
plt.plot(r_vals[mask], v_isoclina[mask], 'aliceblue', linewidth=2, label='Isoclina k=-0.5')


plt.xlabel("r (distancia desde centro de la Tierra)", fontsize=12)
plt.ylabel("v (velocidad)", fontsize=12)
plt.title("CAMPO DE DIRECCIONES E ISOCLINAS", fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlim(R*1.01, S * 1.3)
plt.ylim(-12, 12)
plt.tight_layout()
plt.show()
