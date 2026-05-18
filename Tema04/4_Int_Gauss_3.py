import math
from cuadratura_gaussiana_base import cuadratura_gaussiana

if __name__ == "__main__":
    print("=== EJERCICIO 3: APLICACIÓN FÍSICA (CENTRO DE MASA DE UNA PLACA) ===")
    print("Determinación del centroide estructural usando Cuadratura Gaussiana de 3 puntos.\n")
    
    # Función de densidad variable de la placa
    def densidad_placa(x):
        return math.log(x + 1.0)
        
    # Función del momento de masa estático (x * densidad)
    def momento_placa(x):
        return x * math.log(x + 1.0)
        
    a = 0.0  # Origen de la placa (metros)
    b = 3.0  # Extremo de la placa (metros)
    
    # Calculamos de manera independiente ambas integrales definidas usando n=3 puntos de Gauss
    masa_total = cuadratura_gaussiana(densidad_placa, a, b, n=3)
    momento_total = cuadratura_gaussiana(momento_placa, a, b, n=3)
    
    # Cálculo del centroide de masa estático
    centro_de_masa = momento_total / masa_total
    
    print(f"-> Resultados del análisis de masa (L = {b} m):")
    print(f"   1. Masa total calculada de la placa : {masa_total:.4f} kg")
    print(f"   2. Momento de masa total calculado  : {momento_total:.4f} kg·m")
    print(f"-> Coordenada final del Centro de Masa (x_barra): {centro_de_masa:.5f} metros")
