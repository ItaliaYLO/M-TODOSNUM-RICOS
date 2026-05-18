import math
from biseccion_base import biseccion

# Definimos la función logarítmica
def f(x):
    return math.log(x) + x - 2

if __name__ == "__main__":
    print("=== CASO 05: FUNCIÓN LOGARÍTMICA ===")
    print("Función: f(x) = ln(x) + x - 2\n")
    
    intervalo_a = 1.0
    intervalo_b = 2.0
    
    biseccion(f, intervalo_a, intervalo_b, tol=1e-5)
