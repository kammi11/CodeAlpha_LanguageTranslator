import streamlit as st
from deep_translator import GoogleTranslator

LANGUAGES = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de",
    "Urdu": "ur", "Arabic": "ar", "Chinese": "zh-CN", "Hindi": "hi",
    "Turkish": "tr", "Russian": "ru", "Japanese": "ja", "Italian": "it"
}

st.set_page_config(page_title="Language Translator", page_icon="\U0001F310")
st.title("\U0001F310 Language Translation Tool")

text = st.text_area("Enter text to translate", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=4)

def translate(text, source, target):
    return GoogleTranslator(source=source, target=target).translate(text)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            try:
                result = translate(text, LANGUAGES[source_lang], LANGUAGES[target_lang])
                st.success("Translation complete")
                st.text_area("Translated Text", value=result, height=150)
            except Exception as e:
                st.error(f"Translation failed: {e}")
