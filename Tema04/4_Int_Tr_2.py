import math
from trapecio_compuesto_base import trapecio_compuesto

if __name__ == "__main__":
    print("=== EJERCICIO 2: APLICACIÓN INDUSTRIAL (ENERGÍA ACUMULADA) ===")
    print("Integración del perfil de potencia variable P(t) = 5t * sin(t) en [0, 4] s.\n")
    
    # Función que representa la lectura del medidor de potencia
    def potencia(t):
        return 5.0 * t * math.sin(t)
        
    lim_inferior = 0.0  # Tiempo inicial
    lim_superior = 4.0  # Tiempo final
    segmentos = 20      # Mayor cantidad de divisiones para mayor precisión
    
    # Cálculo del área neta (Energía total)
    energia_total = trapecio_compuesto(potencia, lim_inferior, lim_superior, segmentos)
    
    print(f"-> Configuración: n = {segmentos} subintervalos (h = {(lim_superior - lim_inferior)/segmentos:.4f} s)")
    print(f"-> Energía total acumulada calculada: {energia_total:.5f} Joules / Ws")
