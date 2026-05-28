import numpy as np
import matplotlib.pyplot as plt
from Predictor_Corrector_Master import predictor_corrector

k = 0.5
def reactivo(t, C): return -k * C**2

t, C = predictor_corrector(reactivo, 0, 1.0, 0.2, 25)

print(f"--- Ejercicio 2.5 ---")
print(f"Concentración final después de 5s: {C[-1]:.4f} mol/L")
