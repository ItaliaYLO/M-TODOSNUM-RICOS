import numpy as np

def interpolador_newton(x_nodos, y_nodos, x_objetivo):
    """
    Calcula los coeficientes y evalúa el polinomio en un solo paso
    para simplificar el flujo del ejercicio.
    """
    n = len(x_nodos)
    # Cálculo de la tabla de diferencias divididas (compacto)
    coef = np.copy(y_nodos).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x_nodos[i] - x_nodos[i-j])
    
    # Evaluación (Esquema de Horner)
    res = coef[-1]
    for i in range(n - 2, -1, -1):
        res = res * (x_objetivo - x_nodos[i]) + coef[i]
    return res

# --- Configuración del Experimento ---
x_datos = np.array([1.0, 4.0, 6.0])
y_datos = np.log10(x_datos)
x_buscado = 2.5
valor_real = np.log10(x_buscado)

# 1. Estimación Lineal (Grado 1) - Usando los primeros 2 puntos
res_lineal = interpolador_newton(x_datos[:2], y_datos[:2], x_buscado)

# 2. Estimación Cuadrática (Grado 2) - Usando los 3 puntos
res_cuad = interpolador_newton(x_datos, y_datos, x_buscado)

# --- Presentación de Resultados ---
print(f"{'MÉTODO':<15} | {'VALOR':<12} | {'ERROR ABSOLUTO':<15}")
print("-" * 48)
print(f"{'Real':<15} | {valor_real:<12.6f} | {'0.000000':<15}")
print(f"{'Lineal (n=1)':<15} | {res_lineal:<12.6f} | {abs(valor_real - res_lineal):<15.6f}")
print(f"{'Cuadrática (n=2)':<15} | {res_cuad:<12.6f} | {abs(valor_real - res_cuad):<15.6f}")

# Cálculo del error relativo porcentual de la mejor aproximación
error_rel = abs((valor_real - res_cuad) / valor_real) * 100
print(f"\nNota: El error relativo de la cuadrática es de apenas {error_rel:.2f}%")
