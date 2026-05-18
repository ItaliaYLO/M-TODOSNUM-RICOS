def secante(f, x0, x1, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de la Secante.
    f: Función original a evaluar f(x)
    x0, x1: Dos valores iniciales de arranque (no requieren cambio de signo)
    tol: Tolerancia del error admisible
    """
    print(f"{'Iter':<6}{'xi-1':<12}{'xi':<12}{'xi+1':<12}{'f(xi+1)':<12}{'Error':<12}")
    print("-" * 66)

    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Protección crítica: Evitar división por cero (denominador nulo)
        if abs(f_x0 - f_x1) < 1e-12:
            print(f"\n-> Error: Denominador cercano a cero en la iteración {i} (f(x0) =~ f(x1)).")
            print("El método no puede continuar debido a una pendiente indeterminada.")
            return None

        # Fórmula matemática del Método de la Secante
        x_siguiente = x1 - (f_x1 * (x0 - x1)) / (f_x0 - f_x1)
        f_xsig = f(x_siguiente)
        
        error = abs(x_siguiente - x1)

        print(f"{i:<6}{x0:<12.6f}{x1:<12.6f}{x_siguiente:<12.6f}{f_xsig:<12.5e}{error:<12.6e}")

        # Criterio de parada
        if error < tol:
            print(f"\n-> Convergencia alcanzada en la iteración {i}. Raíz aprox: {x_siguiente:.6f}")
            return x_siguiente

        # Actualización de los puntos para la siguiente iteración
        x0 = x1
        x1 = x_siguiente

    print("\n-> Se alcanzó el límite máximo de iteraciones sin convergencia.")
    return x1
