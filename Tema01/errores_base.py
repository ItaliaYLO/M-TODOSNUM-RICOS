def calcular_errores(v_real, v_aprox):
    """Calcula y muestra los tres tipos de errores."""
    error_absoluto = abs(v_real - v_aprox)
    
    # Evitar división por cero si el valor real es 0
    if v_real != 0:
        error_relativo = error_absoluto / abs(v_real)
    else:
        error_relativo = float('inf')
        
    error_porcentual = error_relativo * 100
    
    return error_absoluto, error_relativo, error_porcentual

# Ejemplo de prueba rápido
if __name__ == "__main__":
    real = 3.14159265
    aprox = 3.14
    
    abs_err, rel_err, pct_err = calcular_errores(real, aprox)
    print(f"Valor Real: {real} | Valor Aproximado: {aprox}")
    print(f"Error Absoluto: {abs_err:.8f}")
    print(f"Error Relativo: {rel_err:.8f}")
    print(f"Error Porcentual: {pct_err:.4f}%")
