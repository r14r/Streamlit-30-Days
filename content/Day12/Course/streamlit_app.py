import streamlit as st

st.set_page_config(page_title='Day12 - Course App', layout='centered')
st.title('Day12: st.checkbox')
st.caption('Automatisch aus content/Day12.md erzeugte Kurs-App')


st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
