from biseccion_base import biseccion

# Definimos la función cuadrática
def f(x):
    return x**2 - 4*x - 2

if __name__ == "__main__":
    print("=== CASO 01: POLINOMIO CUADRÁTICO ===")
    print("Función: f(x) = x^2 - 4x - 2\n")
    
    intervalo_a = 4.0
    intervalo_b = 5.0
    
    biseccion(f, intervalo_a, intervalo_b, tol=1e-4)
