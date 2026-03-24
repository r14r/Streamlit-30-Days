import streamlit as st

st.set_page_config(page_title='Day29 - Course App', layout='centered')
st.title('Day29: How to make a zero-shot learning text classifier using Hugging Face and Streamlit')
st.caption('Interaktive Umsetzung ohne Original-Python-Code')

st.subheader('Tagesziel')
st.write('Diese App bildet die Inhalte aus `content/Day29.md` als interaktive Lernstation ab.')

with st.expander('Originalinhalt anzeigen'):
    st.markdown("# How to make a zero-shot learning text classifier using Hugging Face and Streamlit\n\nIn today's challenge, [Charly Wargnier](https://twitter.com/DataChaz) will walk us through the process of developing a zero-shot learning text classifier using Hugging Face and Streamlit.\n\n## Introduction\n\nHey Streamliters!\n\nToday I'm excited to have the opportunity to contribute to the 30DaysofStreamlit challenge via this hands-on tutorial! 🎈\n\n## What are we building?\n\nWe will create a zero-shot learning text classifier using Hugging Face's API inference and Distilbart!\n\nYou will have the mighty power to classify keyphrases on-the-fly, fast, and without pre ML training!\n\nCreate classifying labels, paste your keyphrases, and you're off!\n\nYou can set these labels anything, e.g.:\n\n- Positive, Negative and Neutral for sentiment analysis\n- Angry, Happy, Emotional for emotion analysis\n- Navigational, Transactional, Informational for intent classification purposes\n- Your product range  (bags, shoes, boots etc.)\n\nYou decide! \n\nExcited? Let's dive in! \n\n## Read the full blog\n👉 [Read the full blog](https://www.charlywargnier.com/post/how-to-create-a-zero-shot-learning-text-classifier-using-hugging-face-and-streamlit)\n\n")

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
    st.checkbox(f'{i}. {s}', key='Day29_'+str(i))
