def analizar_infinitas_soluciones(A_matriz, b_vector):
    n = len(b_vector)
    AB = [A_matriz[i] + [b_vector[i]] for i in range(n)]
    
    # Aplicar reducción controlando ceros en la diagonal
    for k in range(n):
        if abs(AB[k][k]) < 1e-12:
            # Si la fila entera se hace cero en coeficientes y el término independiente también, son infinitas soluciones
            if abs(AB[k][-1]) < 1e-12:
                print(f"\n-> Alerta en fila {k+1}: Se ha detectado un renglón nulo completo [0 0 | 0].")
                print("El sistema posee Infinitas Soluciones (Sistema Indeterminado).")
                return True
            else:
                print("\n-> Sistema sin solución.")
                return False
                
        pivote = AB[k][k]
        for j in range(k, n + 1):
            AB[k][j] /= pivote
        for i in range(n):
            if i != k:
                factor = AB[i][k]
                for j in range(k, n + 1):
                    AB[i][j] -= factor * AB[k][j]
    return False

if __name__ == "__main__":
    print("=== CASO 04: ANÁLISIS DE INFINITAS SOLUCIONES ===\n")
    
    # La segunda ecuación es exactamente el doble de la primera
    A = [
        [1.0, 3.0],
        [2.0, 6.0]
    ]
    b = [4.0, 8.0]
    
    analizar_infinitas_soluciones(A, b)
