
# 🧩 Proyecto 9: Clustering y Regresión

## 📖 Descripción
Este proyecto se centra en el análisis de datos históricos de facturas y órdenes de clientes para identificar patrones de comportamiento y predecir ventas mediante técnicas de *clustering* y modelos de regresión.

### **Retos iniciales**
- Un número limitado de clientes (795), distribuidos en todas las regiones, mercados y países.
- Datos desglosados a nivel de artículo dentro de las facturas, lo que requería consolidarlos a nivel de cliente para una mejor interpretación.
- Duplicidad en los identificadores de clientes (`Customer ID`), lo que llevó a la necesidad de agrupar los datos por el nombre del cliente para realizar el análisis.

### **Variable objetivo**
La variable objetivo elegida fue **`Sales`**, por lo que todos los modelos se centraron en la predicción de este valor.

---

## 🗂️ Estructura del Proyecto

```
📦 PROYECTO9_CLUSTERING_REGRESION
├── 📂 Datos                
│   ├── Datos_Modelo_1/     # Datos procesados para el modelo 1
│   ├── Datos_Modelo_2/     # Datos procesados para el modelo 2
│   ├── Datos_Modelo_3/     # Datos procesados para el modelo 3
│   ├── df_cluster_0.csv    # Cluster 0 generado
│   ├── df_cluster_1.csv    # Cluster 1 generado
│   ├── df_predecir_0.csv   # Predicciones para el Cluster 0
│   ├── df_predecir_1.csv   # Predicciones para el Cluster 1
│   └── Global_Superstore.csv # Datos originales sin procesar
├── 📂 Notebooks            
│   ├── Modelo_1.ipynb      # Notebooks con el análisis y modelo 1
│   ├── Modelo_2.ipynb      # Notebooks con el análisis y modelo 2
│   ├── Modelo_3.ipynb      # Notebooks con el análisis y modelo 3
│   └── EDA.ipynb           # Análisis exploratorio de datos
├── 📂 src                  # Scripts para procesamiento y modelado
└── README.md               # Descripción general del proyecto
```

---

## 🛠️ Instalación y Requisitos

El proyecto fue desarrollado en Python 3.9. Para reproducir los análisis, asegúrate de instalar las siguientes dependencias:

- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`scikit-learn`](https://scikit-learn.org/stable/)
- [`scipy`](https://scipy.org/)

Instala las dependencias con el siguiente comando:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

---

## 🚀 Metodología

### **Preparación de Datos y Clustering**
Se generó un nuevo DataFrame consolidado a nivel de cliente con las siguientes métricas clave:
- **`facturas_total`**: Número total de órdenes por cliente.
- **`descuento_medio`**: Promedio de descuento utilizado por cliente.
- **`compras_total`**: Suma total de las ventas por cliente.
- **`compras_media`**: Promedio de las ventas por cliente.
- **`beneficio_total`**: Beneficio total generado por cliente.
- **`costo_envio_medio`**: Promedio del costo de envío por cliente.

#### **Resultados de Clustering:**
- **K-Means**:
  - Dividió a los clientes en dos clusters (531 y 264 clientes).
- **Ward (Distancia Euclidiana)**:
  - Mejoró la separación con dos clusters (278 y 517 clientes), diferenciando claramente a los clientes con altos valores de ventas y en el resto de columnas, solo a excepción del descuento_medio.

---

### **Modelos de Regresión**
Los modelos se entrenaron separadamente para cada cluster generado.

#### **Primer Modelo:**
- **Cluster 0**:
  - Con una única variable numérica, se observó **underfitting**. El modelo con mejor desempeño fue Gradient Boosting.
- **Cluster 1**:
  - Persistió el underfitting, pero el Random Forest ofreció mejores métricas.

#### **Segundo Modelo:**
- Se añadieron dos columnas demográficas (`Region` y `Country`) para mejorar las predicciones.
- Los resultados fueron mixtos:
  - **Cluster 0**: El underfitting persistió, aunque con mejoras moderadas.
  - **Cluster 1**: Hubo un leve aumento en la precisión de las métricas.

#### **Tercer Modelo:**
- Se mantuvieron las columnas demográficas y se eliminaron *outliers* en `Sales` y `Shipping Cost`.
- **Resultados**:
  - **Cluster 0**:
    - Métricas **R² > 0.8** tanto en entrenamiento como en prueba, sin señales de overfitting ni underfitting.
  - **Cluster 1**:
    - Aunque las métricas no fueron tan buenas como en el Cluster 0, las diferencias entre entrenamiento y prueba fueron aceptables.

---

## 📊 Resultados y Conclusiones

- El método de Ward mostró ser más efectivo para identificar patrones de clientes.
- La eliminación de *outliers* , así como la inclusión de otra variable numérica como Quantity, mejoró notablemente las métricas de los modelos.
- **Cluster 0**:
  - Presentó un comportamiento consistente y métricas superiores a **R² = 0.8**.
- **Cluster 1**:
  - Aunque las métricas fueron menos precisas, las diferencias entre entrenamiento y prueba se mantuvieron en niveles razonables.

---

## 🔄 Recomendaciones 

1. Agregar el costo unitario de los artículos al análisis para mejorar la segmentación.
2. Considerar trabajar con las facturas como conjuntos, en lugar de desglosarlas completamente por artículos.
3. Revisar y depurar los identificadores de clientes y artículos, ya que se encontraron inconsistencias como clientes con múltiples IDs.
4. Tener cuidado con la base de datos y la claridad de la información que se maneja, ya que se presentan casos donde un mismo cliente aparece con múltiples países, regiones y mercados desde los cuales compra. Esto puede sugerir la necesidad de verificar si son personas distintas registradas bajo el mismo ID.

## Próximos pasos:

1. Manejar más a fondo los outliers, tanto univariados como multivariados. 
2. Probar el ingreso de otra variable nuércia como Discount, que uilicé como categórica.
3. Probar un orden distinto de preprocesamiento.
---

## ✒️ Autor
- **Nelson Carvajal** - [@ngcarvajall](https://github.com/ngcarvajall)
