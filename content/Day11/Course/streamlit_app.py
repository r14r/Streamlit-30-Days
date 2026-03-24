import streamlit as st

st.set_page_config(page_title='Day11 - Course App', layout='centered')
st.title('Day11: st.multiselect')
st.caption('Automatisch aus content/Day11.md erzeugte Kurs-App')


st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
