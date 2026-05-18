import math
from diferencias_3p_base import diferencia_central_3p
from diferencias_5p_base import diferencia_central_5p

if __name__ == "__main__":
    print("=== EJERCICIO 3: COMPARATIVA DE EFICIENCIA (3 PUNTOS VS 5 PUNTOS) ===")
    print("Demostración experimental del impacto del orden jerárquico O(h²) vs O(h⁴).\n")
    
    def f_prueba(x):
        return math.cos(x)
        
    x0 = math.pi / 4  # 45 grados
    derivada_real = -math.sin(x0)  # Derivada exacta de cos(x) es -sin(x)
    
    # Probaremos con un paso medianamente grande para hacer evidentes los errores de truncamiento
    pasos = [0.2, 0.1, 0.05]
    
    print(f"{'Paso (h)':<10}{'Error Esquema 3P':<22}{'Error Esquema 5P':<22}{'Ganancia de Precisión'}")
    print("-" * 72)
    
    for h in pasos:
        # Evaluar en 3 puntos O(h²)
        sol_3p = diferencia_central_3p(f_prueba, x0, h)
        err_3p = abs(derivada_real - sol_3p)
        
        # Evaluar en 5 puntos O(h⁴)
        sol_5p = diferencia_central_5p(f_prueba, x0, h)
        err_5p = abs(derivada_real - sol_5p)
        
        # Factor de mejora
        mejora = err_3p / err_5p if err_5p > 0 else float('inf')
        
        print(f"{h:<10.3f}{err_3p:<22.4e}{err_5p:<22.4e}{mejora:.2f} veces mejor")
        
    print("\nNota: Observa cómo a medida que h disminuye, el esquema de 5 puntos incrementa su ventaja de forma exponencial.")
