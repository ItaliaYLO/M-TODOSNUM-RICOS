#  Tema 3: Sistemas de Ecuaciones Lineales

En este módulo se estudian las técnicas numéricas y algorítmicas utilizadas para resolver sistemas de ecuaciones lineales algebraicas de la forma:
$$Ax = b$$

Donde $A$ representa la matriz de coeficientes, $b$ es el vector de términos independientes y $x$ es el vector de incógnitas a descubrir. El estudio se divide en **métodos directos** (buscan soluciones exactas en un número finito de pasos) y **métodos iterativos** (aproximan la solución mediante refinamientos sucesivos).

---
#  Método de Eliminación Gaussiana

###  Concepto Fundamental
El método de **Eliminación Gaussiana** es un algoritmo numérico directo perteneciente al álgebra lineal que permite resolver sistemas de ecuaciones simultáneas de la forma $Ax = b$. Su estrategia principal se divide en dos fases algebraicas consecutivas:

1. **Triangularización (Eliminación hacia adelante):** Modifica la matriz aumentada $[A | b]$ mediante operaciones elementales de fila (multiplicación, suma e intercambio) con el fin de anular todos los coeficientes que se encuentran por debajo de la diagonal principal. Esto transforma el sistema en una **matriz triangular superior**.
2. **Sustitución hacia atrás:** Una vez que la última ecuación depende de una sola incógnita, se despeja directamente su valor y se propaga de abajo hacia arriba para resolver el resto de las variables de forma escalonada.

###  El Algoritmo Paso a Paso

1. **Construcción de la Matriz Aumentada:** Unificar la matriz de coeficientes $A_{n \times n}$ con el vector de términos independientes $b_{n \times 1}$:
   $$[A | b] = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & | & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & | & b_2 \\ \vdots & \vdots & \ddots & \vdots & | & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} & | & b_n \end{pmatrix}$$

2. **Fase de Eliminación:** Para cada columna pivote $k$ (desde $1$ hasta $n-1$), se barren las filas inferiores $i$ (desde $k+1$ hasta $n$) calculando un factor o multiplicador geométrico:
   $$m_{ik} = \frac{a_{ik}}{a_{kk}}$$
   Posteriormente, se actualiza el renglón completo mediante la operación elemental:
   $$\text{Fila}_i = \text{Fila}_i - m_{ik} \cdot \text{Fila}_k$$

3. **Fase de Sustitución Hacia Atrás:** Con la matriz completamente triangularizada, se realiza el despeje iterativo inverso comenzando desde la variable $x_n$ hasta llegar a $x_1$:
   $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$$

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Eliminación Gaussiana General](./eliminacion_gaussiana_base.py)

###  Ejercicios Desarrollados
Catálogo de programas independientes que aplican la eliminación gaussiana sobre diversos problemas analíticos y de ingeniería:

| Caso de Estudio | Tipo de Sistema / Enfoque | Enlace al Script |
| :--- | :--- | :---: |
| **01. Sistema 3x3 Estándar** | Solución base de un sistema lineal determinado de tres variables. | [ ver_codigo.py](./01_sistema_3x3_estandar.py) |
| **02. Pivoteo Parcial** | Algoritmo con intercambio de filas para evitar divisiones entre cero y mitigar errores de redondeo. | [ ver_codigo.py](./02_pivoteo_parcial.py) |
| **03. Aplicación en Circuitos** | Resolución de mallas eléctricas utilizando las Leyes de Kirchhoff. | [ ver_codigo.py](./03_aplicacion_circuitos.py) |
| **04. Matriz Mal Condicionada** | Estudio de sistemas hipersensibles donde un pequeño cambio numérico altera radicalmente la solución. | [ ver_codigo.py](./04_matriz_mal_condicionada.py) |
| **05. Sistema 4x4** | Escalación matemática del algoritmo para un sistema de mayores dimensiones. | [ ver_codigo.py](./05_sistema_4x4.py) |


#  Método de Gauss-Jordan

###  Concepto Fundamental
El método de **Gauss-Jordan** es una variación directa del método de eliminación gaussiana. La principal diferencia radica en que, en lugar de reducir la matriz de coeficientes a una forma triangular superior para luego aplicar sustitución hacia atrás, Gauss-Jordan continúa el proceso de eliminación de forma bilateral. 

Esto significa que elimina los términos no nulos tanto **debajo como encima de la diagonal principal**, al mismo tiempo que normaliza cada fila dividiéndola entre su propio elemento pivote. El objetivo final es transformar la matriz original $A$ en una **matriz identidad** ($I$). Al lograrlo, los valores del vector de términos independientes $b$ se transforman automáticamente en las soluciones exactas del sistema, eliminando por completo la necesidad de una fase de sustitución regresiva.

###  El Algoritmo Paso a Paso

1. **Estructura Aumentada:** Se plantea la matriz aumentada inicial $[A | b]$.
2. **Normalización:** Para cada fila pivote $k$ (desde $1$ hasta $n$), se divide toda la fila entre el elemento de la diagonal principal $a_{kk}$ para convertir el pivote en la unidad ($1$):
   $$\text{Fila}_k = \frac{\text{Fila}_k}{a_{kk}}$$
