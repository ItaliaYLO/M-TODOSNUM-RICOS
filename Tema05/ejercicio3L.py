import numpy as np

def interpolar_lagrange(x_puntos, y_puntos, x_objetivo):
    """
    Calcula la interpolación de Lagrange de forma compacta.
    """
    n = len(x_puntos)
    total = 0
    for i in range(n):
        # Creamos una lista de los índices excepto el actual 'i'
        indices = [j for j in range(n) if j != i]
        
        # Calculamos el producto de (x - xj) / (xi - xj)
        terminos = (x_objetivo - x_puntos[indices]) / (x_puntos[i] - x_puntos[indices])
        L_i = np.prod(terminos)
        
        total += y_puntos[i] * L_i
    return total

# --- Configuración del Experimento (Datos de log10) ---
x_datos = np.array([1.0, 4.0, 6.0])
y_datos = np.log10(x_datos)
objetivo = 2.5

# Cálculo
res_lagrange = interpolar_lagrange(x_datos, y_datos, objetivo)
valor_real = np.log10(objetivo)

# --- Reporte de Resultados ---
print(f"--- Comparativa Lagrange ---")
print(f"Resultado Lagrange: {res_lagrange:.6f}")
print(f"Valor Real log10:   {valor_real:.6f}")
print(f"Diferencia:         {abs(res_lagrange - valor_real):.2e}")

print("\nConclusión: El resultado coincide con el de Newton porque el polinomio")
print("interpolador de grado n es único para un conjunto de n+1 puntos.")
