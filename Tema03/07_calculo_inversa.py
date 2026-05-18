def calcular_matriz_inversa(A_matriz):
    n = len(A_matriz)
    
    # Crear una matriz aumentada uniendo A con una matriz Identidad (n x n)
    AB = [A_matriz[i] + [1.0 if j == i else 0.0 for j in range(n)] for i in range(n)]
    
    for k in range(n):
        if abs(AB[k][k]) < 1e-12:
            print("Error: La matriz es singular, no tiene inversa.")
            return None
            
        pivote = AB[k][k]
        for j in range(k, 2 * n):
            AB[k][j] /= pivote
            
        for i in range(n):
            if i != k:
                factor = AB[i][k]
                for j in range(k, 2 * n):
                    AB[i][j] -= factor * AB[k][j]
                    
    # Extraer la mitad derecha de la matriz reducida (que contiene la inversa)
    inversa = [AB[i][n:] for i in range(n)]
    return inversa

if __name__ == "__main__":
    print("=== CASO 02: CÁLCULO DE LA MATRIZ INVERSA (A^-1) ===")
    
    A = [
        [4.0, 3.0],
        [3.0, 2.0]
    ]
    
    inversa = calcular_matriz_inversa(A)
    
    if inversa:
        print("\n-> Matriz Inversa Resultante:")
        for fila in inversa:
            print([round(elem, 4) for elem in fila])
