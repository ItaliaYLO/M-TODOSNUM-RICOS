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
    def modelo_biologico(t, y):
        a, b, c, d = 1.2, 0.6, 0.8, 0.3
        d_presas = a*y[0] - b*y[0]*y[1]
        d_depredadores = -c*y[1] + d*y[0]*y[1]
        return [d_presas, d_depredadores]

    t_eval, sol = rk4_sistemas(modelo_biologico, 0, [2, 1], 0.1, 100)

    print(f"--- Ejercicio 3.1 ---")
    print(f"Población final -> Presas: {sol[-1,0]:.2f}, Depredadores: {sol[-1,1]:.2f}")
