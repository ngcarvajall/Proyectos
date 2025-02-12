import streamlit as st
import pandas as pd
import pickle

from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title='Predicción de precios',
    page_icon='🏠',
    layout='centered'
)

st.title('Predicción de precios de casa con ML🏠')

st.write('Si quieres buscar el precio para tu casa próximo hogar, estás en el lugar correcto')

st.write("Usa esta aplicación para predecir el precio de una casa basándote en sus características. ¡Sorpréndete con la magia de los datos! 🚀")

st.image(
    "C:\\Users\\DELL\\Git\\Proyecto7---Proyecto-Regresi-n-Lineal\\Foto\\foto.webp",  # URL de la imagen
    caption="Tu próxima casa está aquí.",
    use_column_width=True,
)


# Cargar los modelos y transformadores entrenados
def load_models():
    with open('modelos_pickel_2/target_encoder.pkl', 'rb') as f:
        target_encoder = pickle.load(f)
    with open('modelos_pickel_2/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('modelos_pickel_2/random_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)

    return target_encoder, scaler, model 

target_encoder, scaler, model = load_models()

st.header("🔧 Características de la casa")
col1, col2 = st.columns(2)

with col1:
    propertyType = st.selectbox("Tipo de Propiedad", ["flat", "penthouse", "studio", "duplex", 'chalet', 'countryHouse'], help="Selecciona el tipo de propiedad de la casa.")
    size = st.slider('Tamaño del Piso', 20,140,50, help='Elige el tamaño ideal para ti')
    exterior = st.selectbox("Exterior", ["True", "False"], help="Elige si tiene vista a la calle.")
    rooms = st.number_input("Habitaciones", min_value=0,max_value=4 , value=1, step=1, help="Elige un número de habitaciones entre 0 y 4.")
    bathrooms = st.number_input("Baños", min_value=1, max_value=3, value=1, step=1, help="Elige cuántos baños tiene.")

with col2:
    distance = st.slider("Distancia del Centro (metros)", 180,57000,1000,help="Elige tu distancia deseada del Centro.")
    status = st.selectbox('Condición del piso', ['good', 'Desconocido', 'newdevelopment', 'renew'], help='Elije las condiciones de tu nuevo piso')
    floor = st.selectbox("Piso", ["ss", "st", 'bj', 'en', 'Desconocido', '1','2', '3', '4', '5', '6', '7', '8', '14'], help="Elige si tiene vista a la calle.")
    hasLift = st.selectbox('Tiene ascensor', ['True', 'False', 'Desconocido'])

# Botón para realizar la predicción
if st.button("💡 Predecir Precio"):
    # Crear DataFrame con los datos ingresados
    new_house = pd.DataFrame({
        'propertyType': [propertyType],
        'size': [size],
        'exterior': [exterior],
        'rooms': [rooms],
        'bathrooms': [bathrooms],
        'distance': [distance],
        'status': [status],
        'floor': [floor],
        'hasLift': [hasLift]
    })

    # Columnas categóricas y numéricas
    categorical_columns = ['propertyType', 'exterior', 'rooms', 'bathrooms', 'status', 'floor', 'hasLift']
    numerical_columns = ['size', 'distance']

    # Aplicar el TargetEncoder y StandardScaler
    new_house_encoded = new_house.copy()
    new_house_encoded[new_house.columns] = target_encoder.transform(new_house)
    new_house_encoded[numerical_columns] = scaler.transform(new_house_encoded[numerical_columns])

    # Realizar la predicción
    prediction = model.predict(new_house_encoded)[0]

    # Mostrar el resultado
    st.success(f"💵 El precio estimado de la casa es: ${prediction}")
    st.balloons()

st.markdown(
    """
    ---
    **Proyecto creado con el potencial de la ciencia de datos.**  
    Desarrollado con por un servidor usando Streamlit ❤️.
    """,
    unsafe_allow_html=True,
)