3. **Eliminación Cruzada:** Para todas las demás filas del sistema ($i \neq k$), se eliminan los elementos de la columna actual haciendo la operación elemental de renglón:
   $$\text{Fila}_i = \text{Fila}_i - a_{ik} \cdot \text{Fila}_k$$
4. **Lectura Directa:** Al completar el ciclo para las $n$ columnas, la matriz se habrá convertido en $[I | x]$, donde el vector resultante del lado derecho es la solución directa del sistema.

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Gauss-Jordan General](./gauss_jordan_base.py)

###  Ejercicios Desarrollados
 scripts automatizados diseñados para explorar las capacidades de reducción completa y aplicaciones algebraicas de Gauss-Jordan:

| Caso de Estudio | Tipo de Sistema / Enfoque | Enlace al Script |
| :--- | :--- | :---: |
| **01. Sistema 3x3** | Solución directa reduciendo una matriz de 3x3 a la matriz identidad. | [ ver_codigo.py](./06_gauss_jordan_3x3.py) |
| **02. Cálculo de Matriz Inversa** | Algoritmo extendido para obtener la inversa de una matriz ($A^{-1}$) usando la identidad. | [ ver_codigo.py](./07_calculo_inversa.py) |
| **03. Sistema sin Solución** | Detección analítica de sistemas inconsistentes o indeterminados (Determinante nulo). | [ ver_codigo.py](./08_sistema_sin_solucion.py) |
| **04. Infinitas Soluciones** | Manejo de matrices singulares con infinitas soluciones dependientes de variables libres. | [ ver_codigo.py](./09_infinitas_soluciones.py) |
| **05. Balanceo Químico** | Aplicación práctica para balancear ecuaciones estequiométricas mediante sistemas homogéneos. | [ ver_codigo.py](./10_balanceo_quimico.py) |


#  Método de Iteración de Jacobi

###  Concepto Fundamental
El método de **Jacobi** es un algoritmo iterativo diseñado para resolver sistemas lineales abiertos de la forma $Ax = b$. A diferencia de los métodos directos (como Gauss o Gauss-Jordan), Jacobi no modifica la matriz de coeficientes, sino que realiza un despeje algebraico de cada incógnita $x_i$ en función de las demás variables presentes en su respectiva ecuación.

El algoritmo arranca con un vector de aproximación inicial (típicamente lleno de ceros). En cada iteración, se calculan los nuevos valores de **todas** las incógnitas basándose **estrictamente en los resultados obtenidos en la iteración anterior**. Es decir, los valores actualizados no se utilizan inmediatamente, sino que se guardan de forma simultánea para la siguiente ronda de cálculos.

Para garantizar que el método converja hacia la solución verdadera, la matriz de coeficientes $A$ debe cumplir preferentemente con la propiedad de ser **estrictamente dominante por diagonal**. Esto significa que, en cada fila, el valor absoluto del elemento en la diagonal principal debe ser mayor que la suma de los valores absolutos de todos los demás elementos de esa misma fila:
$$|a_{ii}| > \sum_{j \neq i} |a_{ij}|$$

###  El Algoritmo Paso a Paso

1. **Despeje de Variables:** Convertir el sistema original despejando cada variable $x_i$ de la diagonal principal:
   $$x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij}x_j^{(k)}}{a_{ii}}$$
2. **Vector Semilla:** Definir una aproximación inicial $x^{(0)} = [x_1^{(0)}, x_2^{(0)}, \dots, x_n^{(0)}]^T$ (comúnmente ceros).
3. **Iteración Simultánea:** Evaluar la fórmula de despeje para encontrar el nuevo conjunto de respuestas $x^{(k+1)}$ usando únicamente los valores previos de $x^{(k)}$.
4. **Evaluación del Error:** Calcular el error relativo aproximado al final de cada iteración. El proceso se detiene cuando el error cae por debajo de la tolerancia estipulada ($\text{Error} < \text{tol}$).

---

##  Implementación y Casos Prácticos

###  Código Base del Método
* [ Algoritmo de Jacobi General](./jacobi_base.py)

###  Ejercicios Desarrollados
Menú de scripts independientes para estudiar el comportamiento dinámico y la convergencia de Jacobi:

| Caso de Estudio | Tipo de Enfoque | Enlace al Script |
| :--- | :--- | :---: |
| **01. Sistema 3x3 Dominante** | Solución paso a paso sobre una matriz con diagonal estrictamente dominante. | [ ver_codigo.py](./11_jacobi_dominante.py) |
| **02. Error de Tolerancia Fijo** | Monitoreo del error aproximado hasta alcanzar una precisión estricta de $10^{-5}$. | [ ver_codigo.py](./12_jacobi_tolerancia.py) |
| **03. Demostración de Divergencia** | Ejemplo práctico de cómo falla el método si la diagonal no es dominante. | [ ver_codigo.py](./13_jacobi_divergente.py) |
| **04. Reordenamiento de Filas** | Estrategia algorítmica para forzar la dominancia diagonal intercambiando renglones. | [ ver_codigo.py](./14_jacobi_reordenado.py) |
| **05. Sistema 4x4 Iterativo** | Escalación del algoritmo iterativo simultáneo sobre un sistema de 4 variables. | [ ver_codigo.py](./15_jacobi_sistema4x4.py) |
