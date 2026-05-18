def punto_fijo(g, x0, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de Iteración de Punto Fijo.
    g: Función de iteración despejada x = g(x)
    x0: Valor inicial de semilla
    tol: Tolerancia del error absoluto/relativo admisible
    """
    print(f"{'Iter':<6}{'xi':<15}{'g(xi)':<15}{'Error Absoluto':<15}")
    print("-" * 55)

    xi = x0
    for i in range(1, max_iter + 1):
        # Calcular el siguiente valor iterativo
        try:
            xi_siguiente = g(xi)
        except (ValueError, OverflowError, ZeroDivisionError):
            print(f"\n-> Error matemático en iteración {i}. El método divergió por completo.")
            return None
            
        error = abs(xi_siguiente - xi)

        print(f"{i:<6}{xi:<15.6f}{xi_siguiente:<15.6f}{error:<15.6e}")

        # Comprobar el criterio de parada por tolerancia
        if error < tol:
            print(f"\n-> Convergencia alcanzada en la iteración {i}. Punto Fijo aproximado: {xi_siguiente:.6f}")
            return xi_siguiente

        xi = xi_siguiente

    print("\n-> Se alcanzó el límite máximo de iteraciones. El método podría estar divergiendo o requiere más pasos.")
    return xi
