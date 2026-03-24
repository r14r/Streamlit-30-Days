import streamlit as st

st.set_page_config(page_title='Day3 - Course App', layout='centered')
st.title('Day3: st.button')
st.caption('Automatisch aus content/Day3.md erzeugte Kurs-App')


st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
