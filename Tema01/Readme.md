# Tema 1: Teoría de Errores

##  Concepto Fundamental

En métodos numéricos, los **errores** representan la discrepancia entre el valor real de una magnitud matemática y el valor calculado mediante un algoritmo computacional. Debido a que las computadoras poseen una **precisión finita** (representación de punto flotante), se generan pequeñas desviaciones que, si no se controlan, pueden acumularse y destruir la validez de un cálculo.

###  Tipos Principales de Errores
1. **Error Absoluto:** Mide la diferencia física (magnitud exacta) entre el valor real y la aproximación.
2. **Error Relativo:** Modula el error absoluto dividiéndolo entre el valor real. Es el más importante en ingeniería porque da una idea de la **proporción o gravedad** del error.
3. **Error Porcentual:** Es simplemente el error relativo expresado en términos de porcentaje (multiplicado por 100).

---

## 📐 Modelado Matemático (Fórmulas)

Para los análisis formales, utilizamos las siguientes expresiones matemáticas de precisión:

* **Error Absoluto ($e_a$):**
  $$e_a = |V_{real} - V_{aprox}|$$

* **Error Relativo ($e_r$):**
  $$e_r = \frac{e_a}{|V_{real}|} = \frac{|V_{real} - V_{aprox}|}{|V_{real}|}$$

* **Porcentaje de Error ($e_p$):**
  $$e_p = e_r \times 100\%$$

---

##  Implementación y Casos Prácticos

###  Ejemplo de Referencia
* [ Algoritmo de Cálculo de Errores Base](./) *(Nota: vincula aquí tu script principal)*

### 🛠️ Ejercicios Desarrollados
A continuación, se presentan los problemas resueltos paso a paso y las simulaciones computacionales para este módulo:

| Caso de Estudio | Descripción | Enlace al Código |
| :--- | :--- | :---: |
| **01. Error de Redondeo** | Pérdida de precisión al cortar decimales en operaciones iterativas. | [./ejercicio1_redondeo.py] |
| **02. Error de Truncamiento** | Error inducido al cortar una serie infinita (como Taylor) en un término finito. | [ Ver Código](./) |
| **03. Precisión de Máquina** | Algoritmo para calcular el Épsilon de la máquina ($\epsilon$). | [ Ver Código](./) |
| **04. Operaciones Aritméticas** | Análisis de propagación de errores en sumas y restas críticas. | [ Ver Código](./) |
| **05. Conversión de Base** | Impacto de pasar números decimales a binario en punto flotante. | [ Ver Código](./) |
