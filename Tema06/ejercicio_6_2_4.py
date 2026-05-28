import numpy as np

def predictor_corrector(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.zeros(n + 1)
    fd = np.zeros(n + 1)
    
    y[0] = y0
    fd[0] = f(x[0], y[0])
    
    for i in range(3):
        k1 = h * fd[i]
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        fd[i+1] = f(x[i+1], y[i+1])

    c = h / 24.0
    for i in range(3, n):
        y_p = y[i] + c * (55*fd[i] - 59*fd[i-1] + 37*fd[i-2] - 9*fd[i-3])
        f_p = f(x[i+1], y_p)
        y[i+1] = y[i] + c * (9*f_p + 19*fd[i] - 5*fd[i-1] + fd[i-2])
        fd[i+1] = f(x[i+1], y[i+1])
        
    return x, y

if __name__ == "__main__":
    def f(x, y): return x - y
    
    vx, vy = predictor_corrector(f, 0, 1, 0.1, 15)
    
    y_real = 2 * np.exp(-vx[-1]) + vx[-1] - 1
    
    print(f"--- Ejercicio 2.4 ---")
    print(f"Estimación final en x={vx[-1]:.1f}: {vy[-1]:.5f}")
    print(f"Valor real exacto: {y_real:.5f}")
