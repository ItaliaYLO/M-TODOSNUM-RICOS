import math
from diferencias_5p_base import diferencia_central_5p

if __name__ == "__main__":
    print("=== EJERCICIO 1: DERIVACIÓN DE FUNCIONES EXPONENCIALES ===")
    print("Función: f(x) = e^x * ln(x)  |  Punto: x0 = 2.0\n")
    
    def f_caso1(x):
        return math.exp(x) * math.log(x)
        
    x0 = 2.0
    h = 0.01
    
    # 1. Aproximación numérica (5 puntos)
    derivada_num = diferencia_central_5p(f_caso1, x0, h)
    
    # 2. Solución analítica exacta calculada mediante cálculo elemental:
    # f'(x) = e^x * ln(x) + e^x * (1/x)
    derivada_real = math.exp(x0) * math.log(x0) + math.exp(x0) * (1.0 / x0)
    
    error_abs = abs(derivada_real - derivada_num)
    
    print(f"-> Tamaño de paso (h): {h}")
    print(f"-> Derivada Numérica (5P): {derivada_num:.10f}")
    print(f"-> Derivada Analítica Real: {derivada_real:.10f}")
    print(f"-> Error Absoluto Neto  : {error_abs:.4e}")
