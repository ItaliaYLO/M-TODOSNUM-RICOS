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
