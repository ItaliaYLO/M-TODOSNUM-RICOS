import numpy as np

def simular_redondeo():
    # Usamos float32 (precisión simple) para notar el error más rápido
    valor_sumar = np.float32(0.1)
    valor_real_esperado = 10000.0
    
    suma_acumulada = np.float32(0.0)
    iteraciones = 100000
    
    for _ in range(iteraciones):
        suma_acumulada += valor_sumar
        
    error_abs = abs(valor_real_esperado - suma_acumulada)
    
    print("--- Simulación de Error de Redondeo ---")
    print(f"Sumando 0.1 un total de {iteraciones} veces...")
    print(f"Resultado esperado analíticamente: {valor_real_esperado}")
    print(f"Resultado obtenido por la CPU (float32): {suma_acumulada}")
    print(f"Error Absoluto acumulado por redondeo: {error_abs}")

if __name__ == "__main__":
    simular_redondeo()
