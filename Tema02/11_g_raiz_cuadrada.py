import math
from punto_fijo_base import punto_fijo

# Ecuación original: x^2 - x - 2 = 0
# Despeje g(x): x = sqrt(x + 2)
def g(x):
    return math.sqrt(x + 2)

if __name__ == "__main__":
    print("=== CASO 01: DESPEJE ESTABLE CON RAÍZ CUADRADA ===")
    print("Función g(x) = sqrt(x + 2)\n")
    
    x_semilla = 1.0
    punto_fijo(g, x_semilla, tol=1e-5)
