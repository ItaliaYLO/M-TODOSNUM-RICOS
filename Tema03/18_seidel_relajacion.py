def gauss_seidel_relajacion(A_matriz, b_vector, omega=1.2, tol=1e-5, max_iter=100):
    n = len(b_vector)
    x = [0.0] * n
    
    print(f"--- CORRIENDO CON RELAJACIÓN (OMEGA = {omega}) ---")
    for k in range(1, max_iter + 1):
        error_max = 0.0
        for i in range(n):
            suma = sum(A_matriz[i][j] * x[j] for j in range(n) if i != j)
            x_gs = (b_vector[i] - suma) / A_matriz[i][i]
            
            # Aplicación de la fórmula del factor de relajación
            x_relajado = omega * x_gs + (1 - omega) * x[i]
            
            error_i = abs((x_relajado - x[i]) / x_relajado) if abs(x_relajado) > 1e-12 else abs(x_relajado - x[i])
            if error_i > error_max:
                error_max = error_i
                
            x[i] = x_relajado
            
        if error_max < tol:
            print(f"-> Convergencia SOR lograda en la iteración {k}.")
            return x
    return x

if __name__ == "__main__":
    print("=== CASO 03: OPTIMIZACIÓN POR FACTOR DE RELAJACIÓN (SOR) ===")
    A = [[4.0, 1.0], [1.0, 3.0]]
    b = [5.0, 4.0]
    
    gauss_seidel_relajacion(A, b, omega=1.15, tol=1e-5)
