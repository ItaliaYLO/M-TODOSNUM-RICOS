from jacobi_base import jacobi

if __name__ == "__main__":
    print("=== CASO 01: MATRIZ CON DIAGONAL DOMINANTE ===")
    
    A = [
        [10.0, -1.0, 2.0],
        [-1.0, 11.0, -1.0],
        [2.0, -1.0, 10.0]
    ]
    b = [6.0, 25.0, -11.0]
    
    # Ejecución con tolerancia estándar
    solucion = jacobi(A, b, tol=1e-3)
    
    if solucion:
        print("\n-> Solución aproximada final:")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.5f}")
