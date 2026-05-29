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


