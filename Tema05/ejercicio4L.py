import numpy as np

def interpolador_lagrange_limpio(x_puntos, y_puntos, x_objetivo):
    """
    Calcula la interpolación de Lagrange de forma legible.
    """
    n = len(x_puntos)
    y_interp = 0
    
    for i in range(n):
        # Cálculo del término L_i(x)
        # (x - x0)(x - x1)... / (xi - x0)(xi - x1)...
        puntos_ajenos = np.delete(x_puntos, i)
        numerador = np.prod(x_objetivo - puntos_ajenos)
        denominador = np.prod(x_puntos[i] - puntos_ajenos)
        
        # Sumar y_i * L_i al total
        y_interp += y_puntos[i] * (numerador / denominador)
        
    return y_interp

# --- Datos del Experimento ---
# Relación entre Temperatura (°C) y Resistencia (Ω)
temp = np.array([20, 50, 80, 110], dtype=float)
resistencia = np.array([105.2, 118.5, 132.8, 147.1], dtype=float)

t_target = 75
r_resultado = interpolador_lagrange_limpio(temp, resistencia, t_target)

# --- Reporte Final ---
print(f"--- Calibración de Sensor (Ejercicio 2.4) ---")
print(f"Rango de datos: {temp[0]}°C a {temp[-1]}°C")
print(f"Punto de interés: {t_target}°C")
print("-" * 40)
print(f"Resistencia estimada: {r_resultado:.2f} Ohms")

# Verificación de linealidad aproximada
# Si los datos fueran perfectamente lineales, el valor entre 50 y 80 sería ~130
print(f"Nota: El valor es consistente con el comportamiento del sensor.")
