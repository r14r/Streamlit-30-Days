import streamlit as st

st.set_page_config(page_title='Day4 - Course App', layout='centered')
st.title('Day4: Building Streamlit apps with Ken Jee')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day4.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown("# Building Streamlit apps with Ken Jee\n\n## Watch Ken's video\n\nLet's follow along and watch how [Ken Jee](https://www.youtube.com/c/KenJee1) builds a Streamlit app in this video:\n\n[![Data Science Portfolio Project from Scratch](https://img.youtube.com/vi/Yk-unX4KnV4/0.jpg)](<https://www.youtube.com/watch?v=Yk-unX4KnV4>)]\n")

st.subheader('10-Schritte-Checkliste')
steps=[
    'Lies die Tagesbeschreibung vollständig durch.',
    'Öffne alle verlinkten Ressourcen (Video, Blog, Tools).',
    'Lege eine neue Datei `streamlit_app.py` an.',
    'Übernimm die Kernidee des Tages in eine App-Struktur.',
    'Füge eine klare Überschrift und kurze Beschreibung hinzu.',
    'Baue mindestens ein interaktives Eingabeelement ein.',
    'Implementiere die zentrale Funktion aus der Tagesaufgabe.',
    'Zeige das Ergebnis nutzerfreundlich im Hauptbereich an.',
    'Teste die App lokal mit `streamlit run streamlit_app.py`.',
    'Dokumentiere das Ergebnis in der README dieses Course-Ordners.'
]
for i,s in enumerate(steps,1):
    st.checkbox(f'{i}. {s}', key='Day4_'+str(i))
