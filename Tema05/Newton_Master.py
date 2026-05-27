import numpy as np
import matplotlib.pyplot as plt

def coeficientes_newton(x, y):
    """
    Calcula los coeficientes de las diferencias divididas 
    optimizando el espacio a un arreglo 1D.
    """
    n = len(y)
    # Copiamos y para no modificar el original, b contendrá los coeficientes
    b = np.array(y, dtype=float)
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            # Cálculo in-place: b[i] se actualiza usando su valor previo y el anterior
            b[i] = (b[i] - b[i-1]) / (x[i] - x[i-j])
            
    return b # Retorna [b0, b1, b2, ..., bn]

def evaluar_newton(coef, x_puntos, x_objetivo):
    """
    Evalúa el polinomio usando una forma iterativa eficiente 
    (similar al esquema de Horner).
    """
    n = len(coef)
    res = coef[-1]
    # Iteramos hacia atrás: desde el último coeficiente hasta el primero
    for i in range(n - 2, -1, -1):
        res = res * (x_objetivo - x_puntos[i]) + coef[i]
    return res

# --- Ejecución ---
if __name__ == "__main__":
    x_datos = np.array([1, 4, 6], dtype=float)
    y_datos = np.array([0, 1.386294, 1.791759], dtype=float) # ln(x)
    
    # 1. Obtener coeficientes
    b = coeficientes_newton(x_datos, y_datos)
    
    # 2. Interpolar un punto
    x_interp = 2
    y_interp = evaluar_newton(b, x_datos, x_interp)
    
    print(f"Coeficientes calculados: {b}")
    print(f"Resultado en x={x_interp}: {y_interp:.6f}")

    # --- Visualización ---
    x_eje = np.linspace(0.5, 6.5, 100)
    y_eje = [evaluar_newton(b, x_datos, xi) for xi in x_eje]

    plt.figure(figsize=(8, 5))
    plt.plot(x_eje, y_eje, 'k--', label="Polinomio interpolador", alpha=0.7)
    plt.scatter(x_datos, y_datos, color='darkred', zorder=5, label="Nodos")
    plt.plot(x_interp, y_interp, 's', color='royalblue', label=f"Punto x={x_interp}")
    
    plt.title("Interpolación por Diferencias Divididas de Newton")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
