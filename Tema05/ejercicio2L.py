import numpy as np

def lagrange_funcional(x_puntos, y_puntos, x_objetivo):
    """
    Implementación usando un enfoque funcional con zip para 
    mayor claridad en el emparejamiento de nodos.
    """
    def calcular_base(i):
        # L_i(x) = Producto de (x - xj) / (xi - xj) para todo j != i
        terminos = [
            (x_objetivo - x_j) / (x_puntos[i] - x_j)
            for j, x_j in enumerate(x_puntos) if i != j
        ]
        return np.prod(terminos)

    # Calculamos todos los L_i y multiplicamos por sus respectivos y_i
    n = len(x_puntos)
    pesos_L = [calcular_base(i) for i in range(n)]
    
    return sum(y * L for y, L in zip(y_puntos, pesos_L))

# --- Ejercicio 2.2: Aproximación de sin(x) ---
if __name__ == "__main__":
    # Nodos: 0, 45° y 90° en radianes
    x_datos = np.array([0, np.pi/4, np.pi/2])
    y_datos = np.sin(x_datos)

    # Punto objetivo: 30° (pi/6)
    x_target = np.pi/6
    
    estimado = lagrange_funcional(x_datos, y_datos, x_target)
    real = np.sin(x_target)

    print(f"--- Análisis de Interpolación (sin(π/6)) ---")
    print(f"Estimado:   {estimado:.6f}")
    print(f"Valor Real: {real:.6f}")
    print(f"Error Abs:  {abs(real - estimado):.6e}")
