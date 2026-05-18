from punto_fijo_base import punto_fijo

# Ecuación original: x^2 - 2x - 5 = 0
# Despeje g(x): x(x - 2) = 5 -> x = 5 / (x - 2)
def g(x):
    return 5 / (x - 2)

if __name__ == "__main__":
    print("=== CASO 05: DESPEJE FRACCIONARIO O RACIONAL ===")
    print("Función g(x) = 5 / (x - 2)\n")
    
    x_semilla = 4.0
    punto_fijo(g, x_semilla, tol=1e-5)
