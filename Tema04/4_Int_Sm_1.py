from simpson_13_compuesto_base import simpson_13_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 1: EXACTITUD EN POLINOMIOS CÚBICOS ===")
    print("Evaluando f(x) = x^3 - 2x en el intervalo [1, 3] con n = 2\n")
    
    def f_cubica(x):
        return (x ** 3) - (2.0 * x)
        
    a, b = 1.0, 3.0
    n = 2  # Mínimo número de segmentos admisibles (es par)
    
    resultado_num = simpson_13_compuesto(f_cubica, a, b, n)
    
    # Solución analítica exacta calculada a mano:
    # Int(x^3 - 2x) = (x^4)/4 - x^2. Evaluado de 1 a 3:
    # (81/4 - 9) - (1/4 - 1) = (45/4) - (-3/4) = 48/4 = 12.0
    resultado_real = 12.0
    error_abs = abs(resultado_real - resultado_num)
    
    print(f"-> Segmentos utilizados (n): {n} (Paso h = {(b-a)/n})")
    print(f"-> Resultado aproximado numérico: {resultado_num:.8f}")
    print(f"-> Resultado exacto analítico  : {resultado_real:.8f}")
    print(f"-> Error Absoluto de Truncamiento: {error_abs:.2e} (¡Es cero teórico!)")
