import math
from trapecio_compuesto_base import trapecio_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 3: ANÁLISIS GLOBAL DE CONVERGENCIA ===")
    print("Estudio del comportamiento del error al refinar la malla de trapecios.\n")
    print("Función: f(x) = e^x  |  Límites: [0, 1]  |  Valor Exacto ≈ 1.71828183\n")
    
    def f_exp(x):
        return math.exp(x)
        
    a, b = 0.0, 1.0
    integral_real = math.exp(1.0) - math.exp(0.0)
    
    # Lista con diferentes niveles de discretización
    lista_n = [2, 4, 8, 16, 32, 64]
    
    print(f"{'Subintervalos (n)':<20}{'Resultado Numérico':<24}{'Error Absoluto':<18}{'Factor de Mejora'}")
    print("-" * 78)
    
    error_previo = None
    
    for n in lista_n:
        resultado_num = trapecio_compuesto(f_exp, a, b, n)
        error_actual = abs(integral_real - resultado_num)
        
        if error_previo is not None:
            factor = error_previo / error_actual
            print(f"{n:<20}{resultado_num:<24.8f}{error_actual:<18.2e}{factor:.2f}x")
        else:
            print(f"{n:<20}{resultado_num:<24.8f}{error_actual:<18.2e}{'---':<12}")
            
        error_previo = error_actual
        
    print("\nConclusión: Nota cómo cada vez que duplicamos 'n', el error se reduce a la cuarta parte (Factor ~ 4.0).")
    print("Esto comprueba matemáticamente que el método compuesto del trapecio tiene un orden de error O(h²).")
