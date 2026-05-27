import numpy as np
import sys
import os

# Configuración del entorno para importar el módulo de Newton
directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from Newton_Master import diferencias_divididas, evaluar_newton

def ejecutar_interpolacion():
    # Definición de nodos de control para la función exponencial
    puntos_x = np.array([0, 1, 2, 3], dtype=float)
    valores_y = np.array([1.0, 2.7182, 7.3890, 20.0855], dtype=float)
    
    # Punto donde deseamos realizar la estimación
    punto_a_evaluar = 1.5
    
    # Fase de cálculo: Obtención de coeficientes y evaluación del polinomio
    tabla_coeficientes = diferencias_divididas(puntos_x, valores_y)
    estimacion_final = evaluar_newton(tabla_coeficientes, puntos_x, punto_a_evaluar)
    
    # Comparativa de resultados
    valor_real_exp = np.exp(punto_a_evaluar)
    
    print("="*30)
    print(f"RESULTADOS DEL TEMA 5: EJERCICIO 2")
    print("="*30)
    print(f"Objetivo: Estimar e^{punto_a_evaluar}")
    print(f"Valor calculado por Newton: {estimacion_final:.5f}")
    print(f"Valor real (NumPy):         {valor_real_exp:.5f}")
    print(f"Diferencia absoluta:        {abs(valor_real_exp - estimacion_final):.5e}")
    print("="*30)

if __name__ == "__main__":
    ejecutar_interpolacion()
