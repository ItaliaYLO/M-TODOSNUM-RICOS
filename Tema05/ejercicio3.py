import numpy as np

def calcular_coeficientes(x, y):
    """Calcula la lista completa de coeficientes b_i para el grado máximo posible."""
    n = len(x)
    b = np.array(y, dtype=float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            b[i] = (b[i] - b[i-1]) / (x[i] - x[i-j])
    return b

def evaluar_grado_especifico(coef, x_nodos, x_objetivo, grado):
    """Evalúa el polinomio usando solo hasta el grado indicado."""
    # Tomamos solo los coeficientes necesarios para el grado deseado
    b_sub = coef[:grado + 1]
    res = b_sub[-1]
    for i in range(grado - 1, -1, -1):
        res = res * (x_objetivo - x_nodos[i]) + b_sub[i]
    return res

# --- Configuración del Experimento ---
x_puntos = np.array([1, 2, 3, 4, 5], dtype=float)
y_puntos = np.array([0.5, 2.0, 4.5, 8.0, 12.5]) # f(x) = 0.5 * x^2
x_target = 2.5

# Calculamos todos los coeficientes una sola vez (hasta grado 4)
todos_los_coef = calcular_coeficientes(x_puntos, y_puntos)

print(f"--- Análisis de Interpolación en x = {x_target} ---")
print(f"{'GRADO':<8} | {'PREDICCIÓN':<12} | {'ESTADO'}")
print("-" * 40)

for g in range(1, 4):
    pred = evaluar_grado_especifico(todos_los_coef, x_puntos, x_target, g)
    
    # Verificación de convergencia
    estado = "Creciendo" if g == 1 else "Estabilizado (Real)" if pred == 3.125 else "Calculando"
    print(f"Grado {g:<3} | {pred:<12.3f} | {estado}")

# Valor real para comparar
print("-" * 40)
print(f"Valor real f(2.5) = {0.5 * (2.5**2):.3f}")
