import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="SmartParenting AI",
    page_icon="🌸",
    layout="centered"
)

# --- 2. STYLE CSS (Tampilan Cantik & Friendly) ---
st.markdown("""
    <style>
    .main { background-color: #fff5f7; }
    .stButton>button {
        background-color: #ff85a2;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
    }
    .stTextInput>div>div>input { border-radius: 15px; }
    h1 { color: #d63384; font-family: 'sans-serif'; }
    h3 { color: #d63384; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. KONEKSI API & SYSTEM INSTRUCTION ---
try:
    # Mengambil API Key dari Secrets Streamlit
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Menanamkan Knowledge Psikologi & Kimia
    SYSTEM_INSTRUCTION = """
    Identitas: Anda adalah 'Bunda AI', asisten pribadi yang hangat dan cerdas.
    Keahlian: Psikologi Parenting (Positive Discipline) dan Edukasi Kimia Dasar.
    Gaya Bahasa: Gunakan panggilan 'Bunda/Ayah'. Awali dengan validasi empati. 
    Contoh: "Bunda, saya mengerti itu melelahkan..."
    Tujuan: Mengubah emosi menjadi edukasi dan komunikasi positif.
    """
    
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=SYSTEM_INSTRUCTION
    )
except Exception as e:
    st.error(f"⚠️ Masalah API Key: Pastikan GOOGLE_API_KEY sudah ada di Secrets Streamlit. Error: {e}")

# --- 4. UI APLIKASI ---
st.title("🌸 Bunda AI")
st.subheader("Teman Cerdas untuk Pengasuhan Penuh Kasih")

tabs = st.tabs(["✨ Anti-Bentak", "🧪 Ide Main Sains", "📝 Cek Mood Bunda"])

# --- TAB 1: ANTI-BENTAK ---
with tabs[0]:
    st.write("### Ubah Marah Jadi Kata Indah")
    raw_text = st.text_input("Apa yang ingin Bunda sampaikan ke si Kecil?", placeholder="Contoh: Jangan lari-lari nanti jatuh!", key="input1")
    if st.button("Ubah Kalimat ✨"):
        if raw_text:
            with st.spinner('Berpikir...'):
                res = model.generate_content(f"Ubah kalimat ini agar positif & edukatif: {raw_text}")
                st.success(res.text)
        else:
            st.warning("Tuliskan sesuatu dulu ya, Bunda.")

# --- TAB 2: IDE MAIN SAINS ---
with tabs[1]:
    st.write("### Main Sambil Belajar Kimia")
    kondisi = st.text_input("Bagaimana suasana hati si Kecil?", placeholder="Contoh: Lagi bosan/sedih/hiperaktif", key="input2")
    if st.button("Cari Ide Main 🧪"):
        if kondisi:
            with st.spinner('Mencari ide seru...'):
                res = model.generate_content(f"Berikan 1 aktivitas sensory play kimia sederhana untuk anak yang sedang {kondisi}")
                st.info(res.text)
        else:
            st.warning("Ceritakan kondisi si Kecil dulu ya, Bunda.")

# --- TAB 3: CEK MOOD ---
with tabs[2]:
    st.write("### Ruang Curhat Bunda")
    jurnal = st.text_area("Ceritakan harimu di sini...", placeholder="Hari ini aku merasa...", key="input3")
    if st.button("Analisis Mood 📝"):
        if jurnal:
            with st.spinner('Mendengarkan curhatan Bunda...'):
                res = model.generate_content(f"Analisis jurnal ini, berikan semangat dan tips self-care singkat: {jurnal}")
                st.warning(res.text)
                st.write("---")
                st.caption("Jika Bunda butuh bantuan ahli, klik tombol di bawah:")
                st.link_button("Chat Psikolog Rekanan", "https://wa.me/628XXXXXXXX")
        else:
            st.warning("Tuliskan curhatan Bunda dulu ya.")
