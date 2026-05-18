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

# Integración Numérica: Método del Trapecio (Compuesto)

###  Concepto Fundamental
El **Método del Trapecio** es uno de los esquemas más intuitivos y fundamentales de las fórmulas de Newton-Cotes para integración numérica. Consiste en aproximar la función matemática $f(x)$ mediante una línea recta (un polinomio de primer orden) sobre un intervalo cerrado $[a, b]$, convirtiendo geométricamente el área bajo la curva en un trapecio regular.

Debido a que una sola línea recta genera un gran error de truncamiento en funciones con alta curvatura, se utiliza de forma práctica la **Versión Compuesta**. Esta variante divide el intervalo mayor $[a, b]$ en $n$ subintervalos o segmentos más pequeños de ancho uniforme $h$. Al calcular el área de cada trapecio individual y sumarlas todas, el error global disminuye de forma proporcional al incrementar el número de particiones ($O(h^2)$).

###  El Algoritmo Paso a Paso

1. **Definición del Dominio:** Establecer los límites de integración $a$ (inferior), $b$ (superior) y fijar el número de subintervalos deseados $n$.
2. **Cálculo del Ancho de Segmento:** Determinar el tamaño de paso o espaciado uniforme $h$ mediante la relación:
   $$h = \frac{b - a}{n}$$
3. **Mapeo de Nodos Intermedios:** Evaluar los extremos de la función y definir los puntos interiores distribuidos simétricamente mediante la regla:
   $$x_i = a + i \cdot h \quad \text{para } i = 0, 1, 2, \dots, n$$
4. **Suma Ponderada:** Aplicar la fórmula compuesta. Los valores extremos de la función ($f(a)$ y $f(b)$) se suman de forma simple, mientras que todas las evaluaciones de los nodos intermedios se multiplican por 2, ya que son compartidos por dos trapecios contiguos:
   $$\int_{a}^{b} f(x)dx \approx \frac{h}{2} \left[ f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b) \right]$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo del Trapecio Compuesto General](./trapecio_compuesto_base.py)

###  Ejercicios Desarrollados
Scripts ejecutables listos para su uso académico y análisis numérico de áreas:

| Caso de Estudio | Enfoque / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Área de Función Cuadrática** | Aproximación directa de la integral sobre una parábola estándar para evaluar el algoritmo. | [ ver_codigo.py](./4_Int_Tr_1.py) |
| **02. Cálculo de Energía Acumulada** | Problema de ingeniería eléctrica: Integración de una curva de potencia variable para obtener los kWh totales. | [ ver_codigo.py](./4_Int_Tr_2.py) |
| **03. Evaluación Integral del Error** | Análisis de convergencia que incrementa de forma masiva el parámetro $n$ para observar cómo el error se reduce a cero. | [ ver_codigo.py](./4_Int_Tr_3.py) |


#  Integración Numérica: Regla de Simpson 1/3 (Compuesta)

###  Concepto Fundamental
La **Regla de Simpson 1/3** representa una evolución geométrica dentro de las fórmulas de Newton-Cotes. En lugar de aproximar el área bajo la curva mediante trapecios planos, este método utiliza curvas parabólicas (polinomios de segundo orden) para ajustarse con mayor suavidad a las variaciones reales de la función $f(x)$.

En su **Variante Compuesta**, el método divide el intervalo de integración $[a, b]$ en un número par $n$ de subintervalos de ancho uniforme $h$. Al aproximar cada par de segmentos contiguos con una parábola independiente y sumar las áreas resultantes, se logra un rendimiento numérico excelente. El error global de truncamiento se reduce al **cuarto orden $O(h^4)$**. Esto significa que es un método de alta precisión capaz de integrar de forma exacta cualquier polinomio de grado 3 o menor, aun cuando su deducción matemática base proviene de ecuaciones cuadráticas.

>  **Restricción Crítica del Algoritmo:** Para poder emparejar las subdivisiones de dos en dos y construir las parábolas correspondientes, el número de subintervalos $n$ elegido debe ser **estrictamente un número par**.

###  El Algoritmo Paso a Paso

1. **Configuración de la Malla:** Identificar los límites del intervalo $[a, b]$ y elegir un número par de divisiones $n$.
2. **Cálculo del Paso Constante:** Determinar el espaciado uniforme $h$:
   $$h = \frac{b - a}{n}$$
3. **Mapeo y Evaluación de Nodos:** Calcular los valores internos de los nodos coordenados:
   $$x_i = a + i \cdot h \quad \text{para } i = 0, 1, 2, \dots, n$$
4. **Suma Ponderada Estratégica:** Aplicar la fórmula de coeficientes cruzados de Simpson. Los extremos se suman directo, los nodos con índice **impar** se multiplican por 4 (centros de parábola) y los nodos de índice **par** se multiplican por 2 (puntos de unión de parábolas contiguas):
   $$\int_{a}^{b} f(x)dx \approx \frac{h}{3} \left[ f(a) + 4\sum_{i=1,3,5}^{n-1} f(x_i) + 2\sum_{j=2,4,6}^{n-2} f(x_j) + f(b) \right]$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Simpson 1/3 Compuesto](./simpson_13_compuesto_base.py)

###  Ejercicios Desarrollados
Suite de programas funcionales dedicados a explorar la alta precisión y las restricciones de Simpson 1/3:

| Caso de Estudio | Enfoque / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Área de Función Cúbica** | Comprobación empírica de la exactitud teórica total del método sobre curvas cúbicas. | [ ver_codigo.py](./4_Int_Sm_1.py) |
| **02. Longitud de Arco en Ingeniería** | Aplicación avanzada: Integración de la raíz de la derivada para hallar la longitud real de un cable colgado. | [ ver_codigo.py](./4_Int_Sm_2.py) |
| **03. Duelo Definitivo (Trapecio vs Simpson)** | Análisis comparativo de precisión cruzada enfrentando ambos métodos en igualdad de condiciones de discretización. | [ ver_codigo.py](./4_Int_Sm_3.py) |
