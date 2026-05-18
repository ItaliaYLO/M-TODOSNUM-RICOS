def calcular_epsilon():
    epsilon = 1.0
    # Mientras (1.0 + epsilon) sea diferente de 1.0, seguimos dividiendo entre 2
    while (1.0 + epsilon) != 1.0:
        epsilon_anterior = epsilon
        epsilon /= 2.0
    return epsilon_anterior

if __name__ == "__main__":
    eps = calcular_epsilon()
    print("--- Cálculo del Épsilon de la Máquina ---")
    print(f"El Épsilon calculado en este sistema es: {eps}")
    print(f"En formato científico: {eps:.1e}")
    
    # Prueba de verificación
    print(f"\nVerificación:")
    print(f"1.0 + Eps = {1.0 + eps}")
    print(f"1.0 + (Eps/2) = {1.0 + (eps/2)}  <- (Aquí ya se pierde la precisión)")
