import math
from regla_falsa_base import regla_falsa

def f(x):
    return 2*x - math.exp(-x)

if __name__ == "__main__":
    print("=== CASO 04: FUNCIÓN COMBINADA ===")
    print("Función: f(x) = 2x - e^(-x)\n")
    
    intervalo_a = 0.0
    intervalo_b = 1.0
    
    regla_falsa(f, intervalo_a, intervalo_b, tol=1e-5)
