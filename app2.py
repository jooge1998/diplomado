import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import joblib
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'my_model.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = joblib.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCION APROBACION PRUEBAS ICFES EN COLOMBIA</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    estratos = {'Sin Estrato':0,'Estrato 1':1 , 'Estrato 2':2 ,'Estrato 3':3 , 'Estrato 4':4 ,'Estrato 5':5,'Estrato 6':6}

    genero = {'Femenino':0,'Masculino':1}

    internet = {'No':0,'Si':1}
    computador = {'No':0,'Si':1}
    
    N = st.selectbox("Genero" , ('Masculino','Femenino'))
    C = st.selectbox("Tiene Computador:", ('Si','No'))
    K = st.selectbox("Tiene Internet:", ('Si','No'))
    P = st.selectbox("Estrato de Vivienda:", ('Sin Estrato','Estrato 1','Estrato 2','Estrato 3','Estrato 4','Estrato 5','Estrato 6'))
    
    N = genero[N]
    P = estratos[P]
    K = internet[K]
    C = computador[C]
    
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(N),
                    np.float_(P),
                    np.float_(K),
                    np.float_(C)
            ]
        predictS = model_prediction(x_in, model)
        
        pred = format(predictS[0]).upper() 
    
        if(int(pred) == 1):
            a = "PERDIO"
        else:
            a = "GANO"
            
        st.success('Se predice que el estudiante ' + a + " las pruebas ICFES")

if __name__ == '__main__':
    main()