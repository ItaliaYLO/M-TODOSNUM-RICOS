from secante_base import secante

def f(x):
    return x**3 - 2*x - 5

if __name__ == "__main__":
    print("=== CASO 01: SECANTE EN POLINOMIOS ===")
    print("Función: f(x) = x^3 - 2x - 5\n")
    
    punto_x0 = 1.0
    punto_x1 = 2.0
    
    secante(f, punto_x0, punto_x1, tol=1e-5)
