def diferencia_central_3p(f, x0, h=0.01):
    """
    Implementación de la Regla de Diferencias de Tres Puntos (Variante Central).
    f  : Función de Python que se desea derivar (debe aceptar un flotante y regresar un flotante).
    x0 : Punto en el cual evaluar la primera derivada.
    h  : Tamaño de paso o incremento espacial (valor por defecto 0.01).
    """
    if h <= 0:
        raise ValueError("El tamaño de paso 'h' debe ser estrictamente mayor que cero.")
        
    # Aplicación estricta de la fórmula de diferencias centrales de tres puntos
    numerador = f(x0 + h) - f(x0 - h)
    denominador = 2.0 * h
    
    return numerador / denominador
