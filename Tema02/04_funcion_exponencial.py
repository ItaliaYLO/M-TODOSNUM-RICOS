import math
from biseccion_base import biseccion

# Definimos la función exponencial
def f(x):
    return math.exp(-x) - x

if __name__ == "__main__":
    print("=== CASO 04: FUNCIÓN EXPONENCIAL ===")
    print("Función: f(x) = e^(-x) - x\n")
    
    intervalo_a = 0.0
    intervalo_b = 1.0
    
    biseccion(f, intervalo_a, intervalo_b, tol=1e-5)
