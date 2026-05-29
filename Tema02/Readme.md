# Tema 2: Solución de Ecuaciones de una Variable

En este módulo se exploran los algoritmos analíticos y numéricos utilizados para hallar las raíces (o ceros) de funciones no lineales de la forma $f(x) = 0$. A continuación, se detalla la lógica formal, el modelado algorítmico y el catálogo de implementación para cada método.

---

## 1️ Método de Bisección

### Concepto Fundamental
Es un algoritmo iterativo de búsqueda de raíces que se clasifica dentro de los **métodos cerrados o de intervalo**. Funciona dividiendo repetidamente un intervalo a la mitad y seleccionando el subintervalo donde se garantiza que se encuentra la raíz. 

Su validez matemática se fundamenta estrictamente en el **Teorema del Valor Intermedio (Teorema de Bolzano)**: si una función continua $f(x)$ cambia de signo en un intervalo $[a, b]$ (es decir, $f(a) \cdot f(b) < 0$), entonces existe al menos una raíz real dentro de ese espacio.

### El Algoritmo Paso a Paso

1. **Entrada y Validación:** Definir un intervalo inicial $[a, b]$ tal que cumpla la condición de cambio de signo:
   $$f(a) \cdot f(b) < 0$$
2. **Cálculo del Punto Medio ($x_r$):** Se aproxima la posición de la raíz dividiendo el intervalo exactamente a la mitad:
   $$x_r = \frac{a + b}{2}$$
3. **Evaluación de Subintervalos:**
   * Si $f(a) \cdot f(x_r) < 0$: La raíz se encuentra en la mitad izquierda, por lo tanto el límite derecho se actualiza: $b = x_r$.
   * Si $f(a) \cdot f(x_r) > 0$: La raíz se encuentra en la mitad derecha, por lo tanto el límite izquierdo se actualiza: $a = x_r$.
   * Si $f(a) \cdot f(x_r) = 0$: Se ha encontrado la raíz exacta en $x_r$.
4. **Criterio de Parada:** El ciclo de repetición continúa recalculando $x_r$ hasta que el error aproximado sea menor que una tolerancia predefinida ($\text{Error} < \text{tol}$).

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Bisección General](./biseccion_base.py)

###  Ejercicios Desarrollados
Menú interactivo con problemas resueltos aplicando el método de bisección sobre diferentes familias de funciones matemáticas:

| Caso de Estudio | Tipo de Función | Enlace al Script |
| :--- | :--- | :---: |
| **01. Polinomio Cuadrático** | Curvas polinomiales sencillas de grado 2. | (C:\Users\Lozad\OneDrive\Pictures\Screenshots.png) | [ ver_codigo.py](./01_polinomio_cuadratico.py) |
| **02. Función Cúbica** | Análisis de raíces en ecuaciones de grado 3. | [ ver_codigo.py](./02_funcion_cubica.py) |
| **03. Función Trascendental** | Combinación de identidades y álgebra mixta. | [ ver_codigo.py](./03_funcion_trascendental.py) |
| **04. Función Exponencial** | Búsqueda de ceros en curvas de crecimiento y decaimiento. | [ ver_codigo.py](./04_funcion_exponencial.py) |
| **05. Función Logarítmica** | Solución numérica limitando el dominio a valores positivos. | [ ver_codigo.py](./05_funcion_logaritmica.py) |

---

## 2️ Método de Regla Falsa (Regula Falsi)

###  Concepto Fundamental
A diferencia del método de bisección, que divide el intervalo ciegamente a la mitad, el método de la **Regla Falsa** aprovecha la geometría de la función. Conecta los puntos $(a, f(a))$ y $(b, f(b))$ mediante una línea recta (secante). La intersección de esta línea recta con el eje $x$ nos da una estimación de la raíz ($x_r$), lo que suele acelerar la convergencia en comparación con bisección si la curva es relativamente plana.

Al ser también un **método cerrado**, sigue requiriendo que el intervalo inicial cumpla con el cambio de signo de Bolzano ($f(a) \cdot f(b) < 0$).

###  El Algoritmo Paso a Paso

1. **Entrada e Intervalo:** Definir límites iniciales $[a, b]$ que encierren la raíz con cambio de signo.
2. **Cálculo de la Intersección ($x_r$):** Se calcula la aproximación de la raíz mediante la fórmula de la recta interpolante:
   $$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$
3. **Criterio de Actualización:** Se evalúa el signo del producto para mover los límites del intervalo de la misma forma que en bisección.
4. **Condición de Parada:** El proceso se repite cíclicamente hasta que el error aproximado cumpla con la tolerancia establecida.

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Regla Falsa General](./regla_falsa_base.py)

