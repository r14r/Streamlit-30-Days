import streamlit as st

st.set_page_config(page_title='Day1 - Course App', layout='centered')
st.title('Day1: Setting up a local development environment')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day1.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown("# Setting up a local development environment\n\nBefore we can actually start building Streamlit apps, we will first have to setup a development environment.\n\nLet's start by installing and setting up a conda environment.\n\n## **Install conda**\n- Install `conda` by going to https://docs.conda.io/en/latest/miniconda.html and choose your operating system (Windows, Mac or Linux). \n- Download and run the installer to install `conda`.\n\n## **Create a new conda environment**\nNow that you have conda installed, let's create a conda environment for managing all the Python library dependencies.\n\nTo create a new environment with Python 3.9, enter the following:\n```bash\nconda create -n stenv python=3.9\n```\n\nwhere `create -n stenv` will create a conda environment named `stenv` and `python=3.9` will setup the conda environment with Python version 3.9.\n\n## **Activate the conda environment**\n\nTo use a conda environment that we had just created that is named `stenv`, enter the following into the command line:\n\n```bash\nconda activate stenv\n```\n\n## **Install the Streamlit library**\n\nIt's now time to install the `streamlit` library:\n```bash\npip install streamlit\n```\n\n## **Launching the Streamlit demo app**\nTo launch the Streamlit demo app (Figure 1) type:\n```bash\nstreamlit hello\n```\n")

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
    st.checkbox(f'{i}. {s}', key='Day1_'+str(i))
