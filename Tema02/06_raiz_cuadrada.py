from regla_falsa_base import regla_falsa

# f(x) = x^2 - 2 (Su raíz positiva es raíz de 2)
def f(x):
    return x**2 - 2

if __name__ == "__main__":
    print("=== CASO 01: RAÍZ CUADRADA DE 2 ===")
    print("Función: f(x) = x^2 - 2\n")
    
    intervalo_a = 1.0
    intervalo_b = 2.0
    
    regla_falsa(f, intervalo_a, intervalo_b, tol=1e-5)
