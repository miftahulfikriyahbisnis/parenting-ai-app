import streamlit as st
import google.generativeai as genai

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Bunda AI - Cerdas & Hangat",
    page_icon="🌸",
    layout="centered"
)

# --- 2. STYLE CSS (Tampilan Cantik & Friendly) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fffafb;
    }
    .main {
        padding: 2rem;
    }
    .stButton>button {
        background-color: #ff85a2;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.6rem 2rem;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ef7091;
        border: none;
    }
    h1 {
        color: #d63384;
        text-align: center;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        border-radius: 15px;
        border: 1px solid #ffc1d1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. KONEKSI & INISIALISASI AI ---
# Kita pakai try-except agar jika API bermasalah, aplikasi tidak langsung mati
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
    else:
        st.error("❌ API Key belum diatur di Streamlit Secrets!")
        st.stop()
except Exception as e:
    st.error(f"Terjadi kesalahan konfigurasi: {e}")
    st.stop()

# Menanamkan Pengetahuan Psikologi & Kimia langsung di System Instruction
KNOWLEDGE_BASE = """
IDENTITAS: Anda adalah 'Bunda AI', asisten pribadi yang hangat dan sabar untuk orang tua. 
KUALIFIKASI: Anda ahli dalam Psikologi Parenting (Positive Discipline) dan Dosen Pendidikan Kimia.

ATURAN KOMUNIKASI:
1. Validasi Emosi: Selalu mulai dengan empati (Contoh: "Bunda mengerti, itu memang melelahkan...").
2. Transformasi Positif: Ubah larangan jadi ajakan. Ganti "Jangan" dengan "Ayo" atau "Boleh setelah...".
3. Sentuhan Sains: Setiap kali memberikan saran aktivitas, hubungkan dengan ilmu kimia sederhana yang ada di rumah (misal: polimer tepung, reaksi cuka, kristalisasi gula).

GAYA BAHASA: Sopan, hangat, keibuan, tapi cerdas. Panggil pengguna dengan 'Bunda' atau 'Ayah'.
"""

# Menggunakan model yang paling stabil
try:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=KNOWLEDGE_BASE
    )
except Exception as e:
    st.error(f"Gagal memuat model AI: {e}")
    st.stop()

# --- 4. TAMPILAN ANTARMUKA (UI) ---
st.title("🌸 Bunda AI")
st.markdown("<p style='text-align: center; color: #888;'>Asisten Cerdas untuk Pengasuhan Penuh Kasih</p>", unsafe_allow_html=True)

# Membuat Menu Tab
tabs = st.tabs(["✨ Anti-Bentak", "🧪 Main Sains", "📝 Ruang Curhat"])

# --- TAB 1: ANTI-BENTAK ---
with tabs[0]:
    st.write("### 💬 Ubah Kata-kata")
    st.write("Tulis apa yang ingin Bunda ucapkan, AI akan mengubahnya menjadi lebih lembut.")
    raw_text = st.text_input("Kalimat Bunda:", placeholder="Contoh: Adek jangan lari-lari nanti jatuh!")
    
    if st.button("Ubah Menjadi Positif ✨"):
        if raw_text:
            with st.spinner('Berpikir sejenak...'):
                try:
                    prompt = f"Ubah kalimat ini sesuai prinsip Positive Discipline: '{raw_text}'"
                    response = model.generate_content(prompt)
                    st.success("**Saran Bunda AI:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Aduh, ada gangguan teknis: {e}")
        else:
            st.warning("Tuliskan kalimatnya dulu ya, Bunda.")

# --- TAB 2: MAIN SAINS ---
with tabs[1]:
    st.write("### 🧪 Ide Bermain Edukatif")
    st.write("Dapatkan ide sensory play kimia sederhana berdasarkan mood anak.")
    kondisi = st.text_input("Suasana hati si Kecil saat ini?", placeholder="Contoh: Sedang tantrum / bosan / hiperaktif")
    
    if st.button("Dapatkan Inspirasi Main 🎨"):
        if kondisi:
            with st.spinner('Mencari ide seru...'):
                try:
                    prompt = f"Berikan 1 ide aktivitas sensory play berbasis kimia sederhana untuk anak yang sedang {kondisi}."
                    response = model.generate_content(prompt)
                    st.info("**Coba aktivitas ini yuk, Bunda:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Aplikasi sedang lelah, coba lagi ya: {e}")
        else:
            st.warning("Ceritakan sedikit kondisi si Kecil dulu ya.")

# --- TAB 3: RUANG CURHAT ---
with tabs[2]:
    st.write("### 📝 Jurnal Bunda")
    st.write("Keluarkan unek-unek Bunda hari ini. Kami akan menjaga rahasianya.")
    jurnal = st.text_area("Bagaimana perasaan Bunda hari ini?", placeholder="Hari ini sangat melelahkan karena...")
    
    if st.button("Analisis Mood Bunda ❤️"):
        if jurnal:
            with st.spinner('Mendengarkan curhatan Bunda...'):
                try:
                    prompt = f"Analisis jurnal ini, berikan dukungan moral dan tips self-care singkat: '{jurnal}'"
                    response = model.generate_content(prompt)
                    st.warning("**Pesan untuk Bunda:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Maaf, AI gagal menganalisis: {e}")
            
            st.divider()
            st.markdown("---")
            st.write("🆘 **Butuh bantuan profesional?**")
            st.link_button("Chat Psikolog Rekanan (WhatsApp)", "https://wa.me/628123456789")
        else:
            st.warning("Tuliskan curhatan Bunda dulu ya.")

st.markdown("<br><hr><center><small>Powered by Gemini AI | Created by Your Coach</small></center>", unsafe_allow_html=True)
