import streamlit as st

st.set_page_config(page_title='Day9 - Course App', layout='centered')
st.title('Day9: st.line_chart')
st.caption('Automatisch aus content/Day9.md erzeugte Kurs-App')

import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
