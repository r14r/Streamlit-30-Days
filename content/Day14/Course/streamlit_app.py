import streamlit as st

st.set_page_config(page_title='Day14 - Course App', layout='centered')
st.title('Day14: Streamlit Components')
st.caption('Automatisch aus content/Day14.md erzeugte Kurs-App')

import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)
