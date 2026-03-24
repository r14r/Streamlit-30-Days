import streamlit as st

st.set_page_config(page_title='Day17 - Course App', layout='centered')
st.title('Day17: st.secrets')
st.caption('Automatisch aus content/Day17.md erzeugte Kurs-App')


st.title('st.secrets')

st.write(st.secrets['message'])
