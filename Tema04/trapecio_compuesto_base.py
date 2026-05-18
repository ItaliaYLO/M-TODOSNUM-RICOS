def trapecio_compuesto(f, a, b, n):
    """
    Implementación del Método del Trapecio en su variante Compuesta.
    f : Función matemática continua a integrar (objeto ejecutable).
    a : Límite inferior de integración.
    b : Límite superior de integración.
    n : Número de subintervalos o segmentos (debe ser un entero positivo).
    """
    if n <= 0:
        raise ValueError("El número de subintervalos 'n' debe ser un entero mayor que cero.")
        
    # 1. Cálculo del ancho de cada subintervalo
    h = (b - a) / n
    
    # 2. Inicialización de la suma con los extremos f(a) y f(b)
    suma_interior = 0.0
    
    # 3. Sumatoria de los nodos internos (multiplicados por 2)
    for i in range(1, n):
        xi = a + i * h
        suma_interior += f(xi)
        
    # 4. Aplicación de la fórmula final ponderada
    integral_aproximada = (h / 2.0) * (f(a) + 2.0 * suma_interior + f(b))
    
    return integral_aproximada
