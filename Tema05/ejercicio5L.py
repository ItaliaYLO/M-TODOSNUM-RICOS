import numpy as np

def interpolar_lagrange(x_puntos, y_puntos, x_objetivo):
    """
    Calcula la interpolación de Lagrange utilizando 
    comprensión de listas para mayor claridad.
    """
    n = len(x_puntos)
    
    def base_lagrange(i):
        # Calcula L_i(x) omitiendo el índice i
        terminos = [(x_objetivo - x_puntos[j]) / (x_puntos[i] - x_puntos[j]) 
                    for j in range(n) if i != j]
        return np.prod(terminos)

    # Sumatoria y_i * L_i(x)
    return sum(y_puntos[i] * base_lagrange(i) for i in range(n))

# --- Datos del Lanzamiento ---
# Tiempo (s) y Altura (m)
tiempo = np.array([0, 1.5, 3.0, 4.5, 6.0], dtype=float)
altura = np.array([0, 42.5, 70.2, 85.4, 90.0], dtype=float)

t_eval = 2.0
h_estimada = interpolar_lagrange(tiempo, altura, t_eval)

# --- Reporte de Resultados ---
print(f"--- Análisis de Altura (Ejercicio 2.5) ---")
print(f"Tiempo evaluado: {t_eval} segundos")
print(f"Altura estimada: {h_estimada:.2f} metros")

# Validación física: El proyectil está subiendo
if h_estimada > altura[1] and h_estimada < altura[2]:
    print("\n[INFO] El valor es coherente con el intervalo de tiempo [1.5s, 3.0s].")
