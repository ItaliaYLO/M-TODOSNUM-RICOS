#  Métodos de Diferenciación Numérica: Regla de Diferencias de Tres Puntos

###  Concepto Fundamental
La diferenciación numérica busca aproximar el valor de la derivada de una función en un punto específico $x_0$ utilizando valores conocidos de la función en su vecindad, en lugar de obtener la expresión analítica exacta. 

La **Regla de Diferencias de Tres Puntos** se fundamenta matemáticamente en la expansión de la **Serie de Taylor**. Aunque existen variantes hacia adelante (forward) y hacia atrás (backward), la variante de **Diferencia Central** es la más utilizada en la práctica de la ingeniería debido a su simetría. Su gran ventaja es que el error de truncamiento es de segundo orden $O(h^2)$. En términos prácticos, esto significa que si reduces el tamaño de paso $h$ a la mitad, el error residual se reduce a la cuarta parte, ofreciendo una precisión significativamente superior a las diferencias simples de dos puntos.

###  El Algoritmo Paso a Paso

1. **Definición de Parámetros:** Seleccionar el punto de interés $x_0$ donde se desea evaluar la derivada y establecer un tamaño de paso u orden de incremento $h$ (un valor pequeño y controlado, típicamente $h = 0.01$ o $h = 0.001$).
2. **Evaluación de Entorno:** Evaluar la función original un paso hacia adelante $f(x_0 + h)$ y un paso hacia atrás $f(x_0 - h)$.
3. **Cancelación de Términos:** Restar ambos valores calculados de manera que los términos pares de la Serie de Taylor se cancelen algebraicamente entre sí.
4. **Cálculo de la Pendiente:** Dividir el resultado neto entre la distancia total recorrida ($2h$) para obtener la aproximación final de la primera derivada:
   $$f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Diferencias Centrales de 3 Puntos](./diferencias_3p_base.py)

###  Ejercicios Desarrollados
Scripts ejecutables diseñados para explorar la aproximación de la primera derivada en escenarios físicos y analíticos:

| Caso de Estudio | Enfoque / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Validación Trigonométrica** | Evaluación analítica comparando la aproximación numérica frente a la derivada exacta de funciones trigonométricas. | [ ver_codigo.py](./4_Dif_3P_1.py) |
| **02. Estimación de Velocidad** | Aplicación en física clásica para estimar la velocidad instantánea a partir de tablas discretas de posición-tiempo. | [ ver_codigo.py](./4_Dif_3P_2.py) |
| **03. Estudio de Convergencia** | Análisis de sensibilidad variando dinámicamente el tamaño de paso $h$ para observar el comportamiento del error. | [ ver_codigo.py](./4_Dif_3P_3.py) |


#  Métodos de Diferenciación Numérica: Regla de Diferencias de Cinco Puntos

###  Concepto Fundamental
La **Regla de Diferencias de Cinco Puntos** es un esquema avanzado de diferenciación numérica que incrementa drásticamente la exactitud de la aproximación de la primera derivada en un punto $x_0$. Mientras que el método de tres puntos solo consulta a los vecinos inmediatos, este algoritmo extiende su muestreo evaluando dos nodos simétricos a la izquierda y dos a la derecha.

A través de esta ponderación estratégica de coeficientes, el algoritmo cancela por completo tanto los términos de error de segundo orden como los de tercer orden de la Serie de Taylor. El resultado es un **error de truncamiento de cuarto orden $O(h^4)$**. En la práctica, esto implica una convergencia asombrosamente veloz: si divides el tamaño de paso $h$ a la mitad, ¡el error se reduce en un factor de $2^4 = 16$ veces! Es el estándar preferido para simulaciones dinámicas y modelado de órbitas de alta fidelidad.

###  El Algoritmo Paso a Paso

1. **Configuración Inicial:** Definir el punto de interés $x_0$ y el tamaño de paso base $h$.
2. **Muestreo Cuádruple:** Evaluar la función original en sus cuatro nodos vecinos distribuidos simétricamente:
   * $f(x_0 - 2h)$ (Dos pasos atrás)
   * $f(x_0 - h)$ (Un paso atrás)
   * $f(x_0 + h)$ (Un paso adelante)
   * $f(x_0 + 2h)$ (Dos pasos adelante)
3. **Ponderación de Coeficientes:** Multiplicar cada evaluación por sus coeficientes específicos deducidos algebraicamente para forzar la cancelación de errores intermedios.
4. **Cálculo de la Fórmula Central:** Unificar los términos y dividir el resultado neto entre $12h$:
   $$f'(x_0) \approx \frac{-f(x_0 + 2h) + 8f(x_0 + h) - 8f(x_0 - h) + f(x_0 - 2h)}{12h}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Diferencias Centrales de 5 Puntos](./diferencias_5p_base.py)

###  Ejercicios Desarrollados
Suite de scripts que demuestran la precisión matemática y aplicaciones en variables cinemáticas de segundo orden:

| Caso de Estudio | Enfoque / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Funciones Exponenciales** | Derivación de curvas con crecimiento acelerado ($e^x$ y $\ln(x)$) evaluando la estabilidad del método. | [ ver_codigo.py](./4_Dif_5P_1.py) |
| **02. Cálculo de Aceleración** | Aplicación cinemática: Estimación de la segunda derivada (aceleración instantánea) usando diferencias finitas. | [ ver_codigo.py](./4_Dif_5P_2.py) |
| **03. Torneo de Esquemas (3P vs 5P)** | Análisis comparativo de errores relativos corriendo el mismo problema bajo los órdenes $O(h^2)$ y $O(h^4)$. | [ ver_codigo.py](./4_Dif_5P_3.py) |
