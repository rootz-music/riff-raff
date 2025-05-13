
import streamlit as st
from generator_core import generate_bars, generate_hook

st.set_page_config(page_title="Riff Raff Generator", layout="centered")

st.title("🎤 Riff Raff Lyric Generator")
st.subheader("Build-a-Bar: Surreal Swag Edition")

persona = st.selectbox("Choose your Persona", ["Neon Alien", "Beach Riff", "Snakeskin Tycoon", "Retro Arcade Savage"])
theme = st.selectbox("Theme", ["Fashion", "Flexing", "Snacks", "Sci-Fi", "Random"])
mode = st.radio("Mode", ["4-Bar Verse", "Hook Generator"])
flex_level = st.slider("💎 Flex Level", 1, 10, 7)
nonsense = st.slider("🌀 Nonsense Juice", 0, 10, 5)

if st.button("Generate"):
    if mode == "4-Bar Verse":
        st.text(generate_bars(persona, theme, flex_level, nonsense))
    else:
        st.text(generate_hook(persona, theme, flex_level, nonsense))
