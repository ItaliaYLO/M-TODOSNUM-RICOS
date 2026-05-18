import math

def cuadratura_gaussiana(f, a, b, n=2):
    """
    Implementación del Método de la Cuadratura Gaussiana para n=2 y n=3 puntos.
    Mapea el intervalo [a, b] al intervalo estándar [-1, 1].
    f : Función continua a integrar.
    a : Límite inferior de integración.
    b : Límite superior de integración.
    n : Número de puntos de Gauss (soportado: 2 o 3).
    """
    if n not in [2, 3]:
        raise ValueError("Esta implementación solo soporta n=2 o n=3 puntos de Gauss.")
        
    # Tabulación oficial de Raíces (t) y Pesos (w) de los Polinomios de Legendre
    if n == 2:
        # Raíz: 1 / sqrt(3)
        t = [-1.0 / math.sqrt(3.0), 1.0 / math.sqrt(3.0)]
        w = [1.0, 1.0]
    elif n == 3:
        # Raíz: sqrt(3/5)
        t = [-math.sqrt(3.0 / 5.0), 0.0, math.sqrt(3.0 / 5.0)]
        w = [5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]
        
    # Aplicación formal del Cambio de Variable Lineal (Mapeo de intervalo)
    suma_ponderada = 0.0
    for i in range(n):
        # Transformación del punto t_i en el dominio [-1, 1] al punto x_i en [a, b]
        xi = ((b - a) / 2.0) * t[i] + ((b + a) / 2.0)
        # Acumulación: peso * función evaluada en el punto transformado
        suma_ponderada += w[i] * f(xi)
        
    # Multiplicación final por el diferencial transformado (Jacobiano del mapeo)
    integral_aproximada = ((b - a) / 2.0) * suma_ponderada
    
    return integral_aproximada
