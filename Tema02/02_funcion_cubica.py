from biseccion_base import biseccion

# Definimos la función cúbica
def f(x):
    return x**3 - x - 2

if __name__ == "__main__":
    print("=== CASO 02: FUNCIÓN CÚBICA ===")
    print("Función: f(x) = x^3 - x - 2\n")
    
    intervalo_a = 1.0
    intervalo_b = 2.0
    
    biseccion(f, intervalo_a, intervalo_b, tol=1e-5)
