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
| **01. Polinomio Cuadrático** | Curvas polinomiales sencillas de grado 2. | [ ver_codigo.py](./01_polinomio_cuadratico.py) |
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
