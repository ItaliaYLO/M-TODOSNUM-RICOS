if __name__ == "__main__":
    print("=== EJERCICIO 2: CÁLCULO DE LA ACELERACIÓN (SEGUNDA DERIVADA) ===")
    print("Aproximación de la segunda derivada s''(t) mediante un esquema central.\n")
    
    # Función de trayectoria de un objeto dinámico: s(t) = t^3 + 2*t^2 + t
    def posicion(t):
        return (t ** 3) + (2.0 * (t ** 2)) + t
        
    t0 = 1.5  # Tiempo donde deseamos la aceleración instantánea
    h = 0.05  # Paso temporal corto
    
    # Ecuación de Diferencias Finitas Centrales para Segunda Derivada (3 puntos de control):
    # f''(x) ≈ (f(x+h) - 2*f(x) + f(x-h)) / h²
    num_aceleracion = (posicion(t0 + h) - 2.0 * posicion(t0) + posicion(t0 - h)) / (h ** 2)
    
    # Validación matemática:
    # s'(t) = 3*t^2 + 4*t + 1  =>  s''(t) = 6*t + 4
    aceleracion_real = 6.0 * t0 + 4.0
    
    print(f"-> Punto de evaluación t = {t0} s (h = {h} s)")
    print(f"-> Aceleración Numérica Calculada: {num_aceleracion:.6f} m/s²")
    print(f"-> Aceleración Analítica Real    : {aceleracion_real:.6f} m/s²")
    print(f"-> Error de Truncamiento Neto     : {abs(aceleracion_real - num_aceleracion):.2e}")
