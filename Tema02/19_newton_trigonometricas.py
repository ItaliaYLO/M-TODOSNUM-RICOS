import math
from newton_raphson_base import newton_raphson

def f(x):
    return math.sin(x) - x**2

def df(x):
    return math.cos(x) - 2*x

if __name__ == "__main__":
    print("=== CASO 04: FUNCIÓN TRIGONOMÉTRICA TRASCENDENTAL ===")
    print("Función: f(x) = sin(x) - x^2\n")
    
    x_semilla = 1.0
    newton_raphson(f, df, x_semilla, tol=1e-5)
