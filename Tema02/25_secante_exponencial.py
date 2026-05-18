import math
from secante_base import secante

def f(x):
    return math.exp(-(x**2)) - x

if __name__ == "__main__":
    print("=== CASO 05: CASO EXPONENCIAL COMPLEJO ===")
    print("Función: f(x) = e^(-x^2) - x\n")
    
    punto_x0 = 0.0
    punto_x1 = 1.0
    
    secante(f, punto_x0, punto_x1, tol=1e-5)
