from secante_base import secante

def f(x):
    return x**2 - 2

if __name__ == "__main__":
    print("=== CASO 04: COMPARATIVA DE SEMILLAS INICIALES ===\n")
    
    print("Prueba A: Semillas muy cercanas a la raíz (1.0 y 2.0)")
    secante(f, 1.0, 2.0, tol=1e-5)
    
    print("\n" + "="*40 + "\n")
    
    print("Prueba B: Semillas más lejanas (10.0 y 20.0)")
    secante(f, 10.0, 20.0, tol=1e-5)
