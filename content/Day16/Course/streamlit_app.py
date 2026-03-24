import streamlit as st

st.set_page_config(page_title='Day16 - Course App', layout='centered')
st.title('Day16: Customizing the theme of Streamlit apps')
st.caption('Automatisch aus content/Day16.md erzeugte Kurs-App')


st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
