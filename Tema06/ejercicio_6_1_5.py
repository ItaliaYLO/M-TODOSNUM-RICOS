import numpy as np

def rk4(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x, y

if __name__ == "__main__":
    g, c, m = 9.81, 12.5, 70
    def paracaidas(t, v): return g - (c/m) * v

    t_eval, v_eval = rk4(paracaidas, 0, 0, 2, 10)
    
    v_terminal = (m * g) / c

    print(f"--- Simulación de Salto ---")
    print(f"Velocidad a los {t_eval[-1]}s: {v_eval[-1]:.2f} m/s")
    print(f"Velocidad terminal teórica: {v_terminal:.2f} m/s")
