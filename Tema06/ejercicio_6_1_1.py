import numpy as np
import matplotlib.pyplot as plt

def comparar_metodos():
    # --- Configuración del Problema ---
    # dy/dx = f(x, y)
    f = lambda x, y: -2*x**3 + 12*x**2 - 20*x + 8.5
    
    # Solución analítica (integrando la EDO) para referencia
    # y(x) = -0.5x^4 + 4x^3 - 10x^2 + 8.5x + C; si y(0)=1, C=1
    f_real = lambda x: -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

    x0, y0 = 0, 1
    h = 0.5
    n = 8
    xf = x0 + n*h

    # --- 1. Método de Euler (Primer Orden) ---
    xe = np.linspace(x0, xf, n + 1)
    ye = np.zeros(n + 1)
    ye[0] = y0
    for i in range(n):
        ye[i+1] = ye[i] + f(xe[i], ye[i]) * h

    # --- 2. Método de Runge-Kutta 4 (Cuarto Orden) ---
    xr = np.linspace(x0, xf, n + 1)
    yr = np.zeros(n + 1)
    yr[0] = y0
    for i in range(n):
        k1 = h * f(xr[i], yr[i])
        k2 = h * f(xr[i] + 0.5*h, yr[i] + 0.5*k1)
        k3 = h * f(xr[i] + 0.5*h, yr[i] + 0.5*k2)
        k4 = h * f(xr[i] + h, yr[i] + k3)
        yr[i+1] = yr[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

    # --- Visualización ---
    x_exacta = np.linspace(x0, xf, 100)
    y_exacta = f_real(x_exacta)

    plt.figure(figsize=(10, 6))
    plt.plot(x_exacta, y_exacta, 'k', label='Solución Exacta', alpha=0.5, lw=2)
    plt.plot(xe, ye, 'ro--', label=f'Euler (h={h})', markersize=4)
    plt.plot(xr, yr, 'bs-', label=f'RK4 (h={h})', markersize=4)
    
    plt.title("Impacto de la Precisión: Euler vs. Runge-Kutta 4", fontsize=14)
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend(); plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    comparar_metodos()
