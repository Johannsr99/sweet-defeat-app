import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sweet Defeat – Nutrition Check", page_icon="🍽️", layout="centered")

st.title("🍽️ Sweet Defeat – Nutrition Check")
st.subheader("Lade ein Foto deiner Mahlzeit hoch und erhalte Nährwertinfos.")

uploaded_file = st.file_uploader("📸 Lade dein Essensfoto hoch", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Dein Foto", use_column_width=True)

    st.info("🔍 Die Erkennung läuft... (Dies ist ein Demo-Ergebnis)")

    # Simuliertes Beispielergebnis
    st.success("🍝 Erkanntes Gericht: Pasta mit Tomatensauce")

    st.markdown("""
    **Nährwerte pro Portion (geschätzt):**
    - Kalorien: 420 kcal  
    - Kohlenhydrate: 65 g  
    - Eiweiß: 12 g  
    - Fett: 10 g  
    - Ballaststoffe: 4 g
    """)

    st.markdown("---")
    st.markdown("👉 [Zurück zum Chat](https://dein-mobilecoach-link.de)")
else:
    st.warning("Bitte lade ein Bild hoch, um fortzufahren.")
