import numpy as np

def lagrange_vectorizado(x_puntos, y_puntos, x_objetivo):
    """
    Versión optimizada que usa broadcasting de NumPy 
    para calcular el polinomio de Lagrange.
    """
    n = len(x_puntos)
    L = np.ones(n)
    
    for i in range(n):
        # Creamos una máscara para omitir el punto x_i
        nodos_restantes = np.delete(x_puntos, i)
        
        # Calculamos L_i(x) como el producto de (x - xj) / (xi - xj)
        numeradores = x_objetivo - nodos_restantes
        denominadores = x_puntos[i] - nodos_restantes
        L[i] = np.prod(numeradores / denominadores)
        
    # El resultado es el producto punto entre y_puntos y nuestros coeficientes L
    return np.dot(y_puntos, L)

# --- Ejercicio 2.1 ---
if __name__ == "__main__":
    # Datos: x^2 + 1 (por ejemplo)
    x_datos = np.array([1.0, 3.0, 5.0])
    y_datos = np.array([2.0, 10.0, 26.0])

    x_interp = 4.0
    resultado = lagrange_vectorizado(x_datos, y_datos, x_interp)

    print("--- Resultado del Ejercicio 2.1 ---")
    print(f"Puntos conocidos: x={x_datos}, y={y_datos}")
    print(f"Interpolación en x = {x_interp}")
    print(f"Resultado: {resultado:.4f}")

    # Verificación rápida:
    # Si la función es f(x) = x^2 + 1
    # f(4) = 4^2 + 1 = 17
