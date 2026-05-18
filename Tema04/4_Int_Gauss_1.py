from cuadratura_gaussiana_base import cuadratura_gaussiana

if __name__ == "__main__":
    print("=== EJERCICIO 1: CUADRATURA GAUSSIANA DE 2 PUNTOS ===")
    print("Evaluación exacta sobre f(x) = 3x^2 + 2x + 1 en el intervalo [0, 2]\n")
    
    def f_polinomio(x):
        return 3.0 * (x ** 2) + 2.0 * x + 1.0
        
    a = 0.0
    b = 2.0
    
    # Integración con solo 2 evaluaciones de función
    resultado_num = cuadratura_gaussiana(f_polinomio, a, b, n=2)
    
    # Solución analítica teórica: [x^3 + x^2 + x] evaluado de 0 a 2 = 8 + 4 + 2 = 14.0
    resultado_real = 14.0
    error_abs = abs(resultado_real - resultado_num)
    
    print(f"-> Puntos de Gauss evaluados (n): 2")
    print(f"-> Resultado Numérico Calculado : {resultado_num:.8f}")
    print(f"-> Resultado Analítico Teórico  : {resultado_real:.8f}")
    print(f"-> Error Absoluto Residual     : {error_abs:.2e} (¡Cero matemático!)")
