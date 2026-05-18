import math
from trapecio_compuesto_base import trapecio_compuesto
from simpson_13_compuesto_base import simpson_13_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 3: ENFRENTAMIENTO DE MÉTODOS DE INTEGRACIÓN ===")
    print("Función: f(x) = 1/x  |  Intervalo [1, 5]  |  Valor Exacto = ln(5)\n")
    
    def f_analitica(x):
        return 1.0 / x
        
    a, b = 1.0, 5.0
    integral_real = math.log(5.0)  # log en python es el logaritmo natural (ln)
    
    # Probaremos con diferentes números de subintervalos pares para que ambos puedan competir
    mallas_pares = [2, 4, 10, 50]
    
    print(f"{'n':<6}{'Error Trapecio O(h²)':<25}{'Error Simpson 1/3 O(h⁴)':<28}{'Factor de Ventaja'}")
    print("-" * 72)
    
    for n in mallas_pares:
        # 1. Ejecución en Trapecio Compuesto
        res_trapecio = trapecio_compuesto(f_analitica, a, b, n)
        err_trapecio = abs(integral_real - res_trapecio)
        
        # 2. Ejecución en Simpson 1/3 Compuesto
        res_simpson = simpson_13_compuesto(f_analitica, a, b, n)
        err_simpson = abs(integral_real - res_simpson)
        
        # 3. Factor de ventaja de precisión
        ventaja = err_trapecio / err_simpson if err_simpson > 1e-15 else float('inf')
        
        print(f"{n:<6}{err_trapecio:<25.4e}{err_simpson:<28.4e}{ventaja:.2f}x veces más preciso")
        
    print("\nConclusión: Comprueba cómo con n = 50, Simpson alcanza una precisión impecable,")
    print("siendo miles de veces más exacto que el Trapecio bajo las mismas condiciones.")
