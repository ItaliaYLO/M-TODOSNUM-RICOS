import math
from biseccion_base import biseccion

# Definimos la función trigonométrica trascendental
def f(x):
    return math.cos(x) - x

if __name__ == "__main__":
    print("=== CASO 03: FUNCIÓN TRASCENDENTAL ===")
    print("Función: f(x) = cos(x) - x\n")
    
    intervalo_a = 0.0
    intervalo_b = 1.0
    
    biseccion(f, intervalo_a, intervalo_b, tol=1e-5)
