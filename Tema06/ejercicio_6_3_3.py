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
    g, L = 9.81, 1.0
    def pendulo(t, y):
        d_theta = y[1]
        d_omega = -(g/L) * np.sin(y[0])
        return [d_theta, d_omega]

    t_eval, sol = rk4_sistemas(pendulo, 0, [np.pi/4, 0], 0.05, 40)

    print(f"--- Ejercicio 3.3 ---")
    print(f"Ángulo final (rad): {sol[-1,0]:.4f}")
    print(f"Velocidad angular final (rad/s): {sol[-1,1]:.4f}")
