import json
import streamlit as st
import requests

# URL del servidor que ejecuta el modelo linear-model y usa la interfaz de predicción.
SERVER_URL = 'https://linear-model-service-ivanavila1224.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(inputs):
    # Preparar la solicitud de predicción en el formato JSON esperado.
    predict_request = {'instances': [inputs]}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

def main():
    st.title('Estimador de Tiempo de Desarrollo')

    # Interfaz de usuario para ingresar el tamaño del código.
    code_size = st.number_input('Ingrese el numero de lineas de codigo:', min_value=0.0, step=1.0)

    # Realizar la predicción basada en el tamaño del código ingresado.
    if st.button('Predecir'):
        prediction = make_prediction([code_size])
        st.write(f'Tiempo estimado de desarrollo para un tamaño de código en horas de {code_size}: {prediction["predictions"][0][0]}')

if __name__ == '__main__':
    main()
