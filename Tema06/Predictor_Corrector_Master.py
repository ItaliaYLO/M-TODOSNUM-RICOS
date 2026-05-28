import numpy as np

def predictor_corrector(f, x0, y0, h, n):
    """
    Implementación optimizada de Adams-Bashforth-Moulton de 4to orden.
    Mantiene un historial de derivadas para mejorar el rendimiento.
    """
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.zeros(n + 1)

    f_hist = np.zeros(n + 1)
    
    y[0] = y0
    f_hist[0] = f(x[0], y[0])
    

    for i in range(3):
        k1 = h * f_hist[i]
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h,     y[i] + k3)
        
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        f_hist[i+1] = f(x[i+1], y[i+1])

    
    c_ab = h / 24.0
    c_am = h / 24.0

    for i in range(3, n):

        y_pred = y[i] + c_ab * (55*f_hist[i] - 59*f_hist[i-1] + 37*f_hist[i-2] - 9*f_hist[i-3])
        
        f_pred = f(x[i+1], y_pred)
        
        y[i+1] = y[i] + c_am * (9*f_pred + 19*f_hist[i] - 5*f_hist[i-1] + f_hist[i-2])
        
        f_hist[i+1] = f(x[i+1], y[i+1])
        
    return x, y

if __name__ == "__main__":
    def edo(x, y): return y - x**2 + 1
    
    vx, vy = predictor_corrector(edo, 0, 0.5, 0.1, 10)
    
    print(f"{'x':>5} | {'y (ABM4)':>10}")
    print("-" * 20)
    for i in range(len(vx)):
        print(f"{vx[i]:5.1f} | {vy[i]:10.6f}")
