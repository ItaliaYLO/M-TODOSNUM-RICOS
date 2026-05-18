from gauss_seidel_base import gauss_seidel

if __name__ == "__main__":
    print("=== CASO 05: ESCALACIÓN COMPLETA A SISTEMA 4X4 ===")
    
    A_4x4 = [
        [10.0, -1.0,  2.0,  0.0],
        [-1.0, 11.0, -1.0,  3.0],
        [ 2.0, -1.0, 10.0, -1.0],
        [ 0.0,  3.0, -1.0,  8.0]
    ]
    b_4x4 = [6.0, 25.0, -11.0, 15.0]
    
    solucion = gauss_seidel(A_4x4, b_4x4, tol=1e-5)
    
    if solucion:
        print("\n-> Resultados calculados (4x4):")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.5f}")
