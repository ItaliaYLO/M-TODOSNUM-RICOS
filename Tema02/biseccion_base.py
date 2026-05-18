def biseccion(f, a, b, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de Bisección.
    f: Función a evaluar
    a, b: Límites del intervalo inicial
    tol: Tolerancia del error tolerado
    """
    if f(a) * f(b) >= 0:
        print("Error: El intervalo no cumple con el Teorema de Bolzano (f(a)*f(b) >= 0).")
        return None

    print(f"{'Iter':<6}{'a':<12}{'b':<12}{'xr':<12}{'f(xr)':<12}{'Error':<12}")
    print("-" * 66)

    xr = a
    for i in range(1, max_iter + 1):
        xr_viejo = xr
        xr = (a + b) / 2
        f_xr = f(xr)
        
        # Calcular error relativo aproximado a partir de la iteración 2
        error = abs((xr - xr_viejo) / xr) if xr != 0 and i > 1 else float('inf')

        print(f"{i:<6}{a:<12.6f}{b:<12.6f}{xr:<12.6f}{f_xr:<12.6e}{error:<12.6e}")

        if abs(f_xr) < 1e-15 or error < tol:
            print(f"\n-> Convergencia alcanzada en la iteración {i}. Raíz aprox: {xr:.6f}")
            return xr

        # Validación del cambio de signo
        if f(a) * f_xr < 0:
            b = xr
        else:
            a = xr

    print("\n-> Se alcanzó el límite máximo de iteraciones sin convergencia absoluta.")
    return xr
