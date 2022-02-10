import pandas as pd
import numpy as np
import streamlit as st
from dataframe import load_data
import pickle




with open('model.pkl','rb') as file:
	stroke_model = pickle.load(file)

    

stroke_cat = ['stroke', 'no_stroke']


def app():
    st.title('Stroke Predictor')
    st.markdown('### Selamat Datang di aplikasi stroke predictor')
    st.markdown('#### kami akan memberi tahu anda apakah anda beresiko terkena stroke atau tidak')

    gender = st.selectbox(label = 'Gender (Male (1)/Female(0))',options = [1,0])
    age = st.number_input(label = 'Age (cm)')
    hypertension = st.selectbox(label = 'Hypertension yes = 1 no = 0',options = [1,0])
    heart_disease = st.selectbox(label = 'heart_disease yes = 1 no = 0',options = [1,0])
    married = st.selectbox(label = 'married yes = 1 no = 0' , options = [1,0])
    work_type = st.selectbox(label = 'job_status  govt_job = 0, children = 1, Private = 2 , Self-employed = 3 , never worked = 4, ',options = [2, 3, 0, 1, 4])
    residence_type = st.selectbox(label = 'residence urban = 1 rural = 0', options = [1,0])
    avg_glucose_level = st.number_input(label = 'glucose_level')
    bmi = st.number_input(label = 'bmi')
    smoking_status = st.selectbox(label = 'smoke status 0 = unknown, former = 1, never = 2, smoke = 3' ,options = [2, 0, 1, 3])

    user_feat = pd.DataFrame([[gender,age,hypertension,heart_disease,married,work_type, residence_type, avg_glucose_level, bmi, smoking_status]], columns=['gender','age','hypertension','heart_disease','ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])

    stroke_pred = st.button(label = 'Predict Stroke')
    if stroke_pred:
        user_stroke = stroke_model.predict(user_feat)[0]
        st.markdown(f' ***{stroke_cat[user_stroke]}***')
        user_stroke_proba = stroke_model.predict_proba(user_feat)
        df = pd.DataFrame(user_stroke_proba[0],index = stroke_cat, columns = ['stroke'])
        st.markdown('### **Prediction Confidence (value as probability)**')
        st.bar_chart(df)
    else:
        pass