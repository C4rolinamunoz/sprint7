


import pandas as pd
import streamlit as st
import plotly.express as px



car_data = pd.read_csv('vehicles_us.csv')

grafica = px.histogram(car_data, x="price")
grafica2 = px.scatter(car_data, x="condition", y="price", color="model")
grafica3 = px.scatter(car_data, x="odometer", y="price") 


st.header('DataSet para analizar el conjunto de datos de anuncios de venta de coches') 

    
st.write(car_data) 


showData =  st.button('Analizar el DataSet')


if showData:
    st.write('DataSet analizado por precio') 
    st.plotly_chart(grafica, use_container_width=True)

    st.write('DataSet analizado por condición y precio')
    st.plotly_chart(grafica2, use_container_width=True)

    st.write('DataSet analizado por dispersion, teniendo en cuenta odometer y precio')
    st.plotly_chart(grafica3, use_container_width=True)


         
         

