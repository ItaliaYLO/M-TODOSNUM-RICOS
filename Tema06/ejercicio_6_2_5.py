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
    k_rate = 0.5
    def reactivo(t, C): return -k_rate * C**2
    
    vt, vc = predictor_corrector(reactivo, 0, 1.0, 0.2, 25)
    
    c_real = 1.0 / (1.0 + k_rate * vt[-1])
    
    print(f"--- Ejercicio 2.5 ---")
    print(f"Concentración final después de {vt[-1]}s: {vc[-1]:.4f} mol/L")
    print(f"Valor real analítico: {c_real:.4f} mol/L")
