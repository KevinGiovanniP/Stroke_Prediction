from select import select
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from dataframe import load_data


data = load_data()



def app():
    st.title('Visualisasi Penyakit Stroke dan Beberapa Penyebabnya')
    st.markdown('data yang digunakan merupakan data orang-orang yang mungkin mengidap stroke')

    agree = st.checkbox('Lihat Data')

    if agree:
        st.write(data.head(10))
    perbadingan = st.selectbox("Pilih grafik",['kuantitas produk terbanyak', 'korelasi antar parameter',' perbandingan data rating untuk tiap jenis produk '])
    
    ''' if perbadingan_total == 'kuantitas produk terbanyak':
        st.subheader("Jumlah pembelian produk paling banyak")
        xdata = [1,2,3,4,5,6,7,8,9,10]
        plt.figure(figsize = (12,6))
        sns.distplot(data['quantity'])
        plt.xticks(xdata)
        st.pyplot()
        st.write('berdasarkan grafik dapat dilihat bahwa customer paling banyak membeli 10 buah produk')
    elif df_perbadingan_total == 'korelasi antar parameter':
        st.subheader("korelasi antar parameter dataset ")
        sns.heatmap(np.round(data.corr(),2), annot=True)
        st.pyplot()
        st.write('angka 1 menandakan parameter saling berkorelasi sedangkan minus memiliki arti bahwa parameter tidak saling berkorelasi')
    else:
        xdata = [0,1,2,3,4,5,6,7,8,9,10]
        plt.figure(figsize = (12,6))
        sns.barplot(y = data['product_line'], x = data['rating'])
        plt.xticks(xdata)
        st.pyplot()
        st.write("terlihat bahwa rating tiap jenis product tidak berbeda jauh")'''
    


