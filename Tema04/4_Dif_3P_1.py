import math
from diferencias_3p_base import diferencia_central_3p

if __name__ == "__main__":
    print("=== EJERCICIO 1: VALIDACIÓN CON FUNCIONES TRIGONOMÉTRICAS ===")
    print("Función: f(x) = sin(x)  |  Punto de evaluación: x0 = pi / 3\n")
    
    # Definición de la función objetivo
    def f_trig(x):
        return math.sin(x)
        
    x0 = math.pi / 3  # 60 grados en radianes
    h = 0.01          # Tamaño de paso seleccionado
    
    # 1. Cálculo Numérico aproximado
    derivada_numerica = diferencia_central_3p(f_trig, x0, h)
    
    # 2. Cálculo Analítico exacto (La derivada teórica de sin(x) es cos(x))
    derivada_real = math.cos(x0)
    
    # 3. Evaluación de errores numéricos
    error_absoluto = abs(derivada_real - derivada_numerica)
    error_relativo_pct = (error_absoluto / derivada_real) * 100
    
    print(f"-> Parámetro de paso (h): {h}")
    print(f"-> Derivada Numérica Aproximada : {derivada_numerica:.8f}")
    print(f"-> Derivada Analítica Real     : {derivada_real:.8f}")
    print(f"-> Error Absoluto de Truncamiento: {error_absoluto:.2e}")
    print(f"-> Error Relativo Porcentual    : {error_relativo_pct:.6f}%")
