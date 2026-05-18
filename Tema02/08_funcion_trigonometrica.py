import math
from regla_falsa_base import regla_falsa

def f(x):
    return x * math.sin(x) - 1

if __name__ == "__main__":
    print("=== CASO 03: FUNCIÓN TRIGONOMÉTRICA ===")
    print("Función: f(x) = x * sin(x) - 1\n")
    
    intervalo_a = 0.0
    intervalo_b = 2.0
    
    regla_falsa(f, intervalo_a, intervalo_b, tol=1e-5)
