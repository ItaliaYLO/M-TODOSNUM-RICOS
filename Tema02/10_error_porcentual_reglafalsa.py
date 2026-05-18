def regla_falsa_porcentual(f, a, b, tol_porcentual=0.01, max_iter=100):
    if f(a) * f(b) >= 0:
        return None

    print(f"{'Iter':<6}{'xr':<12}{'f(xr)':<15}{'Error Porcentual':<18}")
    print("-" * 55)

    xr = a
    for i in range(1, max_iter + 1):
        xr_viejo = xr
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        f_xr = f(xr)
        
        # Error relativo porcentual aproximado
        error_pct = abs((xr - xr_viejo) / xr) * 100 if xr != 0 and i > 1 else float('inf')

        print(f"{i:<6}{xr:<12.6f}{f_xr:<15.6e}{f'{error_pct:.4f}%' if i>1 else '---':<18}")

        if abs(f_xr) < 1e-15 or error_pct < tol_porcentual:
            print(f"\n-> Convergencia al {tol_porcentual}% alcanzada en la iteración {i}.")
            print(f"Raíz aproximada: {xr:.6f}")
            return xr

        if f(a) * f_xr < 0:
            b = xr
        else:
            a = xr

# Función de prueba para el caso 5
def f_caso5(x):
    return x**4 - 3

if __name__ == "__main__":
    print("=== CASO 05: ANÁLISIS DE ERROR PORCENTUAL ===")
    print("Función: f(x) = x^4 - 3\n")
    
    # Tolerancia establecida al 0.05% de error admisible
    regla_falsa_porcentual(f_caso5, 1.0, 2.0, tol_porcentual=0.05)
