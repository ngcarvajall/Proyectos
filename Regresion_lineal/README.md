
# 🏡 Modelos Predictivos: Predicción de Precios de Propiedades

## 📖 Descripción
En este proyecto trabajé con **modelos predictivos** para estimar precios de propiedades. Utilicé diversas técnicas de análisis de datos y Machine Learning, aplicando transformaciones avanzadas y ajustes de parámetros para optimizar los resultados. Durante el proceso, evalué cómo las decisiones en el preprocesamiento y ajuste de parámetros afectaban el rendimiento de los modelos.

---

## 🗂️ Estructura del Proyecto

```
├── Datos/                     # Contiene los datos iniciales y procesados
├── Modelos/                   # Contiene los modelos en desarrollo
├── modelos_pickle/            # Modelos y transformadores guardados como pickle
├── Notebooks/                 # Notebooks de Jupyter con el análisis exploratorio
├── src/                       # Scripts de procesamiento y modelado
├── Foto/                      # Imágenes para la visualización del proyecto
├── README.md                  # Este archivo de descripción
```

---

## 🛠️ Instalación y Requisitos
Este proyecto utiliza **Python 3.8+**. Asegúrate de instalar las siguientes dependencias. Los enlaces llevan a la documentación oficial de cada paquete:

- [pandas](https://pandas.pydata.org/docs/)
- [numpy](https://numpy.org/doc/)
- [matplotlib](https://matplotlib.org/stable/contents.html)
- [seaborn](https://seaborn.pydata.org/)
- [scikit-learn](https://scikit-learn.org/stable/documentation.html)
- [xgboost](https://xgboost.readthedocs.io/)
- [streamlit](https://docs.streamlit.io/)

Para instalar todos los requisitos, usa el siguiente comando:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Detalles del Análisis

### **Modelo Inicial:**
1. **Limpieza de Datos:**
   - Eliminación de columnas innecesarias.
   - Transformación de variables a formatos más útiles.
   - Agregación de nuevas categorías para variables categóricas.

2. **Procesamiento de Datos:**
   - **Estandarización numérica:** Aplicación del método estándar.
   - **Detección de Outliers:** Usando Isolation Forest con los siguientes parámetros:
     - Contaminación: `[0.01, 0.05, 0.1]`
     - Estimadores: `[10, 100, 150]`
     - Selección de los elementos señalados al 100% como outliers y algunos dentro del fragmento del 60%.
   - **Codificación de Variables Categóricas:** 
     - Métodos estadísticos: `mannwhitneyu` y `kruskal`.
     - Aplicación posterior de **One-Hot Encoding** y **Target Encoding**.

3. **Modelos Probados:**
   - **Decision Tree**
   - **Random Forest**
   - **Gradient Booster**
   - **XGBooster**

   Se realizaron pruebas con el 70% y 80% de datos de entrenamiento y ajustes de parámetros específicos.

### **Iteraciones en Modelos Posteriores:**
- Se probó con diferentes órdenes de transformaciones para observar el impacto en las métricas finales.
- Evaluación continua de combinaciones de parámetros para optimizar el rendimiento.

---

## 📊 Resultados y Conclusiones

- **Eficiencia de Preprocesamiento:** La integración de One-Hot Encoding y Target Encoding permitió capturar relaciones categóricas importantes.
- **Impacto de la Detección de Outliers:** La eliminación de ruido en los datos mediante Isolation Forest mejoró la precisión de los modelos.
- **Modelos Predictivos:** Los modelos lograron un desempeño estable con métricas confiables tras las iteraciones de ajustes.

---

## 🔄 Próximos Pasos
- Continuar optimizando los hiperparámetros para mejorar las métricas.
- Experimentar con modelos avanzados como **LightGBM** o **CatBoost** para comparar resultados.
- Explorar nuevas técnicas de **feature engineering** para variables categóricas y numéricas.

---

## 📷 Visualización de Datos
Aquí tienes una muestra de la distribución de los datos utilizada durante el análisis:

![Distribución de Datos](Foto/distribucion_datos.png)

---

## ✒️ Autor
- **Nelson Carvajal** - [GitHub](https://github.com/ngcarvajall)
