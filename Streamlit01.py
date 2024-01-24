import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("./image/versicolor.jpg")
with col2:
    st.header("Verginica")
    st.image("./image/verginica.jpg")
with col3:
    st.header("Setosa")
    st.image("./image/setosa.jpg")

df=pd.read_csv("./data/iris.csv")    
 
if(st.button("เเสดงข้อมูลตัวอย่าง")):
    st.write(df.head(10)) 
    st.buttom("ไม่เเสดงข้อมูลตัวอย่าง")
else :
    st.buttom("ไม่เเสดงข้อมูลตัวอย่าง")    

