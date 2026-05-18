from punto_fijo_base import punto_fijo

# Ecuación original: x^2 - x - 2 = 0
# Despeje g(x) alternativo: x = x^2 - 2
# Nota: Este despeje va a divergir porque la derivada g'(x) = 2x evaluada en la raíz es mayor a 1.
def g_divergente(x):
    return x**2 - 2

if __name__ == "__main__":
    print("=== CASO 03: DEMOSTRACIÓN DE DIVERGENCIA ===")
    print("Función g(x) = x^2 - 2 (Incumple |g'(x)| < 1)\n")
    
    x_semilla = 1.5
    # Limitamos las iteraciones máximas porque los valores crecerán infinitamente
    punto_fijo(g_divergente, x_semilla, tol=1e-5, max_iter=10)
