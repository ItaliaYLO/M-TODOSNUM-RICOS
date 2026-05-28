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
    def quimica(t, y):
        k1, k2 = 0.5, 0.2
        dA = -k1 * y[0]
        dB = k1 * y[0] - k2 * y[1]
        dC = k2 * y[1]
        return [dA, dB, dC]

    t_eval, sol = rk4_sistemas(quimica, 0, [100, 0, 0], 0.1, 50)

    print(f"--- Ejercicio 3.4 ---")
    print(f"Concentración final -> A: {sol[-1,0]:.2f}, B: {sol[-1,1]:.2f}, C: {sol[-1,2]:.2f}")
