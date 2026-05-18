def analizar_precision_decimal():
    # El clásico dilema de por qué 0.1 + 0.2 no es exactamente 0.3 en programación
    suma = 0.1 + 0.2
    esperado = 0.3
    
    print("--- Análisis de Conversión Decimal a Binario ---")
    print(f"¿Cuánto es 0.1 + 0.2?")
    print(f"Resultado crudo en memoria: {suma:.17f}")
    print(f"Resultado esperado:         {esperado:.17f}")
    print(f"¿Son exactamente iguales?:  {suma == esperado}")
    
    # Solución recomendada en ingeniería numérica para comparar flotantes:
    tol = 1e-9
    son_cercanos = abs(suma - esperado) < tol
    print(f"¿Son iguales bajo una tolerancia de {tol}?: {son_cercanos}")

if __name__ == "__main__":
    analizar_precision_decimal()
