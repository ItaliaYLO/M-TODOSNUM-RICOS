from regla_falsa_base import regla_falsa

def f(x):
    return x**3 - 2*x - 5

if __name__ == "__main__":
    print("=== CASO 02: POLINOMIO DE GRADO 3 ===")
    print("Función: f(x) = x^3 - 2x - 5\n")
    
    intervalo_a = 2.0
    intervalo_b = 3.0
    
    regla_falsa(f, intervalo_a, intervalo_b, tol=1e-5)
