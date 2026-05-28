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
        k4 = h * np.asarray(f(x[i] + h,     y[i] + k3))
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x, y

if __name__ == "__main__":
    L, R, C, E = 0.5, 10, 0.001, 12
    def circuito_rlc(t, y):
        dq = y[1]
        di = (E - R*y[1] - (1/C)*y[0]) / L
        return [dq, di]

    t_eval, sol = rk4_sistemas(circuito_rlc, 0, [0, 0], 0.01, 100)

    print(f"--- Ejercicio 3.5 ---")
    print(f"Carga en el capacitor (q): {sol[-1,0]:.6f} C")
    print(f"Corriente final en el inductor (i): {sol[-1,1]:.4f} A")
