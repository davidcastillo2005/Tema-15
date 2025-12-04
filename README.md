# Proyecto Conjunto: Ecuaciones Diferenciales Ordinarias y Matemática Numérica, Segundo Año, Ciencia de la Computación, Universidad de La Habana, Curso 2025-2026

## 🌌 Aceleración Gravitacional Variable

### 👥 Equipo 15
Este repositorio contiene la implementación numérica, análisis matemático y visualización de resultados para el **Tema 15**, basado en el texto de *Edwards & Penney (4ta edición)*.

**Integrantes:**
* Patricia Conde Lorente C-212
* David Castillo Rodríguez C-211
* Boris Luis Vizcay Cartaya C-211

# Proyecto de EDO y Métodos Numéricos - Tema 15

## 📄 Descripción del Problema

El proyecto se divide en tres secciones que modelan la dinámica de cuerpos bajo aceleración gravitacional no constante, aplicando ecuaciones diferenciales ordinarias.

### Parte A: Problema de Julio Verne e Isoclinas 🚀
Se modela el lanzamiento de un proyectil desde la Tierra hacia la Luna. La distancia $r(t)$ desde el centro de la Tierra satisface:

$$
\frac{d^2r}{dt^2} = -\frac{GM_e}{r^2} + \frac{GM_m}{(S-r)^2}
$$

Donde:
* $M_e, M_m$: Masas de la Tierra y la Luna.
* $S$: Distancia Tierra-Luna ($384,400$ km).
* Condiciones iniciales: $r(0) = R$ (Radio terrestre), $r'(0) = v_0$.

**Objetivos realizados:**
1. Cálculo de la **velocidad mínima de lanzamiento $v_0$** para superar el punto de equilibrio gravitacional.
2. Visualización del **campo de isoclinas** para $\frac{dv}{dr}$ e interpretación de trayectorias.

### Parte B: Bifurcación 🔀
Análisis de cambios en la estabilidad dinámica mediante el modelo unidimensional con parámetro $\mu$:

$$
\frac{dz}{dt} = \mu z - z^3
$$

**Objetivos realizados:**
1. Determinación de puntos de equilibrio en función de $\mu$.
2. Clasificación de estabilidad usando el criterio de la derivada $z' = \mu - 3z^2$.
3. Construcción del **diagrama de bifurcación** e interpretación física (escape vs. captura gravitacional).

### Parte C: Plano de Fase y Estabilidad 📉
Estudio de un sistema numérico simplificado para altura $y(t)$ y velocidad $v(t)$ bajo gravedad decreciente:

$$
\begin{cases} 
\frac{dy}{dt} = v \\ 
\frac{dv}{dt} = -\frac{100}{(y+1)^2} 
\end{cases}
$$

**Objetivos realizados:**
1. Cálculo y clasificación de puntos críticos.
2. Generación del **plano de fase** para interpretar el movimiento (caída al centro o acercamiento asintótico).

---

## 💻 Requisitos y Tecnologías

El proyecto fue desarrollado utilizando **[Python / laTeX]**.

### Librerías necesarias
* numpy
* matplotlib
