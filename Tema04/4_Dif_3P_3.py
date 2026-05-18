import math
from diferencias_3p_base import diferencia_central_3p

if __name__ == "__main__":
    print("=== EJERCICIO 3: ANÁLISIS DINÁMICO DE CONVERGENCIA ===")
    print("Evaluando el comportamiento del error disminuyendo el tamaño de paso h.\n")
    print("Función: f(x) = e^x  |  Derivada teórica real f'(0) = 1.00000000\n")
    
    def f_exp(x):
        return math.exp(x)
        
    x0 = 0.0
    derivada_real = 1.0  # e^0 = 1
    
    # Tamaño de paso inicial largo para la demostración
    h = 0.4
    
    print(f"{'Paso (h)':<12}{'Derivada Numérica':<22}{'Error Absoluto':<18}{'Factor de Reducción'}")
    print("-" * 70)
    
    error_anterior = None
    
    # Ejecutamos un ciclo de 6 etapas de refinamiento dividiendo h a la mitad
    for i in range(6):
        num_derivada = diferencia_central_3p(f_exp, x0, h)
        error_actual = abs(derivada_real - num_derivada)
        
        if error_anterior is not None and error_actual > 1e-15:
            factor_reduccion = error_anterior / error_actual
            print(f"{h:<12.5f}{num_derivada:<22.9f}{error_actual:<18.2e}{factor_reduccion:.4f}x")
        else:
            # En la primera iteración no hay un paso previo para calcular el factor de reducción
            print(f"{h:<12.5f}{num_derivada:<22.9f}{error_actual:<18.2e}{'---':<12}")
            
        error_anterior = error_actual
        h /= 2.0  # Reducir el paso a la mitad
        
    print("\nNota: Observa cómo al dividir h a la mitad, el error se divide aproximadamente entre 4 (Factor ~ 4.0).")
    print("¡Esto demuestra el comportamiento práctico del orden de convergencia cuadrático O(h²)! ")
