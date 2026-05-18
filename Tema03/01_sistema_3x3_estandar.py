from eliminacion_gaussiana_base import eliminacion_gaussiana

if __name__ == "__main__":
    print("=== CASO 01: SISTEMA 3X3 ESTÁNDAR ===")
    
    # Matriz de coeficientes
    A = [
        [3.0, 2.0, 1.0],
        [5.0, 3.0, 4.0],
        [1.0, 1.0, -1.0]
    ]
    
    # Vector de términos independientes
    b = [1.0, 2.0, 1.0]
    
    solucion = eliminacion_gaussiana(A, b)
    
    if solucion:
        print("\n-> Solución del sistema:")
        for i, val in enumerate(solucion):
            print(f"x_{i+1} = {val:.6f}")
