from gauss_jordan_base import gauss_jordan

if __name__ == "__main__":
    print("=== CASO 01: REDUCCIÓN GAUSS-JORDAN 3X3 ===")
    
    A = [
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0]
    ]
    b = [8.0, -11.0, -3.0]
    
    solucion = gauss_jordan(A, b)
    
    if solucion:
        print("\n-> Solución directa del sistema:")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.6f}")
