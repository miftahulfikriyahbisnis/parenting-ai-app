import streamlit as st
import google.generativeai as genai
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="SmartParenting AI",
    page_icon="🌸",
    layout="centered"
)

# --- STYLE CSS (Agar Friendly buat Ibu-Ibu) ---
st.markdown("""
    <style>
    .main { background-color: #fff5f7; }
    .stButton>button {
        background-color: #ff85a2;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    .stTextInput>div>div>input { border-radius: 15px; }
    h1 { color: #d63384; font-family: 'Comic Sans MS', cursive; }
    </style>
    """, unsafe_allow_supported_types=True)

# --- KONEKSI API ---
# Mengambil API Key dari Secret Streamlit (Lebih Aman)
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("API Key tidak ditemukan. Pastikan sudah di-set di Streamlit Secrets.")

# --- SYSTEM INSTRUCTION (Penanaman Knowledge Psikologi) ---
SYSTEM_INSTRUCTION = """
Identitas: Anda adalah 'Bunda AI', asisten pribadi yang hangat, sabar, dan sangat cerdas dalam Psikologi Parenting serta Kimia Edukasi.
Pengetahuan Inti:
1. Psikologi: Gunakan metode 'Positive Discipline'. Jika user marah, validasi perasaan mereka dulu. Contoh: "Bunda, saya paham itu melelahkan..."
2. Komunikasi: Ubah instruksi negatif (Jangan!) menjadi instruksi positif (Ayo/Boleh).
3. Sains: Hubungkan aktivitas dengan konsep kimia dasar (misal: tekanan udara, polimer tepung, reaksi warna) sebagai cara bonding anak.
Bahasa: Gunakan panggilan 'Bunda/Ayah' agar terasa lebih dekat.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

# --- UI APLIKASI ---
st.title("🌸 Bunda AI")
st.subheader("Teman Cerdas untuk Pengasuhan Penuh Kasih")

tabs = st.tabs(["✨ Anti-Bentak", "🧪 Ide Main Sains", "📝 Cek Mood Bunda"])

with tabs[0]:
    st.write("### Ubah Marah Jadi Kata Indah")
    raw_text = st.text_input("Apa yang ingin Bunda sampaikan ke si Kecil?", placeholder="Contoh: Jangan lari-lari nanti jatuh!")
    if st.button("Ubah Kalimat"):
        res = model.generate_content(f"Ubah kalimat ini agar positif & edukatif: {raw_text}")
        st.success(res.text)

with tabs[1]:
    st.write("### Main Sambil Belajar Kimia")
    kondisi = st.text_input("Bagaimana suasana hati si Kecil?", placeholder="Contoh: Lagi bosan/sedih/hiperaktif")
    if st.button("Cari Ide Main"):
        res = model.generate_content(f"Berikan 1 aktivitas sensory play kimia sederhana untuk anak yang sedang {kondisi}")
        st.info(res.text)

with tabs[2]:
    st.write("### Ruang Curhat Bunda")
    jurnal = st.text_area("Ceritakan harimu di sini...", placeholder="Hari ini aku merasa...")
    if st.button("Analisis Mood"):
        res = model.generate_content(f"Analisis jurnal ini, berikan semangat dan tips self-care singkat: {jurnal}")
        st.warning(res.text)
        st.write("---")
        st.caption("Jika Bunda butuh bantuan ahli, klik tombol di bawah:")
        st.link_button("Chat Psikolog Rekanan", "https://wa.me/628XXXXXXXX")
