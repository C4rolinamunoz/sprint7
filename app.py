


import pandas as pd
import streamlit as st
import plotly.express as px


 # leer los datos
car_data = pd.read_csv('vehicles_us.csv')

fig = px.histogram(car_data, x="price")
fig2 = px.scatter(car_data, x="condition", y="price", color="model")


st.write('DataSet para analizar el conjunto de datos de anuncios de venta de coches') 

    
st.write(car_data) 
         
         
st.write('DataSet analizado por precio') 
st.plotly_chart(fig, use_container_width=True)

st.write('DataSet analizado por condición y precio')
st.plotly_chart(fig2, use_container_width=True)
