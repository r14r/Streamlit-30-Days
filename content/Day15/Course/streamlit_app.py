import streamlit as st

st.set_page_config(page_title='Day15 - Course App', layout='centered')
st.title('Day15: st.latex')
st.caption('Automatisch aus content/Day15.md erzeugte Kurs-App')


st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
