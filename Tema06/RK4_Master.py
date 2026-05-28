import numpy as np

def rk4(f, x0, y0, h, n):
    """
    Implementación de RK4 con almacenamiento de pendientes factorizado.
    Optimizado para claridad en la actualización de estados.
    """
    # Inicialización de arreglos
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        # Cálculo de las 4 pendientes (estimaciones de la derivada)
        # Multiplicamos por h dentro de cada k para simplificar la suma final
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1)
        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2)
        k4 = h * f(x[i] + h,     y[i] + k3)

        # Actualización de y usando el promedio ponderado de Simpson
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x, y

# --- Ejemplo de prueba rápida ---
if __name__ == "__main__":
    # EDO: dy/dx = x * sqrt(y) | y(0) = 4
    def modelo(x, y): return x * np.sqrt(y)
    
    t, sol = rk4(modelo, 0, 4, 0.1, 5)
    
    print(f"{'Paso':<6} | {'x':<6} | {'y':<10}")
    print("-" * 25)
    for i in range(len(t)):
        print(f"{i:<6} | {t[i]:<6.1f} | {sol[i]:<10.5f}")
