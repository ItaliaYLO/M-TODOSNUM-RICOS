import numpy as np

def rk4_circuito(f, t0, v0, dt, pasos):
    """
    Solver RK4 para transitorios en circuitos eléctricos.
    """
    t = np.linspace(t0, t0 + pasos * dt, pasos + 1)
    v = np.zeros(pasos + 1)
    v[0] = v0

    for i in range(pasos):
        k1 = dt * f(t[i], v[i])
        k2 = dt * f(t[i] + 0.5*dt, v[i] + 0.5*k1)
        k3 = dt * f(t[i] + 0.5*dt, v[i] + 0.5*k2)
        k4 = dt * f(t[i] + dt, v[i] + k3)
        
        v[i+1] = v[i] + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        
    return t, v

RESISTENCIA = 1000.0 
CAPACITANCIA = 0.001  
V_FUENTE = 10.0      
TAU = RESISTENCIA * CAPACITANCIA 

def modelo_rc(t, Vc):
    """
    Ecuación diferencial: dVc/dt = (Vf - Vc) / Tau
    """
    return (V_FUENTE - Vc) / TAU

tiempo, voltaje_c = rk4_circuito(modelo_rc, 0, 0, 0.1, 50)

print(f"--- Simulación Circuito RC ---")
print(f"Constante de tiempo (Tau): {TAU} s")
print(f"Voltaje final a los {tiempo[-1]}s: {voltaje_c[-1]:.4f} V")

v_teorico = V_FUENTE * (1 - np.exp(-tiempo[-1] / TAU))
error = abs(voltaje_c[-1] - v_teorico)

print(f"Voltaje teórico esperado:  {v_teorico:.4f} V")
print(f"Error numérico (RK4):      {error:.2e} V")

if voltaje_c[-1] >= 0.99 * V_FUENTE:
    print("\nEstado: El capacitor está prácticamente cargado ( > 5 Tau).")
