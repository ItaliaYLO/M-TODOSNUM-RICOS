import numpy as np

def rk4_sistemas(f, x0, y0, h, n):
    """
    Implementación optimizada de RK4 para sistemas de ecuaciones diferenciales.
    Aprovecha el broadcasting de NumPy para operaciones vectoriales eficientes.
    """
    # Aseguramos que y0 sea un arreglo de punto flotante desde el inicio
    y0 = np.asarray(y0, dtype=float)
    num_vars = len(y0)
    
    # Pre-asignación de memoria
    x = np.linspace(x0, x0 + n*h, n + 1)
    y = np.empty((n + 1, num_vars))
    
    y[0] = y0

    for i in range(n):
        curr_x = x[i]
        curr_y = y[i]
        
        # Cálculo de pendientes vectoriales
        # Multiplicamos h aquí para simplificar la actualización final
        k1 = h * np.asarray(f(curr_x, curr_y))
        k2 = h * np.asarray(f(curr_x + 0.5*h, curr_y + 0.5*k1))
        k3 = h * np.asarray(f(curr_x + 0.5*h, curr_y + 0.5*k2))
        k4 = h * np.asarray(f(curr_x + h,     curr_y + k3))

        # Actualización de estado (vectorial)
        y[i+1] = curr_y + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x, y

# --- Ejemplo: Péndulo Simple (sin fricción) ---
if __name__ == "__main__":
    # Estado: [ángulo, velocidad_angular]
    # d_theta/dt = omega
    # d_omega/dt = -(g/L) * sin(theta)
    def pendulo(t, estado):
        theta, omega = estado
        g, L = 9.81, 1.0
        return [omega, -(g/L) * np.sin(theta)]

    # Condiciones iniciales: 45 grados (en rad) y reposo
    x_sol, y_sol = rk4_sistemas(pendulo, 0, [np.pi/4, 0], 0.05, 20)

    print(f"{'t':>5} | {'Ángulo (rad)':>12} | {'Velocidad':>12}")
    print("-" * 45)
    for i in range(len(x_sol)):
        print(f"{x_sol[i]:5.2f} | {y_sol[i,0]:12.6f} | {y_sol[i,1]:12.6f}")
