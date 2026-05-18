import math
from secante_base import secante

def f(x):
    return math.cos(x) - x

if __name__ == "__main__":
    print("=== CASO 02: FUNCIÓN TRASCENDENTAL ===")
    print("Función: f(x) = cos(x) - x\n")
    
    punto_x0 = 0.0
    punto_x1 = 1.0
    
    secante(f, punto_x0, punto_x1, tol=1e-5)
