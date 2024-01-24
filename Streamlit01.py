import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F2%2F27%2FBlue_Flag%252C_Ottawa.jpg&tbnid=9t7-HOVnnndy0M&vet=12ahUKEwjYraqKh_WDAxX7S2cHHYZGAgsQMygAegQIARBL..i&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIris_versicolor&docid=FROT0TfbWiLqOM&w=1200&h=1200&q=versicolor%20flower&ved=2ahUKEwjYraqKh_WDAxX7S2cHHYZGAgsQMygAegQIARBL")
with col2:
    st.header("Verginica")
    st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Ff%2Ff8%2FIris_virginica_2.jpg%2F1200px-Iris_virginica_2.jpg&tbnid=s9x5PKa4yUGkGM&vet=12ahUKEwjx39u8h_WDAxXBSWwGHbmYBhIQMygAegQIARA1..i&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIris_virginica&docid=ObshDB616CHvIM&w=1200&h=1200&q=verginica%20flower&ved=2ahUKEwjx39u8h_WDAxXBSWwGHbmYBhIQMygAegQIARA1")
with col3:
    st.header("Setosa")
    st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fa%2Fa7%2FIrissetosa1.jpg%2F1200px-Irissetosa1.jpg&tbnid=jK2aO4BFleICMM&vet=12ahUKEwjDpPfdh_WDAxVKUGwGHZm9BjAQMygAegQIARBL..i&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIris_setosa&docid=loMPw0AbXOCEuM&w=1200&h=900&q=Setosa%20flower&ved=2ahUKEwjDpPfdh_WDAxVKUGwGHZm9BjAQMygAegQIARBL")