import math

def aproximar_euler_taylor(x, terminos):
    aproximacion = 0.0
    for i in range(terminos):
        aproximacion += (x**i) / math.factorial(i)
    return aproximacion

if __name__ == "__main__":
    x_evaluar = 2.0
    valor_real = math.exp(x_evaluar)
    
    print(f"--- Error de Truncamiento (Serie de Taylor para e^{x_evaluar}) ---")
    print(f"Valor real (math.exp): {valor_real}\n")
    print(f"{'Términos':<10}{'Aproximación':<20}{'Error Absoluto':<20}")
    print("-" * 50)
    
    # Evaluamos agregando de 1 a 7 términos para ver cómo cae el error
    for n in range(1, 8):
        v_aprox = aproximar_euler_taylor(x_evaluar, n)
        err_abs = abs(valor_real - v_aprox)
        print(f"{n:<10}{v_aprox:<20.10f}{err_abs:<20.10e}")
