from jacobi_base import jacobi

if __name__ == "__main__":
    print("=== CASO 04: REDISEÑO DE MATRIZ MEDIANTE REORDENAMIENTO ===")
    print("Modificando las posiciones del caso inestable anterior para forzar dominancia:\n")
    
    # Hemos intercambiado la fila 1 por la fila 2 para ubicar los valores máximos en la diagonal
    A_reordenada = [
        [4.0, 2.0, 1.0],  # Era la fila 2 original
        [1.0, 2.0, 3.0],  # Era la fila 1 original (sigue sin ser ideal, pero es más estable)
        [2.0, 1.0, 2.0]   
    ]
    b_reordenado = [13.0, 14.0, 9.0]
    
    print("Intentando resolver nuevamente con reordenamiento:")
    jacobi(A_reordenada, b_reordenado, tol=1e-4, max_iter=30)
