import numpy as np

def calcular_tabla_newton(x, y):
    """
    Calcula los coeficientes de Newton de forma in-place para ahorrar memoria.
    """
    coef = np.array(y, dtype=float)
    n = len(x)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def interpolar_newton(coef, x_puntos, x_objetivo):
    """
    Evalúa el polinomio de Newton usando el algoritmo de Horner.
    """
    n = len(coef)
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x_objetivo - x_puntos[i]) + coef[i]
    return resultado

# --- Datos del Fluido ---
# Temperatura (C) y Viscosidad (10^-3 Pa*s)
temp = np.array([0, 10, 20, 30, 40], dtype=float)
visc = np.array([1.787, 1.307, 1.002, 0.797, 0.653], dtype=float)

t_objetivo = 25

# 1. Obtención de coeficientes
b = calcular_tabla_newton(temp, visc)

# 2. Evaluación
v_estimada = interpolar_newton(b, temp, t_objetivo)

# --- Resultado y Análisis ---
print(f"--- Análisis de Viscosidad (Ejercicio 5) ---")
print(f"Temperatura objetivo: {t_objetivo}°C")
print(f"Viscosidad calculada: {v_estimada:.4f} x 10^-3 Pa*s")

# Pequeña validación científica
if visc[3] < v_estimada < visc[2]:
    print("\n[✓] El resultado es coherente: disminuye al aumentar la temperatura.")
else:
    print("\n[!] Alerta: El resultado no sigue la tendencia física esperada.")
