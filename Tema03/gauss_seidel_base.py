def gauss_seidel(A_matriz, b_vector, x0_vector=None, tol=1e-5, max_iter=100):
    """
    Implementación genérica del Método de Iteración de Gauss-Seidel.
    A_matriz: Matriz de coeficientes (n x n)
    b_vector: Vector de términos independientes (n)
    x0_vector: Vector inicial aproximado (semilla)
    tol: Tolerancia del error relativo aproximado admisible
    """
    n = len(b_vector)
    
    if x0_vector is None:
        x0_vector = [0.0] * n
        
    # En Gauss-Seidel modificamos directamente sobre el mismo vector en tiempo real
    x = list(x0_vector)
    
    print(f"{'Iter':<6}{'Valores del Vector Aproximado (x)':<45}{'Error Máx':<12}")
    print("-" * 65)
    
    print(f"{0:<6}{str([round(elem, 5) for elem in x]):<45}{'---':<12}")

    for k in range(1, max_iter + 1):
        error_max = 0.0
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if i != j:
                    # Aquí radica la diferencia: 'x' ya contiene valores nuevos de esta iteración
                    # para los índices j < i, y valores viejos para j > i.
                    suma += A_matriz[i][j] * x[j]
            
            if abs(A_matriz[i][i]) < 1e-12:
                print(f"\n-> Error: Elemento diagonal a_{i+1}{i+1} es cero. No se puede dividir.")
                return None
                
            x_nuevo_i = (b_vector[i] - suma) / A_matriz[i][i]
            
            # Calcular el error relativo para esta variable individual inmediatamente
            if abs(x_nuevo_i) > 1e-12:
                error_i = abs((x_nuevo_i - x[i]) / x_nuevo_i)
            else:
                error_i = abs(x_nuevo_i - x[i])
                
            if error_i > error_max:
                error_max = error_i
                
            # Inyección inmediata del dato calculado
            x[i] = x_nuevo_i
            
        print(f"{k:<6}{str([round(elem, 5) for elem in x]):<45}{error_max:<12.6e}")
        
        if error_max < tol:
            print(f"\n-> Convergencia lograda en la iteración {k}.")
            return x
            
    print("\n-> Se alcanzó el límite máximo de iteraciones sin lograr convergencia.")
    return x
