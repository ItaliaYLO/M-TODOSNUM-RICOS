from newton_raphson_base import newton_raphson

def f(x):
    return x**2 - 4

def df(x):
    return 2*x

if __name__ == "__main__":
    print("=== CASO 03: DEMOSTRACIÓN DE CONVERGENCIA CUADRÁTICA ===")
    print("Función: f(x) = x^2 - 4\n")
    
    x_semilla = 6.0  # Empezamos lejos de la raíz (que es 2) para ver la velocidad
    newton_raphson(f, df, x_semilla, tol=1e-6)
