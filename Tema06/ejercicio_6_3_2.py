import numpy as np

def rk4_sistemas(f, x0, y0, h, n):
    y0 = np.asarray(y0, dtype=float)
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0

    for i in range(n):
        k1 = h * np.asarray(f(x[i], y[i]))
        k2 = h * np.asarray(f(x[i] + 0.5*h, y[i] + 0.5*k1))
        k3 = h * np.asarray(f(x[i] + 0.5*h, y[i] + 0.5*k2))
        k4 = h * np.asarray(f(x[i] + h, y[i] + k3))
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x, y

if __name__ == "__main__":
    m, c, k = 1.0, 0.5, 2.0
    def masa_resorte(t, y):
        d_posicion = y[1]
        d_velocidad = -(c/m)*y[1] - (k/m)*y[0]
        return [d_posicion, d_velocidad]

    t_eval, sol = rk4_sistemas(masa_resorte, 0, [1.0, 0], 0.1, 50)

    print(f"--- Ejercicio 3.2 ---")
    print(f"Posición final a los {t_eval[-1]}s: {sol[-1,0]:.4f} m")
    print(f"Velocidad final: {sol[-1,1]:.4f} m/s")
