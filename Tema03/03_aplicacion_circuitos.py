from eliminacion_gaussiana_base import eliminacion_gaussiana

if __name__ == "__main__":
    print("=== CASO 03: APLICACIÓN EN INGENIERÍA (CIRCUITOS ELÉCTRICOS) ===")
    print("Resolviendo las ecuaciones de malla para encontrar las corrientes I1, I2 e I3:\n")
    
    # Ecuaciones resultantes del circuito de mallas
    #  10*I1 -  2*I2 -  3*I3 = 12  (Malla 1)
    #  -2*I1 +  8*I2 -  1*I3 = 0   (Malla 2)
    #  -3*I1 -  1*I2 +  6*I3 = -5  (Malla 3)
    
    A_mallas = [
        [10.0, -2.0, -3.0],
        [-2.0,  8.0, -1.0],
        [-3.0, -1.0,  6.0]
    ]
    b_voltajes = [12.0, 0.0, -5.0]
    
    corrientes = eliminacion_gaussiana(A_mallas, b_voltajes)
    
    if corrientes:
        print("\n-> Corrientes calculadas para el circuito:")
        print(f"I_1 = {corrientes[0]:.4f} Amperios")
        print(f"I_2 = {corrientes[1]:.4f} Amperios")
        print(f"I_3 = {corrientes[2]:.4f} Amperios")
