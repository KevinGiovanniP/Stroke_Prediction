import streamlit as st
import  predict, visual



#create streamlit app

PAGES = {
    "Data Visualization": visual,
    "Stroke Prediction": predict
}



st.sidebar.title("Menu")
selection = st.sidebar.selectbox("Pages", list(PAGES.keys()))
page = PAGES[selection]
page.app()





