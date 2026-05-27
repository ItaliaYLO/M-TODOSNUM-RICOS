import numpy as np

def interpolacion_lagrange(x_puntos, y_puntos, x_objetivo):
    """
    Calcula el valor interpolado usando el método de Lagrange
    optimizando el cálculo de los polinomios base con NumPy.
    """
    n = len(x_puntos)
    
    def calcular_L(i, x):
        # Creamos una lista de términos (x - xj) / (xi - xj) omitiendo i == j
        terminos = [(x - x_puntos[j]) / (x_puntos[i] - x_puntos[j]) 
                    for j in range(n) if i != j]
        return np.prod(terminos) # Producto de todos los elementos de la lista

    # Sumatoria de y_i * L_i(x)
    return sum(y_puntos[i] * calcular_L(i, x_objetivo) for i in range(n))

# --- Prueba del código ---
if __name__ == "__main__":
    # Datos de prueba: f(x) = x^2 + 1
    x_test = np.array([0, 2, 4])
    y_test = np.array([1, 5, 17])
    
    punto_a_evaluar = 3
    resultado = interpolacion_lagrange(x_test, y_test, punto_a_evaluar)
    
    print(f"--- Resultado ---")
    print(f"Para x = {punto_a_evaluar}, el valor interpolado es: {resultado}")
