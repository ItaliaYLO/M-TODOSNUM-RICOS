def gauss_jordan(A_matriz, b_vector):
    """
    Implementación genérica del Método de Gauss-Jordan.
    Transforma la matriz aumentada directamente en una matriz identidad.
    """
    n = len(b_vector)
    
    # Construcción de la matriz aumentada clonando los datos
    AB = [A_matriz[i] + [b_vector[i]] for i in range(n)]
    
    print("--- FASE DE REDUCCIÓN COMPLETA (GAUSS-JORDAN) ---")
    for k in range(n):
        # Validación y protección contra pivote nulo o muy pequeño
        if abs(AB[k][k]) < 1e-12:
            print(f"Error: Pivote nulo detectado en la diagonal ({k},{k}).")
            print("El sistema requiere intercambio de filas (pivoteo) o es singular.")
            return None
            
        # 1. Normalización de la fila pivote (hacer que AB[k][k] sea igual a 1)
        pivote = AB[k][k]
        print(f"Normalizando fila {k+1} dividiendo entre el pivote: {pivote:.4f}")
        for j in range(k, n + 1):
            AB[k][j] /= pivote
            
        # 2. Eliminación bilateral: limpiar arriba y abajo de la diagonal principal
        for i in range(n):
            if i != k:  # Excluimos la fila del pivote actual
                factor = AB[i][k]
                if abs(factor) > 1e-12:
                    print(f" Eliminando columna {k+1} en Fila {i+1} -> Fila {i+1} - ({factor:.4f}) * Fila {k+1}")
                    for j in range(k, n + 1):
                        AB[i][j] -= factor * AB[k][j]
                        
    print("\nMatriz aumentada resultante (Forma Escalonada Reducida):")
    for fila in AB:
        print([round(elem, 4) for elem in fila])
        
    # Extraer el vector solución directo (última columna)
    solucion = [AB[i][n] for i in range(n)]
    return solucion