### 🛠️ Ejercicios Desarrollados
Menú de problemas resueltos aplicando el método sobre diversas funciones matemáticas:

| Caso de Estudio | Tipo de Función / Enfoque | Enlace al Script |
| :--- | :--- | :---: |
| **01. Raíz de $x^2 - 2$** | Cálculo exacto aproximado para la raíz cuadrada de 2. | [ ver_codigo.py](./06_raiz_cuadrada.py) |
| **02. Polinomio de Grado 3** | Análisis de convergencia en curvas cúbicas más pronunciadas. | [ ver_codigo.py](./07_polinomio_grado3.py) |
| **03. Función Trigonométrica** | Evaluación de raíces oscilatorias acotadas en un intervalo. | [ ver_codigo.py](./08_funcion_trigonometrica.py) |
| **04. Función Combinada** | Mezcla de términos algebraicos y exponenciales simultáneos. | [ ver_codigo.py](./09_funcion_combinada.py) |
| **05. Análisis de Error Porcentual** | Monitoreo estricto del error porcentual en cada paso. | [ ver_codigo.py](./10_error_porcentual_reglafalsa.py) |

---

## 3️ Método de Iteración de Punto Fijo

###  Concepto Fundamental
A diferencia de los métodos cerrados, el método de **Punto Fijo** es un método abierto que no requiere de un intervalo que encierre la raíz de forma obligatoria. Consiste en transformar algebraicamente la ecuación original $f(x) = 0$ para despejar una variable $x$ en función del resto, obteniendo una ecuación equivalente de la forma:
$$x = g(x)$$

El algoritmo inicia con un único valor estimado $x_0$ y busca el punto geométrico exacto donde la curva $y = g(x)$ se cruza con la recta identidad de 45 grados ($y = x$). Para que este método garantice su éxito (convergencia), la derivada de la función de aproximación debe cumplir con la condición de contracción en el entorno de la raíz:
$$|g'(x)| < 1$$

###  El Algoritmo Paso a Paso

1. **Preparación y Despeje:** Modificar algebraicamente $f(x) = 0$ para encontrar una función adecuada $g(x)$.
2. **Valor Inicial:** Definir una aproximación semilla o valor de arranque $x_0$.
3. **Iteración Recursiva:** Calcular los siguientes términos aplicando la regla de asignación:
   $$x_{i+1} = g(x_i)$$
4. **Criterio de Convergencia:** El proceso se detiene cuando la diferencia absoluta o relativa entre dos estimaciones consecutivas es menor que la tolerancia fijada:
   $$|x_{i+1} - x_i| < \text{tol}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Punto Fijo General](./punto_fijo_base.py)

###  Ejercicios Desarrollados
Catálogo de problemas resueltos diseñados para evaluar la convergencia y divergencia de distintas funciones $g(x)$:

| Caso de Estudio | Función a Evaluar | Enlace al Script |
| :--- | :--- | :---: |
| **01. Raíz Cuadrada** | Despeje clásico $g(x)$ basado en una raíz cuadrada estable. | [ ver_codigo.py](./11_g_raiz_cuadrada.py) |
| **02. Coseno Iterativo** | Evaluación de funciones trigonométricas con convergencia en espiral. | [ ver_codigo.py](./12_g_coseno.py) |
| **03. Análisis de Convergencia** | Comparativa matemática demostrando por qué algunos despejes divergen. | [ ver_codigo.py](./13_analisis_convergencia.py) |
| **04. Función Exponencial** | Búsqueda de punto fijo en curvas exponenciales amortiguadas. | [ ver_codigo.py](./14_g_exponencial.py) |
| **05. Función Fraccionaria** | Despeje racional iterativo controlado para evitar divisiones por cero. | [ ver_codigo.py](./15_g_fraccionaria.py) |

---

## 4️ Método de Newton-Raphson

###  Concepto Fundamental
El método de **Newton-Raphson** es un algoritmo abierto que utiliza el cálculo diferencial para acelerar la búsqueda de raíces. A partir de un valor inicial estimado $x_0$, el método traza una línea tangente a la curva de la función en el punto $(x_0, f(x_0))$. El punto donde esta línea recta tangente cruza el eje $x$ se convierte en nuestra siguiente aproximación mejorada ($x_1$).

Debido a que utiliza información tanto del valor de la función como de su pendiente (derivada), tiene una velocidad de **convergencia cuadrática**. Esto significa que el número de dígitos significativos correctos aproximadamente se duplica en cada iteración. Su única gran limitante es que requiere conocer analíticamente la derivada $f'(x)$ y que esta no sea cero en ningún punto evaluado ($f'(x) \neq 0$).

###  El Algoritmo Paso a Paso

