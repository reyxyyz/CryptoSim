# File: Home.py
import streamlit as st

st.set_page_config(page_title="CryptoApp", layout="centered")

st.title("🔐 CryptoApp: Simulasi Kriptografi Interaktif")
st.markdown("""# File: app.py
import streamlit as st
from utils import caesar, vigenere, rsa  # pastikan folder utils ada

st.set_page_config(page_title="CryptoApp", layout="wide")
st.title("🔐 CryptoApp: Aplikasi Kriptografi Interaktif")

# Sidebar Navigation
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Caesar Cipher", "Vigenère Cipher", "RSA Encryption"])

# Halaman Beranda
if menu == "Beranda":
    st.markdown("""
    ## Selamat Datang di CryptoApp
    Aplikasi ini membantu Anda belajar dan mensimulasikan berbagai algoritma kriptografi.
    
    - 🔁 Enkripsi & Dekripsi pesan
    - 📊 Membandingkan algoritma
    - 📚 Edukasi kriptografi klasik & modern
    
    Pilih algoritma di sidebar untuk mulai.
    """)

# Caesar Cipher
elif menu == "Caesar Cipher":
    st.subheader("🔁 Caesar Cipher")
    text = st.text_input("Masukkan teks")
    shift = st.slider("Pergeseran", 1, 25, 3)
    mode = st.radio("Mode", ["Enkripsi", "Dekripsi"])
    
    if text:
        if mode == "Enkripsi":
            result = caesar.encrypt_caesar(text, shift)
        else:
            result = caesar.decrypt_caesar(text, shift)
        st.success(f"Hasil: {result}")

# Vigenère Cipher
elif menu == "Vigenère Cipher":
    st.subheader("🔑 Vigenère Cipher")
    text = st.text_input("Masukkan teks")
    key = st.text_input("Masukkan kunci")
    mode = st.radio("Mode", ["Enkripsi", "Dekripsi"])

    if text and key:
        if mode == "Enkripsi":
            result = vigenere.encrypt_vigenere(text, key)
        else:
            result = vigenere.decrypt_vigenere(text, key)
        st.success(f"Hasil: {result}")

# RSA Encryption (simulasi)
elif menu == "RSA Encryption":
    st.subheader("🔐 RSA Encryption")
    st.markdown("Simulasi RSA sederhana: akan dibuat kunci public-private secara otomatis.")
    text = st.text_input("Masukkan teks (max 100 karakter)")

    if text:
        public, private = rsa.generate_keys()
        encrypted = rsa.encrypt_rsa(text, public)
        decrypted = rsa.decrypt_rsa(encrypted, private)
        
        st.code(f"Enkripsi: {encrypted}")
        st.code(f"Dekripsi: {decrypted}")

Selamat datang di **CryptoApp**, aplikasi interaktif untuk mempelajari dan mencoba algoritma kriptografi klasik dan modern.

Navigasi di sidebar untuk:
- 🔁 Enkripsi & Dekripsi teks
- 📊 Membandingkan algoritma
- 🧠 Belajar kriptografi secara interaktif

---

**Dibuat untuk Tugas UAS - Pemrograman Kriptografi**
""")

st.markdown("""
### 📄 Navigasi Halaman

Pilih halaman di sidebar (kiri layar):
- **Caesar Cipher**  → Enkripsi/Dekripsi dengan pergeseran huruf
- **Vigenère Cipher** → Enkripsi dengan kata kunci
- **RSA Encryption** → Enkripsi menggunakan kunci publik/pribadi
- **Perbandingan Algoritma** → Bandingkan kekuatan & kecepatan

Selamat bereksplorasi! 🔐✨
""")
