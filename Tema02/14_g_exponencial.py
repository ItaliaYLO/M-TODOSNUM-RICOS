import math
from punto_fijo_base import punto_fijo

# Ecuación original: e^(-x) - x = 0
# Despeje g(x): x = e^(-x)
def g(x):
    return math.exp(-x)

if __name__ == "__main__":
    print("=== CASO 04: FUNCIÓN EXPONENCIAL AMORTIGUADA ===")
    print("Función g(x) = e^(-x)\n")
    
    x_semilla = 0.0
    punto_fijo(g, x_semilla, tol=1e-5)
