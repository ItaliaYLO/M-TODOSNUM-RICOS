from jacobi_base import jacobi

if __name__ == "__main__":
    print("=== CASO 03: DEMOSTRACIÓN DE DIVERGENCIA EN JACOBI ===")
    print("Nota: El elemento diagonal a_11 es 1, menor que la suma de sus compañeros (2+3=5).\n")
    
    # Matriz mal estructurada para un método iterativo abierto
    A_inestable = [
        [1.0, 2.0, 3.0],
        [4.0, 2.0, 1.0],
        [2.0, 1.0, 2.0]
    ]
    b = [14.0, 13.0, 9.0]
    
    # Ponemos un límite bajo de iteraciones (10) porque los valores explotarán exponencialmente
    jacobi(A_inestable, b, max_iter=10)