1. **Entrada:** Definir la función $f(x)$, su derivada analítica $f'(x)$, y un valor semilla inicial $x_0$.
2. **Cálculo Iterativo:** Se proyecta la intersección de la tangente con el eje $x$ mediante la fórmula recursiva:
   $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
3. **Validación Crítica:** Si en algún punto $f'(x_i)$ se aproxima a cero, el algoritmo se detiene para evitar una división por cero (lo que geométricamente significa una tangente horizontal que nunca cruzará el eje $x$).
4. **Criterio de Parada:** El ciclo finaliza cuando el error absoluto o relativo entre dos aproximaciones consecutivas es menor que la tolerancia:
   $$|x_{i+1} - x_i| < \text{tol}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Newton-Raphson General](./newton_raphson_base.py)

###  Ejercicios Desarrollados
Soluciones numéricas optimizadas aplicando Newton-Raphson en diferentes tipos de funciones complejas:

| Caso de Estudio | Función / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Newton en Polinomios** | Raíces exactas en polinomios clásicos de grado superior. | [ ver_codigo.py](./16_newton_polinomios.py) |
| **02. Raíces de Grado $n$** | Algoritmo optimizado para calcular raíces cúbicas o quintas de cualquier número. | [ ver_codigo.py](./17_newton_raiz_n.py) |
| **03. Convergencia Rápida** | Demostración de cómo el método converge en poquísimas iteraciones. | [ ver_codigo.py](./18_convergencia_rapida.py) |
| **04. Newton con Trigonométricas** | Resolución de ecuaciones oscilatorias donde la pendiente cambia drásticamente. | [ ver_codigo.py](./19_newton_trigonometricas.py) |
| **05. Newton con Exponenciales** | Aplicación en modelos de transferencia o decaimiento exponencial. | [ ver_codigo.py](./20_newton_exponenciales.py) |

---

## 5️ Método de la Secante

###  Concepto Fundamental
El método de la **Secante** es un algoritmo abierto que funciona de manera similar al de Newton-Raphson, pero con una gran ventaja práctica: **no requiere calcular la derivada de la función**. En su lugar, aproxima la pendiente de la tangente utilizando una diferencia finita basada en dos puntos previos ($x_{i-1}$ y $x_i$).

Geométricamente, traza una línea secante que pasa por los puntos $(x_{i-1}, f(x_{i-1}))$ y $(x_i, f(x_i))$. El lugar exacto donde esta línea corta el eje $x$ se convierte en la nueva aproximación ($x_{i+1}$). Al ser un método abierto, no requiere que los dos valores iniciales encierren obligatoriamente la raíz (no exige cambio de signo), pero sí es vital que estén relativamente cerca de ella para garantizar la convergencia.

###  El Algoritmo Paso a Paso

1. **Entrada:** Definir la función $f(x)$ y establecer dos puntos iniciales de arranque: $x_0$ y $x_1$.
2. **Aproximación de la Raíz ($x_{i+1}$):** Se calcula el siguiente término sustituyendo la derivada de Newton por la fórmula de la pendiente secante:
   $$x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}$$
3. **Validación de Pendiente:** Si los valores de la función en ambos puntos se igualan ($f(x_{i-1}) = f(x_i)$), el denominador se vuelve cero. En este caso, el algoritmo se detiene para evitar una indeterminación.
4. **Criterio de Parada:** El ciclo de cálculo termina cuando la diferencia absoluta entre las últimas dos aproximaciones es menor que la tolerancia:
   $$|x_{i+1} - x_i| < \text{tol}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de la Secante General](./secante_base.py)

###  Ejercicios Desarrollados
Menú interactivo con problemas resueltos aplicando la aproximación por secantes en escenarios de ingeniería:

| Caso de Estudio | Función / Aplicación | Enlace al Script |
| :--- | :--- | :---: |
| **01. Secante en Polinomios** | Extracción de raíces sin calcular derivadas en ecuaciones de grado superior. | [ ver_codigo.py](./21_secante_polinomios.py) |
| **02. Función Trascendental** | Resolución de ecuaciones mixtas trigonométricas mediante diferencias finitas. | [ ver_codigo.py](./22_secante_trascendental.py) |
| **03. Evitando la Indeterminación** | Prueba de estabilidad controlando que el denominador no se haga cero. | [ ver_codigo.py](./23_estabilidad_denominador.py) |
| **04. Comparativa de Semillas** | Evaluación de cómo afecta la elección de los dos puntos de arranque ($x_0, x_1$). | [ ver_codigo.py](./24_comparativa_semillas.py) |
| **05. Caso Exponencial Complejo** | Solución numérica en curvas asintóticas donde Newton sería muy complejo de derivar. | [ ver_codigo.py](./25_secante_exponencial.py) |
