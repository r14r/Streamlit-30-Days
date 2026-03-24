import streamlit as st

st.set_page_config(page_title='Day6 - Course App', layout='centered')
st.title('Day6: Uploading your Streamlit app to GitHub')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day6.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown('# Uploading your Streamlit app to GitHub\n\n## GitHub\n\nGit is a software for keeping track of all changes made to code (i.e. version control). GitHub is a Git repository hosting service that makes data and code publicly available on the web, which allows team collaboration and allow others to contribute to the repo.\n\nHousing your Streamlit app in a GitHub repository will allow apps to be deployed to the cloud (the next challenge).\n\n## Sign up for GitHub\n\nFirstly, sign up for a [GitHub](https://github.com/) account.\n\n## Create a GitHub repository\n\nFollow the following steps to create a GitHub repository:\n- In the top right hand corner, click on the **"+"** icon which should reveal a drop-down menu, then click on **"New repository"** (*Figure 1*).\n\n- This should bring to a new webpage called **"Create a new repository"**. Under the **"Repository name"** field, enter a name for your repository, for example, `helloworld` (***Figure 2***).\n\n- Under the **"Initialize this repository with:"** field, tick on **"Add a README file"**.\n\n- Finally, click on **"Create repository"** (Figure 3).\n\nYour newly created repository will be available at `https://github.com/dataprofessor/helloworld` where `dataprofessor` is the username and `helloworld` is the repository name.\n\nBelow is the screenshot of the newly created repo (Figure 4):\n\n## Upload files to the GitHub repo\n\nSlightly above the file table and adjacent to the green **Code** button, click on **Add file** > **Upload files** (Figure 5).\n\nThis will bring you to a new webpage where the central box says ***Drag files here to add them to your repository*** and **choose your files**, which you can either drag-and-drop files into this box or click on the **choose your files** link to choose files from your local computer.\n\nClick on **Commit changes** to proceed further (Figure 6).\n')

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
    st.checkbox(f'{i}. {s}', key='Day6_'+str(i))
