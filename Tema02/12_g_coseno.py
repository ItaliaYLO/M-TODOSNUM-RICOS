import math
from punto_fijo_base import punto_fijo

# Ecuación original: cos(x) - x = 0
# Despeje g(x): x = cos(x)
def g(x):
    return math.cos(x)

if __name__ == "__main__":
    print("=== CASO 02: COSENO ITERATIVO TRASCENDENTAL ===")
    print("Función g(x) = cos(x)\n")
    
    x_semilla = 0.5
    punto_fijo(g, x_semilla, tol=1e-5)
