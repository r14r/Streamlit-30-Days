import streamlit as st

st.set_page_config(page_title='Day2 - Course App', layout='centered')
st.title('Day2: Building your first Streamlit app')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day2.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown("# Building your first Streamlit app\n\n## Fire up your IDE\n\nFire up your IDE whether it be Atom, VS Code or even a cloud IDE such as GitPod or GitHub.dev.\n\nCreate a file called `streamlit_app.py`\n\n## Entering your first lines of code\n\nTo the newly created file, enter the following lines of code:\n\n```\nimport streamlit as st\n\nst.write('Hello world!')\n```\n\nSave the file.\n\n## Fire up the command line terminal\n\nTo the terminal, enter the following:\n\n```\nstreamlit run streamlit_app.py\n```\n\nA browser window should pop-up showing the newly created Streamlit app.\n\n**Congratulations!** You have just created your first Streamlit app!\n")

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
    st.checkbox(f'{i}. {s}', key='Day2_'+str(i))
