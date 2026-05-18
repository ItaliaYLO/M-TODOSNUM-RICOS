def eliminacion_gaussiana_pivoteo(A_matriz, b_vector):
    n = len(b_vector)
    AB = [A_matriz[i] + [b_vector[i]] for i in range(n)]
    
    print("--- ELIMINACIÓN CON PIVOTEO PARCIAL ACTIVO ---")
    for k in range(n - 1):
        # Estrategia de pivoteo: Buscar el máximo en la columna actual
        max_fila = k
        for i in range(k + 1, n):
            if abs(AB[i][k]) > abs(AB[max_fila][k]):
                max_fila = i
                
        # Si la fila con el máximo valor absoluto no es la actual, se intercambian
        if max_fila != k:
            print(f" [PIVOTEO] Intercambiando Fila {k+1} con Fila {max_fila+1}")
            AB[k], AB[max_fila] = AB[max_fila], AB[k]
            
        if abs(AB[k][k]) < 1e-12:
            print("Error: Sistema singular, no tiene solución única.")
            return None
            
        for i in range(k + 1, n):
            factor = AB[i][k] / AB[k][k]
            for j in range(k, n + 1):
                AB[i][j] -= factor * AB[k][j]
                
    # Sustitución hacia atrás
    x = [0.0] * n
    x[n-1] = AB[n-1][n] / AB[n-1][n-1]
    for i in range(n - 2, -1, -1):
        suma = sum(AB[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (AB[i][n] - suma) / AB[i][i]
    return x

if __name__ == "__main__":
    print("=== CASO 02: ESTRATEGIA DE PIVOTEO PARCIAL ===")
    print("Nota: El primer elemento a_11 es 0. El algoritmo clásico fallaría sin pivoteo.\n")
    
    # Sistema de prueba
    A = [
        [0.0, 2.0, 1.0],
        [1.0, -1.0, 3.0],
        [2.0, 1.0, 1.0]
    ]
    b = [5.0, 10.0, 7.0]
    
    solucion = eliminacion_gaussiana_pivoteo(A, b)
    if solucion:
        print("\n-> Solución con pivoteo:")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.6f}")
