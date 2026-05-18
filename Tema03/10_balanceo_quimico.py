import math
from gauss_jordan_base import gauss_jordan

if __name__ == "__main__":
    print("=== CASO 05: APLICACIÓN PRÁCTICA (BALANCEO DE REACCIONES QUÍMICAS) ===")
    print("Balanceando: x1*(C3H8) + x2*(O2) -> x3*(CO2) + x4*(H2O)")
    print("Fijando arbitrariamente x4 = 4 para resolver el sistema homogéneo:\n")
    
    # Sistema resultante para los átomos de Carbono, Hidrógeno y Oxígeno:
    # 3*x1 - 1*x3 = 0  (Carbono)
    # 8*x1 - 2*x4 = 0 -> 8*x1 = 8 (Hidrógeno, con x4=4)
    # 2*x2 - 2*x3 - 1*x4 = 0 -> 2*x2 - 2*x3 = 4 (Oxígeno, con x4=4)
    
    A_quimica = [
        [3.0,  0.0, -1.0],
        [8.0,  0.0,  0.0],
        [0.0,  2.0, -2.0]
    ]
    b_balance = [0.0, 8.0, 4.0]
    
    coeficientes = gauss_jordan(A_quimica, b_balance)
    
    if coeficientes:
        x1 = round(coeficientes[0])
        x2 = round(coeficientes[1])
        x3 = round(coeficientes[2])
        x4 = 4
        
        print("\n-> Coeficientes Estequiométricos Calculados:")
        print(f" {x1} C3H8 + {x2} O2 -> {x3} CO2 + {x4} H2O")
        print("\n¡La ecuación química se encuentra perfectamente balanceada!")
