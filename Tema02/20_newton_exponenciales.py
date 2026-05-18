import math
from newton_raphson_base import newton_raphson

def f(x):
    return math.exp(-x) - x

# Derivada analítica: f'(x) = -e^(-x) - 1
def df(x):
    return -math.exp(-x) - 1

if __name__ == "__main__":
    print("=== CASO 05: FUNCIÓN EXPONENCIAL ===")
    print("Función: f(x) = e^(-x) - x\n")
    
    x_semilla = 0.0
    newton_raphson(f, df, x_semilla, tol=1e-5)
