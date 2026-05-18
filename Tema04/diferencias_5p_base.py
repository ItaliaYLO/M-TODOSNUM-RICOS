def diferencia_central_5p(f, x0, h=0.01):
    """
    Implementación de la Regla de Diferencias de Cinco Puntos (Variante Central).
    Garantiza un orden de convergencia de cuarto orden O(h^4).
    f  : Función matemática a derivar.
    x0 : Punto de evaluación de la derivada.
    h  : Tamaño de paso base.
    """
    if h <= 0:
        raise ValueError("El tamaño de paso 'h' debe ser estrictamente mayor que cero.")
        
    # Evaluación de los 4 nodos simétricos requeridos por el algoritmo
    f_mas_2h = f(x0 + 2.0 * h)
    f_mas_h  = f(x0 + h)
    f_menos_h = f(x0 - h)
    f_menos_2h = f(x0 - 2.0 * h)
    
    # Aplicación de la fórmula de coeficientes ponderados
    numerador = -f_mas_2h + 8.0 * f_mas_h - 8.0 * f_menos_h + f_menos_2h
    denominador = 12.0 * h
    
    return numerador / denominador
