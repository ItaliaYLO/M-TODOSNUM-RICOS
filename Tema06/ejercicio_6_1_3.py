import numpy as np

def rk4_vaciado(f, t0, h0, dt, pasos):
    """
    Solver RK4 robusto para problemas de vaciado de tanques.
    """
    t = np.linspace(t0, t0 + pasos * dt, pasos + 1)
    h = np.zeros(pasos + 1)
    h[0] = h0

    for i in range(pasos):
        hi = max(0, h[i])
        
        k1 = dt * f(t[i], hi)
        k2 = dt * f(t[i] + 0.5*dt, max(0, hi + 0.5*k1))
        k3 = dt * f(t[i] + 0.5*dt, max(0, hi + 0.5*k2))
        k4 = dt * f(t[i] + dt, max(0, hi + k3))
        
        h[i+1] = hi + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        
    return t, h

# --- Parámetros Físicos ---
G_GRAVEDAD = 9.81
R_TANQUE = 1.0   # Radio del tanque (m)
R_ORIFICIO = 0.05 # Radio del orificio de salida (m)
H_INICIAL = 2.5  # Altura inicial del agua (m)

def modelo_torricelli(t, h):
    """
    Implementación de la EDO basada en la relación de áreas.
    """
    if h <= 0:
        return 0.0
    
    ratio_areas = (R_ORIFICIO**2) / (R_TANQUE**2)
    return -ratio_areas * np.sqrt(2 * G_GRAVEDAD * h)


tiempo, alturas = rk4_vaciado(modelo_torricelli, 0, H_INICIAL, 10, 15)

print(f"--- Simulación de Vaciado ---")
print(f"Altura inicial: {H_INICIAL} m")
print(f"Tiempo transcurrido: {tiempo[-1]} segundos")
print(f"Altura final calculada: {alturas[-1]:.4f} m")


t_v_teorico = (R_TANQUE**2 / R_ORIFICIO**2) * np.sqrt(2 * H_INICIAL / G_GRAVEDAD)
print(f"Tiempo estimado para vaciado total: {t_v_teorico:.2f} s")
