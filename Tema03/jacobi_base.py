def jacobi(A_matriz, b_vector, x0_vector=None, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de Iteración de Jacobi.
    A_matriz: Matriz de coeficientes (n x n)
    b_vector: Vector de términos independientes (n)
    x0_vector: Vector inicial aproximado (semilla)
    tol: Tolerancia del error relativo aproximado admisible
    """
    n = len(b_vector)
    
    # Si no se provee un vector inicial, se inicializa por defecto en ceros
    if x0_vector is None:
        x0_vector = [0.0] * n
        
    x_viejo = list(x0_vector)
    x_nuevo = [0.0] * n
    
    print(f"{'Iter':<6}{'Valores del Vector Aproximado (x)':<45}{'Error Máx':<12}")
    print("-" * 65)
    
    # Imprimir estado inicial de arranque
    print(f"{0:<6}{str([round(elem, 5) for elem in x_viejo]):<45}{'---':<12}")

    for k in range(1, max_iter + 1):
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if i != j:
                    # En Jacobi se multiplica estrictamente por los valores anteriores (x_viejo)
                    suma += A_matriz[i][j] * x_viejo[j]
            
            # Protección contra división por cero en la diagonal
            if abs(A_matriz[i][i]) < 1e-12:
                print(f"\n-> Error: Elemento diagonal a_{i+1}{i+1} es cero. No se puede dividir.")
                return None
                
            x_nuevo[i] = (b_vector[i] - suma) / A_matriz[i][i]
            
        # Calcular el error relativo aproximado (utilizando norma infinito / valor máximo absoluto)
        errores = []
        for i in range(n):
            if abs(x_nuevo[i]) > 1e-12:
                errores.append(abs((x_nuevo[i] - x_viejo[i]) / x_nuevo[i]))
            else:
                errores.append(abs(x_nuevo[i] - x_viejo[i]))
                
        error_max = max(errores)
        
        print(f"{k:<6}{str([round(elem, 5) for elem in x_nuevo]):<45}{error_max:<12.6e}")
        
        # Validación de convergencia
        if error_max < tol:
            print(f"\n-> Convergencia lograda en la iteración {k}.")
            return x_nuevo
            
        # Actualización del vector para la siguiente iteración simultánea
        x_viejo = list(x_nuevo)
        
    print("\n-> Se alcanzó el límite máximo de iteraciones sin lograr convergencia.")
    return x_nuevo
