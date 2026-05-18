from gauss_seidel_base import gauss_seidel

if __name__ == "__main__":
    print("=== CASO 02: CONTROL DE TOLERANCIA ESTRICTA (1e-6) ===")
    
    A = [
        [5.0, 1.0, 2.0],
        [1.0, 4.0, 1.0],
        [2.0, 1.0, 6.0]
    ]
    b = [19.0, 12.0, -4.0]
    
    solucion = gauss_seidel(A, b, tol=1e-6)
