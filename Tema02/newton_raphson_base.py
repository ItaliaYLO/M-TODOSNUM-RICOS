def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de Newton-Raphson.
    f: Función original a evaluar f(x)
    df: Derivada analítica de la función f'(x)
    x0: Valor semilla inicial
    tol: Tolerancia del error admisible
    """
    print(f"{'Iter':<6}{'xi':<12}{'f(xi)':<12}{'f\'(xi)':<12}{'Error':<12}")
    print("-" * 54)

    xi = x0
    for i in range(1, max_iter + 1):
        f_xi = f(xi)
        df_xi = df(xi)

        # Protección crítica: Evitar división por cero (tangente horizontal)
        if abs(df_xi) < 1e-12:
            print(f"\n-> Error: Derivada cercana a cero (f'(xi) = {df_xi:.6e}) en la iteración {i}.")
            print("El método no puede continuar. Intenta con otra semilla x0.")
            return None

        # Fórmula matemática de Newton-Raphson
        xi_siguiente = xi - (f_xi / df_xi)
        error = abs(xi_siguiente - xi)

        print(f"{i:<6}{xi:<12.6f}{f_xi:<12.5e}{df_xi:<12.5e}{error:<12.6e}")

        # Criterio de parada
        if error < tol:
            print(f"\n-> Convergencia alcanzada en la iteración {i}. Raíz aprox: {xi_siguiente:.6f}")
            return xi_siguiente

        xi = xi_siguiente

    print("\n-> Se alcanzó el límite máximo de iteraciones sin convergencia.")
    return xi
