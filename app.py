


import pandas as pd
import streamlit as st
import plotly.express as px


 # leer los datos
car_data = pd.read_csv('vehicles_us.csv')

fig = px.histogram(car_data, x="odometer")
fig2 = px.density_heatmap(car_data, x="odometer")

    
         
         # escribir un mensaje
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma


     
         # mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
