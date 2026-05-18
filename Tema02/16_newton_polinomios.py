from newton_raphson_base import newton_raphson

# Función original
def f(x):
    return x**3 - 2*x - 5

# Derivada analítica: f'(x) = 3x^2 - 2
def df(x):
    return 3*x**2 - 2

if __name__ == "__main__":
    print("=== CASO 01: NEWTON EN POLINOMIOS ===")
    print("Función: f(x) = x^3 - 2x - 5\n")
    
    x_semilla = 2.0
    newton_raphson(f, df, x_semilla, tol=1e-5)
