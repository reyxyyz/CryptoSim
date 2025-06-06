# File: Home.py
import streamlit as st

st.set_page_config(page_title="CryptoApp", layout="centered")

st.title("🔐 CryptoApp: Simulasi Kriptografi Interaktif")
st.markdown("""
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
