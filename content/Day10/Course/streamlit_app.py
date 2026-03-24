import streamlit as st

st.set_page_config(page_title='Day10 - Course App', layout='centered')
st.title('Day10: st.selectbox')
st.caption('Automatisch aus content/Day10.md erzeugte Kurs-App')


st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
