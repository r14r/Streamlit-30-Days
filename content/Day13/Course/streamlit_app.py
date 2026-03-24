import streamlit as st

st.set_page_config(page_title='Day13 - Course App', layout='centered')
st.title('Day13: Spin up a cloud development environment')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day13.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown('# Spin up a cloud development environment\n\n### GitPod\nTo spin up a development environment on the cloud, we can use [GitPod](https://www.gitpod.io/) and this can be done simply by clicking on the following link:\n- Try it 👉 https://gitpod.io/#/https://github.com/dataprofessor/streamlit101/\n\nAs you can see from the URL above, a GitHub repo URL is appended after `https://gitpod.io/#/` which essentially allow GitPod to spin up a development environment using instructions contained within the GitHub repo URL (namely in the `requirements.txt` file that specifically lists the Python libraries to install).\n\n> Note: There are other similar cloud development environment such as:\n> - [GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-python-project-for-codespaces)\n> - [Replit](https://replit.com/)\n> - [Cloud9](https://aws.amazon.com/cloud9/)\n')

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
    st.checkbox(f'{i}. {s}', key='Day13_'+str(i))
