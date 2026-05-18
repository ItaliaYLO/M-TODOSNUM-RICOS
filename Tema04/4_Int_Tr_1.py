from trapecio_compuesto_base import trapecio_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 1: ÁREA BAJO UNA FUNCIÓN CUADRÁTICA ===")
    print("Evaluación sobre f(x) = x^2  |  Intervalo [0, 2]  |  n = 4\n")
    
    # Definición de la parábola
    def f_cuadratica(x):
        return x ** 2
        
    a = 0.0
    b = 2.0
    n = 4
    
    # 1. Integración numérica
    resultado_num = trapecio_compuesto(f_cuadratica, a, b, n)
    
    # 2. Solución analítica exacta: (x^3)/3 evaluado de 0 a 2 = 8/3
    resultado_real = 8.0 / 3.0
    error_abs = abs(resultado_real - resultado_num)
    
    print(f"-> Ancho del segmento (h): {(b-a)/n}")
    print(f"-> Integral Numérica (Trapecio): {resultado_num:.6f}")
    print(f"-> Integral Analítica Real     : {resultado_real:.6f}")
    print(f"-> Error Absoluto Calculado    : {error_abs:.6f}")
