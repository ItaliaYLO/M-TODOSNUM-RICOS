from eliminacion_gaussiana_base import eliminacion_gaussiana

if __name__ == "__main__":
    print("=== CASO 04: ANÁLISIS DE MATRIZ MAL CONDICIONADA ===\n")
    
    # Sistema Original
    print("--- SISTEMA ORIGINAL ---")
    A_original = [
        [1.0, 1.0],
        [1.0, 1.001]
    ]
    b = [2.0, 2.001]
    
    sol_original = eliminacion_gaussiana(A_original, b)
    print(f"Solución original: x_1 = {sol_original[0]:.2f}, x_2 = {sol_original[1]:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Sistema con una pequeña alteración de 0.001 en el coeficiente a_22
    print("--- SISTEMA ALTERADO (+0.001 en coeficiente a_22) ---")
    A_alterada = [
        [1.0, 1.0],
        [1.0, 1.002]
    ]
    
    sol_alterada = eliminacion_gaussiana(A_alterada, b)
    print(f"Solución alterada: x_1 = {sol_alterada[0]:.2f}, x_2 = {sol_alterada[1]:.2f}")
