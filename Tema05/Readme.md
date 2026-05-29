Tema 5: Interpolación y Ajuste de Funciones
En la práctica de la ingeniería, frecuentemente se dispone de un conjunto de datos discretos obtenidos mediante experimentos o muestreos. El objetivo de este tema es generar funciones continuas que permitan representar estos datos para realizar estimaciones, análisis de tendencias o cálculos de derivadas e integrales de forma analítica.

5.1 Interpolación Polinomial
La interpolación se basa en la premisa de que la función aproximada debe pasar exactamente por todos los puntos proporcionados. Es ideal cuando los datos son precisos y no contienen ruido.

Métodos Principales:
Polinomios de Lagrange: Se fundamentan en una combinación lineal de polinomios base. Aunque conceptualmente elegante, es ineficiente si se desea agregar nuevos puntos al conjunto original.

Polinomios de Newton (Diferencias Divididas): Este método es preferido por su naturaleza recursiva. Permite construir una tabla de diferencias que facilita la adición de nuevos datos sin necesidad de reiniciar todo el cálculo.

Trazadores (Splines) Cúbicos: En lugar de usar un solo polinomio de alto grado para todos los puntos (que suele causar oscilaciones artificiales o "Efecto Runge"), se utilizan polinomios de bajo grado (generalmente grado 3) entre cada par de puntos, asegurando continuidad en la función y sus derivadas.

5.2 Ajuste de Curvas (Regresión)
A diferencia de la interpolación, el ajuste de curvas se utiliza cuando los datos tienen incertidumbre o errores experimentales. Aquí no buscamos pasar por cada punto, sino encontrar una curva que minimice la distancia global hacia todos ellos.

Conceptos Clave:
Criterio de Mínimos Cuadrados: Técnica matemática que minimiza la suma de los cuadrados de los residuos (la diferencia vertical entre el dato observado y la curva calculada).

Regresión Lineal y Multilineal: Ajuste de datos a un modelo de línea recta o planos.

Regresión No Lineal: Ajuste de datos a modelos exponenciales, potenciales o logarítmicos mediante la linealización de las ecuaciones.
