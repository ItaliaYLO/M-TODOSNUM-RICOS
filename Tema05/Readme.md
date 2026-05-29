#  Tema 5: Interpolación y Ajuste de Funciones

<div align="justify">

En la práctica de la ingeniería, frecuentemente se dispone de un conjunto de datos discretos obtenidos mediante experimentos o muestreos. El objetivo de este tema es generar **funciones continuas** que permitan representar estos datos para realizar estimaciones, análisis de tendencias o cálculos de derivadas e integrales de forma analítica.

---

### 🔹 5.1 Interpolación Polinomial
La **interpolación** se basa en la premisa de que la función aproximada debe pasar **exactamente** por todos los puntos proporcionados. Es la herramienta ideal cuando los datos son precisos y no contienen ruido experimental.

#### **Métodos Principales:**
* **Polinomios de Lagrange:** Se fundamentan en una combinación lineal de polinomios base. Aunque conceptualmente es un método elegante, resulta **ineficiente** si se desea agregar nuevos puntos al conjunto original, ya que requiere recalcular todo el sistema.
* **Polinomios de Newton (Diferencias Divididas):** Este método es preferido por su **naturaleza recursiva**. Permite construir una tabla de diferencias que facilita la adición de nuevos datos sin necesidad de reiniciar el cálculo desde cero.
* **Trazadores (Splines) Cúbicos:** En lugar de usar un solo polinomio de alto grado para todos los puntos (evitando así las oscilaciones artificiales o el **"Efecto Runge"**), se utilizan polinomios de bajo grado (generalmente grado 3) entre cada par de puntos, asegurando la **continuidad** de la función y sus derivadas.

---

### 🔹 5.2 Ajuste de Curvas (Regresión)
A diferencia de la interpolación, el **ajuste de curvas** se utiliza cuando los datos presentan incertidumbre o errores experimentales. En este enfoque, no buscamos pasar por cada punto, sino encontrar una curva que **minimice la distancia global** hacia todos ellos para representar la tendencia general.

#### **Conceptos Clave:**
* **Criterio de Mínimos Cuadrados:** Es la técnica matemática que minimiza la suma de los cuadrados de los **residuos** (la diferencia vertical entre el dato observado y la curva calculada).
* **Regresión Lineal y Multilineal:** Se enfoca en el ajuste de datos a un modelo de línea recta o, en casos de múltiples variables, a planos.
* **Regresión No Lineal:** Permite el ajuste de datos a modelos **exponenciales, potenciales o logarítmicos**. Esto se logra mediante la **linealización** de las ecuaciones originales para facilitar su resolución numérica.

</div>

---

# 🚀 Tema 6: Solución de Ecuaciones Diferenciales Ordinarias (EDO)

<div align="justify">

La resolución de **Ecuaciones Diferenciales Ordinarias** es el pilar de la simulación de sistemas dinámicos. Dado que la mayoría de las leyes de la física y la química se expresan en términos de tasas de cambio, los métodos numéricos permiten predecir el estado futuro de un sistema a partir de una condición inicial.

---

### 🔸 6.1 Métodos de Paso Único
Estos algoritmos calculan el valor de la variable dependiente en el siguiente paso basándose exclusivamente en la información del punto actual.

* **Método de Euler:** Es el algoritmo más simple. Utiliza la pendiente al inicio del intervalo para proyectar el valor siguiente. Aunque es fundamental para entender la lógica numérica, posee un error acumulado considerable en pasos grandes.
* **Método de Runge-Kutta (RK4):** Es el estándar de oro en computación científica. Evalúa la pendiente en cuatro puntos distintos del intervalo para obtener un promedio ponderado sumamente preciso de orden $O(h^4)$, equilibrando perfectamente el costo computacional y la exactitud.

---

### 🔸 6.2 Métodos de Pasos Múltiples y Sistemas
Optimizan el cálculo utilizando la memoria de puntos calculados previamente para mejorar la trayectoria de la solución.

* **Esquemas Predictor-Corrector:** Implementan un enfoque de dos etapas donde primero se "predice" el valor futuro mediante un método explícito y luego se "corrige" mediante un método implícito para garantizar la estabilidad de la solución.
* **Sistemas de EDOs:** Aplicación de los métodos anteriores a vectores de funciones. Esto permite resolver ecuaciones de orden superior (como la aceleración en sistemas mecánicos) transformándolas en un sistema de ecuaciones de primer orden interconectadas.

</div>

---
