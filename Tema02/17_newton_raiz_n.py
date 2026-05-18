from newton_raphson_base import newton_raphson

# Si queremos la raíz cúbica de 25, planteamos: x = v^1/3 -> x^3 = 25 -> x^3 - 25 = 0
def f(x):
    return x**3 - 25

# Derivada analítica: f'(x) = 3x^2
def df(x):
    return 3*x**2

if __name__ == "__main__":
    print("=== CASO 02: CÁLCULO DE RAÍZ CÚBICA DE 25 ===")
    print("Función: f(x) = x^3 - 25\n")
    
    x_semilla = 3.0  # Sabemos que 3^3 es 27, por lo que la raíz está cerca de 3
    newton_raphson(f, df, x_semilla, tol=1e-6)
