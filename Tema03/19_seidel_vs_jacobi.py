from jacobi_base import jacobi
from gauss_seidel_base import gauss_seidel

if __name__ == "__main__":
    print("=== CASO 04: ENFRENTAMIENTO DIRECTO (JACOBI VS GAUSS-SEIDEL) ===\n")
    
    A = [
        [8.0, 2.0, 1.0],
        [1.0, 7.0, 2.0],
        [2.0, 1.0, 9.0]
    ]
    b = [11.0, 10.0, 12.0]
    
    print(">>> EJECUTANDO METODO DE JACOBI:")
    jacobi(A, b, tol=1e-5)
    
    print("\n" + "="*55 + "\n")
    
    print(">>> EJECUTANDO METODO DE GAUSS-SEIDEL:")
    gauss_seidel(A, b, tol=1e-5)
