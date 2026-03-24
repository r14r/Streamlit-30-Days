import streamlit as st

st.set_page_config(page_title='Day18 - Course App', layout='centered')
st.title('Day18: st.file_uploader')
st.caption('Automatisch aus content/Day18.md erzeugte Kurs-App')

import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
