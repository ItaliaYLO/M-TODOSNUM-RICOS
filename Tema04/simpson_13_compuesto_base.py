def simpson_13_compuesto(f, a, b, n):
    """
    Implementación de la Regla de Simpson 1/3 Compuesta.
    f : Función continua a integrar.
    a : Límite inferior de integración.
    b : Límite superior de integración.
    n : Número de subintervalos (DEBE SER ESTRICTAMENTE PAR).
    """
    # Validación matemática obligatoria de la Regla de Simpson 1/3
    if n % 2 != 0:
        raise ValueError("El número de subintervalos 'n' debe ser un número par para aplicar la Regla de Simpson 1/3.")
    if n <= 0:
        raise ValueError("El número de subintervalos 'n' debe ser un entero positivo.")
        
    h = (b - a) / n
    
    suma_impares = 0.0
    suma_pares = 0.0
    
    # Recorrido de nodos intermedios discriminando por su índice algebraico
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            suma_pares += f(xi)     # Coeficiente de peso 2
        else:
            suma_impares += f(xi)   # Coeficiente de peso 4
            
    # Estructura formal de la fórmula ponderada de Simpson
    integral_aproximada = (h / 3.0) * (f(a) + 4.0 * suma_impares + 2.0 * suma_pares + f(b))
    
    return integral_aproximada
