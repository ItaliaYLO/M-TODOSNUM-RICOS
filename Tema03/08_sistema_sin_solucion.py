from gauss_jordan_base import gauss_jordan

if __name__ == "__main__":
    print("=== CASO 03: DETECCIÓN DE SISTEMA SIN SOLUCIÓN ===")
    print("Ecuaciones con pendientes idénticas pero desplazadas:\n")
    
    # 2x + 3y = 5
    # 4x + 6y = 12 (El doble en coeficientes, pero no en el término independiente)
    A = [
        [2.0, 3.0],
        [4.0, 6.0]
    ]
    b = [5.0, 12.0]
    
    # Capturará el error de pivote nulo en la segunda iteración debido a la dependencia lineal
    gauss_jordan(A, b)
