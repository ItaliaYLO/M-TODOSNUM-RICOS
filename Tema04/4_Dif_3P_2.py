from diferencias_3p_base import diferencia_central_3p

if __name__ == "__main__":
    print("=== EJERCICIO 2: ESTIMACIÓN DE VELOCIDAD INSTANTÁNEA ===")
    print("Aplicación práctica con arreglos discretos de posición y tiempo (Física).\n")
    
    # Datos experimentales recopilados por un sensor
    # Tiempo t (en segundos) espaciados uniformemente cada h = 0.2 s
    tiempo = [0.0, 0.2, 0.4, 0.6, 0.8]
    # Posición s (en metros) correspondientes a cada instante de tiempo
    posicion = [0.0, 0.12, 0.48, 1.10, 2.02]
    
    print("Tabla de Datos Experimentales:")
    print("Tiempo (s):   ", tiempo)
    print("Posición (m): ", posicion)
    
    # Queremos aproximar la velocidad instantánea en t0 = 0.4 segundos (Índice 2)
    # Para usar diferencias centrales de 3 puntos necesitamos el punto anterior (índice 1) y el posterior (índice 3)
    t0_indice = 2
    h = tiempo[1] - tiempo[0] # Tamaño de paso uniforme h = 0.2
    
    # Simulamos una función matemática que consulta el arreglo basado en el paso indexado
    # Como t0 = 0.4, t0 + h = 0.6 (índice 3), t0 - h = 0.2 (índice 1)
    s_adelante = posicion[t0_indice + 1] # s(0.6) = 1.10
    s_atras = posicion[t0_indice - 1]    # s(0.2) = 0.12
    
    # Aplicación directa de la regla central discreta
    velocidad_instantanea = (s_adelante - s_atras) / (2.0 * h)
    
    print(f"\n-> Evaluando de forma discreta alrededor de t = {tiempo[t0_indice]} s:")
    print(f"   s(t0 + h) = {s_adelante} m")
    print(f"   s(t0 - h) = {s_atras} m")
    print(f"-> Velocidad calculada en t = 0.4 s: {velocidad_instantanea:.4f} m/s")
