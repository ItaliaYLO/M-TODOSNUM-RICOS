from eliminacion_gaussiana_base import eliminacion_gaussiana

if __name__ == "__main__":
    print("=== CASO 05: ESCALACIÓN A SISTEMA 4X4 ===")
    
    A_4x4 = [
        [2.0,  1.0, -1.0,  2.0],
        [4.0,  5.0, -3.0,  6.0],
        [-2.0, 5.0, -2.0,  6.0],
        [4.0, 11.0, -4.0,  8.0]
    ]
    
    b_4x4 = [5.0, 9.0, 4.0, 2.0]
    
    solucion = eliminacion_gaussiana(A_4x4, b_4x4)
    
    if solucion:
        print("\n-> Solución del sistema 4x4:")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.6f}")
