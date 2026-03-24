import streamlit as st

st.set_page_config(page_title='Day7 - Course App', layout='centered')
st.title('Day7: Deploying your Streamlit app with Streamlit Community Cloud')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day7.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown('# Deploying your Streamlit app with Streamlit Community Cloud\n\n## Streamlit Community Cloud\n\n[Streamlit Community Cloud](https://streamlit.io/cloud) is a hosting service for easily deploying Streamlit apps.\n\n## Sign up for Streamlit Community Cloud\n\nYou can easily sign up for [Streamlit Community Cloud](https://streamlit.io/cloud) by simply logging in with Google or GitHub account.\n\n## Deploy a Streamlit app\n\nTo deploy a Streamlit app, do the following:\n1. Sign in with GitHub or Gmail credentials\n2. Pick a repo, branch and file\n3. Click Deploy\n\nThen any time you do a git push your app will update immediately.\n')

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
    st.checkbox(f'{i}. {s}', key='Day7_'+str(i))
