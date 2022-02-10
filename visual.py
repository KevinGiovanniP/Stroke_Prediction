from select import select
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from dataframe import load_data


data = load_data()



def app():
    st.title('Visualisasi Penyakit Stroke dan Beberapa Penyebabnya')
    st.markdown('data yang digunakan merupakan data orang-orang yang mungkin mengidap stroke')

    agree = st.checkbox('Lihat Data')

    st.write('Grafik Umum')
    if agree:
        st.write(data.head(10))
    
    
    struk = st.selectbox("Pilih grafik",['distribusi jenis kelamin', 'Penderita Hipertensi',' penderita stroke '])

    if struk == 'distribusi jenis kelamin':
        st.subheader("Jenis Kelamin")
        fig = px.pie(data, names='gender', title = 'Distribusi jenis kelamin', width=600, height=400)
        #fig.show()
        st.plotly_chart(fig)
        st.write('data didominasi oleh perempuan dengan asumsi lebih banyak perempuan yang terkena stroke')
    elif struk == 'Penderita Hipertensi':
        st.subheader("Hipertensi")
        fig = px.pie(data, names='hypertension', title = 'Distribusi hipertensi', width=600, height=400)
        st.plotly_chart(fig)
        st.write('dapat dilihat pengidap hipertensi hanya 9.75% sehingga lebih banyak orang tanpa hipertensi dengan persentase 90,3% ')
    else:
        labels =data['stroke'].value_counts(sort = True).index
        sizes = data['stroke'].value_counts(sort = True)

        colors = ["lightgreen","red"]
        explode = (0.05,0) 
        st.write('orang yang stroke (1) dan tidak stroke (0')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90,)

        st.pyplot(fig1)
        st.write("terlihat penderita stroke jauh lebih sedikit dibandingkan dengan yang sehat")


    st.write('grafik penyebab terjadinya stroke berdasarkan pekerjaan, status merokok dan penyakit jantung')
    struk = st.selectbox("Pilih grafik",['stroke berdasarkan tipe pekerjaan', 'status merokok', 'penyakit jantung'])

    if struk == 'stroke berdasarkan tipe pekerjaan':
        #fig2 = plt.figure(figsize=(10, 4))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Tipe Pekerjaan")
        sns.catplot(y="work_type", hue="stroke", kind="count",palette="pastel", edgecolor=".6",data=data)
        st.pyplot()
        st.write('berdasarkan grafik dapat dilihat bahwa tipe pekerjaan private paling banyak menyebabkan stroke')
    elif struk == 'status merokok':
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Status Merokok")
        sns.catplot(y="smoking_status", hue="stroke", kind="count",palette="pastel", edgecolor=".6",data=data)
        st.pyplot()
        st.write('berdasarkan status merokok diatas, ternyata merokok tidak terlalu mempengaruhi stroke ')
    else:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Penyakit Jantung")
        sns.catplot(x="gender", y="stroke", hue="heart_disease", palette="pastel", kind="bar", data=data)
        st.pyplot()
        st.write("terlihat penyakit jantung cukup berpengaruh terhadap stroke dan terlihat lebih memiliki efek yang besar untuk kaum pria")
