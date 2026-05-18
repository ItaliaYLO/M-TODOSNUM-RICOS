import math
from simpson_13_compuesto_base import simpson_13_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 2: APLICACIÓN EN INGENIERÍA (LONGITUD DE ARCO) ===")
    print("Calculando la longitud real de un cable usando la regla de Simpson 1/3.\n")
    
    # Ecuación de la raíz de la derivada para la longitud de arco del cable
    # f(x) representa localmente la ecuación diferencial del colgamiento geométrico
    def integrando_longitud(x):
        # Representa la función interna: sqrt(1 + [sinh(x)]²) = cosh(x)
        # Usaremos una curva genérica compleja para forzar al método numérico:
        return math.sqrt(1.0 + (math.sinh(x / 10.0) ** 2))
        
    a = -10.0  # Torre izquierda (posición en metros)
    b = 10.0   # Torre derecha (posición en metros)
    n = 12     # Número par de divisiones de diseño
    
    longitud_cable = simpson_13_compuesto(integrando_longitud, a, b, n)
    
    print(f"-> Parámetros estructurales: Intervalo [{a}, {b}] metros | n = {n}")
    print(f"-> Longitud total calculada de la catenaria: {longitud_cable:.5f} metros")
