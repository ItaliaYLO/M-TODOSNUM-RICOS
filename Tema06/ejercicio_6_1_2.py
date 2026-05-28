import numpy as np

def rk4_enfriamiento(f, t0, T0, dt, pasos):
    """
    Método Runge-Kutta de 4to Orden optimizado para procesos térmicos.
    """
    t = np.linspace(t0, t0 + pasos*dt, pasos + 1)
    T = np.zeros(pasos + 1)
    T[0] = T0

    for i in range(pasos):

        k1 = dt * f(t[i], T[i])
        k2 = dt * f(t[i] + 0.5*dt, T[i] + 0.5*k1)
        k3 = dt * f(t[i] + 0.5*dt, T[i] + 0.5*k2)
        k4 = dt * f(t[i] + dt, T[i] + k3)
        
        T[i+1] = T[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        
    return t, T

K_CONST = 0.1     
T_AMB = 20.0      
T_INICIAL = 80.0  

def modelo_termico(t, T): 
    return -K_CONST * (T - T_AMB)

tiempo, temps = rk4_enfriamiento(modelo_termico, 0, T_INICIAL, 2, 10)

print(f"--- Simulación de Enfriamiento ---")
print(f"Tiempo inicial: {tiempo[0]} min | Temp: {temps[0]:.1f}°C")
print(f"Tiempo final:   {tiempo[-1]} min | Temp: {temps[-1]:.2f}°C")
print(f"Diferencia con T_amb: {temps[-1] - T_AMB:.2f}°C")

T_teorica = T_AMB + (T_INICIAL - T_AMB) * np.exp(-K_CONST * 20)
print(f"Error vs Valor Teórico: {abs(temps[-1] - T_teorica):.2e}")
