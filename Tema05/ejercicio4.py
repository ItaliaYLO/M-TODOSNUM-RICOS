import numpy as np

def calcular_newton_polinomio(x, y):
    """
    Calcula los coeficientes de Newton de manera eficiente.
    """
    n = len(x)
    # Inicializamos la base de los coeficientes con los valores de y
    coef = np.array(y, dtype=float)
    
    for j in range(1, n):
        # Actualizamos los coeficientes de atrás hacia adelante
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
            
    return coef

def predecir_valor(coef, x_nodos, x_objetivo):
    """
    Evalúa el punto usando el método acumulativo.
    """
    n = len(coef)
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x_objetivo - x_nodos[i]) + coef[i]
    return resultado

# --- Datos del Sistema ---
tiempo = np.array([0, 2, 5, 6, 9], dtype=float)
presion = np.array([10, 14, 22, 28, 45], dtype=float)
t_buscado = 4

# 1. Obtención de coeficientes (b0, b1, b2, b3, b4)
b = calcular_newton_polinomio(tiempo, presion)

# 2. Estimación del valor
p_estimada = predecir_valor(b, tiempo, t_buscado)

# --- Salida de Resultados ---
print(f"--- Análisis de Presión (Ejercicio 4) ---")
print(f"Coeficientes calculados: {b}")
print(f"Resultado: a los {t_buscado}s, la presión es de {p_estimada:.2f} psi")

# Validación lógica simple
if presion[1] < p_estimada < presion[2]:
    print("Estado: La estimación es coherente con el intervalo [2s, 5s].")
else:
    print("Estado: Revisar, el valor está fuera del rango esperado.")
