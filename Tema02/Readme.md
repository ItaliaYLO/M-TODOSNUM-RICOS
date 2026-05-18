# Tema 2: Solución de Ecuaciones de una Variable

En este módulo se exploran los algoritmos analíticos y numéricos utilizados para hallar las raíces (o ceros) de funciones no lineales de la forma $f(x) = 0$. A continuación, se detalla la lógica formal, el modelado algorítmico y el catálogo de implementación para cada método.

---

## 1️Método de Bisección

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
