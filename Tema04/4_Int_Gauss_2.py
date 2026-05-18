import math
from cuadratura_gaussiana_base import cuadratura_gaussiana

if __name__ == "__main__":
    print("=== EJERCICIO 2: INTEGRACIÓN DE FUNCIONES TRASCENDENTES ===")
    print("Evaluando f(x) = exp(-x^2) en el rango [0, 1]\n")
    
    def f_trascendente(x):
        return math.exp(-(x ** 2))
        
    a, b = 0.0, 1.0
    
    # Valor de referencia con alta precisión (calculado vía funciones especiales de error erf)
    valor_real = 0.7468241328
    
    # 1. Evaluación con n = 2 puntos
    res_n2 = cuadratura_gaussiana(f_trascendente, a, b, n=2)
    err_n2 = abs(valor_real - res_n2)
    
    # 2. Evaluación con n = 3 puntos
    res_n3 = cuadratura_gaussiana(f_trascendente, a, b, n=3)
    err_n3 = abs(valor_real - res_n3)
    
    print(f"-> Valor de Referencia Real: {valor_real:.10f}\n")
    print(f"-> Esquema Gauss n=2: Resultado = {res_n2:.10f} | Error Absoluto = {err_n2:.2e}")
    print(f"-> Esquema Gauss n=3: Resultado = {res_n3:.10f} | Error Absoluto = {err_n3:.2e}")
    
    print("\nNota: Observa cómo con solo 3 evaluaciones (n=3), el error cae al orden de 10^-5.")
    print("Para lograr esto con el Trapecio, se necesitarían decenas de subintervalos.")
