# 🔷 Prime Analytics v1

## 🧠 Idea central
> “No se trata de calcular primos, sino de entender cómo se comportan.”  
> “From brute force to insight.”

---

## 📌 Motivación

Los números primos parecen distribuirse de forma caótica cuando se observan individualmente.  
Sin embargo, al analizarlos a gran escala, emergen patrones estadísticos y propiedades matemáticas sorprendentes.

Este proyecto explora esa aparente contradicción combinando algoritmos, benchmarking, estadística y visualización de datos.

---

## ⚙️ Objetivos

Este proyecto analiza números primos desde tres perspectivas:

- **Algorítmica** → comparar algoritmos  
- **Performance** → benchmarking y escalabilidad  
- **Matemática** → densidad de primos y modelo teórico  
- **Patrones** → entender cómo emergen estructuras globales  

El objetivo no es solo obtener resultados, sino comprender **cómo crecen, escalan y se comportan** los números primos.

---

## ❓ Preguntas que intenta responder

- ¿Qué algoritmo escala mejor?  
- ¿Cómo evoluciona la densidad de primos?  
- ¿Por qué la aproximación 1 / log(n) funciona tan bien?  
- ¿Cuándo una optimización deja de ser incremental?  
- ¿Puede surgir orden a partir del aparente caos?  

---

## 📊 1. Algorithm Performance

![Performance](images/performance.png)

### 💡 Insight

A medida que crece el rango analizado, las diferencias entre algoritmos dejan de ser pequeñas mejoras y pasan a ser cambios estructurales.

El método ingenuo escala rápidamente y se vuelve impracticable.  
La optimización por raíz cuadrada mejora significativamente el rendimiento.  
La criba de Eratóstenes introduce un cambio de enfoque y mantiene alta eficiencia.

👉 **Conclusión:**  
La diferencia entre algoritmos no es incremental, sino estructural.

---

## 📊 2. Scaling Behaviour (log-log)

![LogLog](images/loglog.png)

### 💡 Insight

En escala log-log se revela el verdadero comportamiento de la escalabilidad.

El speedup crece de forma sostenida, mostrando que los algoritmos eficientes no solo son más rápidos, sino que **su ventaja se amplifica con el tamaño del problema**.

👉 **Conclusión:**  
La diferencia entre algoritmos se vuelve evidente solo a gran escala.

---

## 📊 3. Speedup Comparison

![Speedup](images/speedup.png)

### 💡 Insight

El speedup mide cuántas veces un algoritmo es más rápido que otro.

- Naive vs √n → mejora significativa  
- Naive vs Sieve → salto cualitativo  

👉 **Conclusión clave:**  
A gran escala, la diferencia deja de ser de rendimiento y pasa a ser de viabilidad.

---

## 📊 4. Prime Density vs Theory

![Density](images/density.png)

### 💡 Insight

La densidad de primos disminuye con n, pero lo hace de forma predecible.

La aproximación **1 / log(n)** sigue de cerca los datos reales y mejora su precisión a medida que crece el rango.

👉 Los primos:
- son impredecibles localmente  
- pero siguen patrones globales consistentes  

👉 **Conclusión:**  
El orden emerge del comportamiento colectivo.

---

## 🔥 Conclusiones generales

- Los algoritmos no escalan igual  
- El enfoque domina sobre la optimización  
- La eficiencia se vuelve crítica en problemas grandes  
- Los números primos muestran orden dentro del aparente caos  
- Los patrones globales emergen incluso cuando el comportamiento local parece aleatorio  

---

## 🚀 Próximos pasos

- error absoluto y relativo  
- regresión y modelado  
- análisis con ventanas móviles  
- primos gemelos  
- exportación de datos  
- visualización en Power BI  

---

## 🧠 Reflexión final

Este proyecto muestra que:

> **el verdadero valor no está en calcular resultados, sino en entender los procesos que los generan.**

---

## ▶️ How to run

Clone the repository and execute:

```bash
python Prime_Analytics_V1.py
