def cancelamiento_catastrofico():
    # Dos números extremadamente cercanos
    x = 1.23456789012345
    y = 1.23456789012340
    
    resta_computadora = x - y
    resta_teorica = 0.00000000000005 # 5e-14
    
    print("--- Propagación en Operaciones Aritméticas ---")
    print(f"Valor de X: {x}")
    print(f"Valor de Y: {y}")
    print(f"Resta teórica esperada: {resta_teorica:.15f}")
    print(f"Resta real de la CPU:    {resta_computadora:.15f}")
    print(f"Diferencia del error:    {abs(resta_teorica - resta_computadora):.20f}")

if __name__ == "__main__":
    cancelamiento_catastrofico()
