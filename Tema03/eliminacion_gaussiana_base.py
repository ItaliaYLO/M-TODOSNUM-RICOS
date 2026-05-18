def eliminacion_gaussiana(A_matriz, b_vector):
    """
    Implementación genérica del Método de Eliminación Gaussiana.
    A_matriz: Lista de listas que representa la matriz de coeficientes (n x n)
    b_vector: Lista que representa el vector de términos independientes (n)
    """
    n = len(b_vector)
    
    # 1. Construcción de la matriz aumentada clonando los datos para no modificar los originales
    AB = [A_matriz[i] + [b_vector[i]] for i in range(n)]
    
    print("--- FASE DE ELIMINACIÓN HACIA ADELANTE ---")
    for k in range(n - 1):
        # Validación de pivote nulo
        if abs(AB[k][k]) < 1e-12:
            print(f"Error: Pivote nulo detectado en la posición ({k},{k}).")
            print("El algoritmo base requiere pivoteo parcial para este caso.")
            return None
            
        for i in range(k + 1, n):
            # Cálculo del factor/multiplicador
            factor = AB[i][k] / AB[k][k]
            print(f"Fila {i+1} -> Fila {i+1} - ({factor:.4f}) * Fila {k+1}")
            
            for j in range(k, n + 1):
                AB[i][j] -= factor * AB[k][j]
                
    print("\nMatriz aumentada resultante (Triangular Superior):")
    for fila in AB:
        print([round(elem, 4) for elem in fila])

    # 2. Fase de Sustitución Hacia Atrás
    print("\n--- FASE DE SUSTITUCIÓN HACIA ATRÁS ---")
    x = [0.0] * n
    
    # Verificar el último elemento de la diagonal
    if abs(AB[n-1][n-1]) < 1e-12:
        print("Error: El sistema no tiene solución única (Determinante igual a cero).")
        return None
        
    x[n-1] = AB[n-1][n] / AB[n-1][n-1]
    
    for i in range(n - 2, -1, -1):
        suma_regresiva = 0.0
        for j in range(i + 1, n):
            suma_regresiva += AB[i][j] * x[j]
        x[i] = (AB[i][n] - suma_regresiva) / AB[i][i]
        
    return x
