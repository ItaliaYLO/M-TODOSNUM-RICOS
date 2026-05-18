from secante_base import secante

# Una parábola simétrica f(x) = x^2 - 4
def f(x):
    return x**2 - 4

if __name__ == "__main__":
    print("=== CASO 03: PRUEBA DE ESTABILIDAD (PENDIENTE NULA) ===")
    print("Función: f(x) = x^2 - 4")
    print("Puntos simétricos donde f(-2) y f(2) valen lo mismo (0)\n")
    
    # Al ser simétricos, f(-2) = 0 y f(2) = 0, lo que provoca división por cero inmediata
    punto_x0 = -2.0
    punto_x1 = 2.0
    
    secante(f, punto_x0, punto_x1, tol=1e-5)
