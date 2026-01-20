import streamlit as st
from languages.ebira import translate as ebira_lang
from languages.yoruba import translate as yoruba_lang
from languages.igbo import translate as igbo_lang
from languages.hausa import translate as hausa_lang
from languages.calabar import translate as calabar_lang


st.title("SIMDB TRANSLATOR APP")

language = st.selectbox(
    "Choose a language",
    ("Ebira","Igbo","Hausa","Yoruba","Calabar")
)

word = st.text_input("Enter a word in english: ", placeholder="e.g water,food, money")
if st.button("Translate"):
    if word.strip() == "":
        st.warning("Please enter a word!")
    else:
        if language == "Ebira":
            result = ebira_lang(word)
        elif language == "Igbo":
            result = igbo_lang(word)
        elif language == "Hausa":
            result = hausa_lang(word)
        elif language == "Yoruba":
            result = yoruba_lang(word)
        elif language == "Calabar":
            result = calabar_lang(word)
        st.success(result)