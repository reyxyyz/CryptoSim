from streamlit_option_menu import option_menu
import streamlit as st
from Crypto.Cipher import AES, DES, Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import random

st.set_page_config(page_title="CryptoSim", layout="wide")

# Tambahkan setelah import
st.markdown(
    """
    <style>
        .stApp {
            background-color: #9EC6F3;
        }
    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar:
    selected = option_menu(
        menu_title="CryptoSim Menu",
        options=[
            "Beranda", "Caesar Cipher", "Substitution Cipher", "ROT13", "XOR Cipher",
            "Vigenère Cipher", "AES", "RSA", "DES", "Blowfish", "ElGamal"
        ],
        icons=[
            "house", "file-text", "repeat", "repeat", "code",
            "key", "lock", "shield-lock", "lock-fill", "lightning", "shield"
        ],
        menu_icon="app-indicator",
        default_index=0,
    )

st.markdown(
    """
    <style>
    /* Ubah warna latar belakang sidebar secara keseluruhan */
    section[data-testid="stSidebar"] {
        background-color: #d0f0f9; /* biru muda */
    }

    /* Ubah latar menu container utama dalam sidebar */
    div[data-testid="stSidebarNav"] {
        background-color: #ffffff10; /* transparan lembut */
        border-radius: 12px;
        padding: 10px;
        margin-top: 20px;
    }

    /* Ubah background tombol aktif (halaman yang sedang dipilih) */
    div[data-testid="stSidebarNav"] ul li button[aria-current="page"] {
        background-color: #ff5252 !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Ubah teks pada judul menu */
    div[data-testid="stSidebarNav"] h2 {
        color: #004d40;
    }

    /* Gaya tambahan: hover item menu */
    div[data-testid="stSidebarNav"] ul li button:hover {
        background-color: #e0f2f1 !important;
        color: #004d40 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def caesar_cipher(text, shift, mode):
    if mode == "Dekripsi":
        shift = -shift
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def substitution_cipher(text, key, mode):
    import string
    alphabet = string.ascii_lowercase
    key = key.lower()
    if len(key) != 26 or not key.isalpha():
        return "Kunci harus 26 huruf alfabet."
    mapping_enc = {alphabet[i]: key[i] for i in range(26)}
    mapping_dec = {v: k for k, v in mapping_enc.items()}
    mapping = mapping_enc if mode == "Enkripsi" else mapping_dec
    result = ""
    for c in text:
        low = c.lower()
        if low in mapping:
            new_c = mapping[low]
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def rot13(text):
    return caesar_cipher(text, 13, "Enkripsi")

def xor_cipher(text, key):
    key_ord = ord(key) if key else 0
    result = ""
    for c in text:
        result += chr(ord(c) ^ key_ord)
    return result

def vigenere_cipher(text, key, mode):
    result = ""
    key = key.lower()
    key_len = len(key)
    key_int = [ord(i) - 97 for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            base = 65 if char.isupper() else 97
            key_char = key_int[i % key_len]
            if mode == "Enkripsi":
                result += chr((ord(char) - base + key_char) % 26 + base)
            else:
                result += chr((ord(char) - base - key_char) % 26 + base)
        else:
            result += char
    return result

def aes_encrypt_decrypt(text, key, mode):
    try:
        key_bytes = key.encode('utf-8')
        key_bytes = key_bytes[:16].ljust(16, b'\0')
        cipher = AES.new(key_bytes, AES.MODE_ECB)
        if mode == "Enkripsi":
            ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
            return base64.b64encode(ct_bytes).decode('utf-8')
        else:
            ct = base64.b64decode(text)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            return pt.decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"

def rsa_encrypt_decrypt(text, mode):
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher_rsa_enc = PKCS1_OAEP.new(public_key)
    cipher_rsa_dec = PKCS1_OAEP.new(key)
    try:
        if mode == "Enkripsi":
            encrypted = cipher_rsa_enc.encrypt(text.encode('utf-8'))
            return base64.b64encode(encrypted).decode('utf-8')
        else:
            decoded = base64.b64decode(text)
            decrypted = cipher_rsa_dec.decrypt(decoded)
            return decrypted.decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"

def des_encrypt_decrypt(text, key, mode):
    try:
        key_bytes = key.encode('utf-8')
        key_bytes = key_bytes[:8].ljust(8, b'\0')
        cipher = DES.new(key_bytes, DES.MODE_ECB)
        if mode == "Enkripsi":
            ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), DES.block_size))
            return base64.b64encode(ct_bytes).decode('utf-8')
        else:
            ct = base64.b64decode(text)
            pt = unpad(cipher.decrypt(ct), DES.block_size)
            return pt.decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"

def blowfish_encrypt_decrypt(text, key, mode):
    try:
        key_bytes = key.encode('utf-8')
        cipher = Blowfish.new(key_bytes, Blowfish.MODE_ECB)
        if mode == "Enkripsi":
            ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), Blowfish.block_size))
            return base64.b64encode(ct_bytes).decode('utf-8')
        else:
            ct = base64.b64decode(text)
            pt = unpad(cipher.decrypt(ct), Blowfish.block_size)
            return pt.decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"

if selected == "Beranda":
    st.title("🏠 CryptoSim")
    st.markdown("""
    ### Selamat datang di **CryptoSim** — simulasi enkripsi dan dekripsi algoritma klasik & modern.

    Pilih menu di sidebar untuk mencoba berbagai algoritma enkripsi dan dekripsi.

    _Dibuat untuk tugas UAS Pemrograman Kriptografi._
    """)

elif selected == "Caesar Cipher":
    st.title("🔁 Caesar Cipher")
    st.write("Caesar Cipher adalah metode enkripsi dengan menggeser huruf dalam alfabet.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    shift = st.slider("Pergeseran (shift):", 1, 25, 3)
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text:
            st.warning("Masukkan teks terlebih dahulu!")
        else:
            hasil = caesar_cipher(text, shift, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "Substitution Cipher":
    st.title("🔤 Substitution Cipher")
    st.write("Menggantikan setiap huruf dengan huruf lain sesuai kunci alfabet.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    key = st.text_input("Masukkan kunci (26 huruf):", placeholder="qwertyuiopasdfghjklzxcvbnm")
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text or len(key) != 26:
            st.warning("Masukkan teks dan kunci yang valid (26 huruf)!")
        else:
            hasil = substitution_cipher(text, key, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "ROT13":
    st.title("🔄 ROT13")
    st.write("ROT13 adalah Caesar Cipher dengan pergeseran 13, digunakan untuk 'membalik' teks.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    if st.button("Proses"):
        if not text:
            st.warning("Masukkan teks terlebih dahulu!")
        else:
            hasil = rot13(text)
            st.success(f"Hasil: {hasil}")

elif selected == "XOR Cipher":
    st.title("🛡️ XOR Cipher")
    mode = st.radio("Pilih Mode:", ["Enkripsi", "Dekripsi"])
    text = st.text_input("Masukkan teks:")
    key = st.text_input("Masukkan kunci:")

    if st.button("Proses"):
        if not key:
            st.error("Kunci tidak boleh kosong!")
        else:
            hasil = xor_cipher(text, key)
            if mode == "Enkripsi":
                # Untuk enkripsi, tampilkan dalam format hexadecimal agar bisa dibaca
                hasil_hex = hasil.encode().hex()
                st.success(f"Hasil Enkripsi (hex): {hasil_hex}")
            else:
                try:
                    # Coba decode dari hex
                    decoded_text = bytes.fromhex(text).decode()
                    hasil = xor_cipher(decoded_text, key)
                    st.success(f"Hasil Dekripsi: {hasil}")
                except:
                    st.error("Teks yang dimasukkan harus dalam format hex hasil enkripsi!")

elif selected == "Vigenère Cipher":
    st.title("🔑 Vigenère Cipher")
    st.write("Vigenère Cipher mengenkripsi teks dengan kunci berupa kata, menggunakan pergeseran yang bervariasi.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    key = st.text_input("Masukkan kunci:", placeholder="kunci")
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text or not key:
            st.warning("Masukkan teks dan kunci terlebih dahulu!")
        else:
            hasil = vigenere_cipher(text, key, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "AES":
    st.title("🔐 AES (Advanced Encryption Standard)")
    st.write("AES adalah algoritma enkripsi blok modern yang kuat. Gunakan kunci 16 karakter.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    key = st.text_input("Masukkan kunci (16 karakter):", max_chars=16)
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text or len(key) != 16:
            st.warning("Masukkan teks dan kunci 16 karakter!")
        else:
            hasil = aes_encrypt_decrypt(text, key, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "RSA":
    st.title("🔐 RSA Encryption")
    st.write("RSA adalah kriptografi kunci publik. Ini simulasi sederhana dengan key baru tiap proses.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text:
            st.warning("Masukkan teks terlebih dahulu!")
        else:
            hasil = rsa_encrypt_decrypt(text, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "DES":
    st.title("🔐 DES (Data Encryption Standard)")
    st.write("DES adalah algoritma enkripsi blok lama. Gunakan kunci 8 karakter.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    key = st.text_input("Masukkan kunci (8 karakter):", max_chars=8)
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text or len(key) != 8:
            st.warning("Masukkan teks dan kunci 8 karakter!")
        else:
            hasil = des_encrypt_decrypt(text, key, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "Blowfish":
    st.title("🔐 Blowfish")
    st.write("Blowfish adalah algoritma enkripsi blok dengan kunci variabel.")
    text = st.text_input("Masukkan teks:", placeholder="Halo Dunia")
    key = st.text_input("Masukkan kunci (minimal 4 karakter):")
    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])
    if st.button("Proses"):
        if not text or len(key) < 4:
            st.warning("Masukkan teks dan kunci minimal 4 karakter!")
        else:
            hasil = blowfish_encrypt_decrypt(text, key, mode)
            st.success(f"Hasil: {hasil}")

elif selected == "ElGamal":
    st.title("🔐 ElGamal Encryption Demo")
    st.markdown("""
    **ElGamal** adalah algoritma kriptografi kunci publik berbasis logaritma diskrit.  
    Pada demo ini, gunakan pesan berupa angka bulat antara 0 sampai p-1.

    Parameter sistem:
    - p (bilangan prima): 467
    - g (generator): 2
    """)

    p = 467
    g = 2

    def generate_keys():
        x = random.randint(1, p - 2)  # private key x
        h = pow(g, x, p)              # public key h = g^x mod p
        return x, h

    def encrypt(m, h):
        y = random.randint(1, p - 2)
        c1 = pow(g, y, p)
        s = pow(h, y, p)
        c2 = (m * s) % p
        return c1, c2

    def decrypt(c1, c2, x):
        s = pow(c1, x, p)
        # s^-1 mod p = inverse modulo
        s_inv = pow(s, p - 2, p)
        m = (c2 * s_inv) % p
        return m

    # Generate keys once
    if 'elgamal_keys' not in st.session_state:
        st.session_state.elgamal_keys = generate_keys()
    x, h = st.session_state.elgamal_keys

    st.write(f"**Public key (p, g, h):** ({p}, {g}, {h})")
    st.write(f"**Private key x:** (disembunyikan)")

    mode = st.radio("Mode:", ["Enkripsi", "Dekripsi"])

    if mode == "Enkripsi":
        m_input = st.number_input(f"Masukkan pesan sebagai bilangan bulat 0 ≤ m < {p}:", min_value=0, max_value=p-1, value=123, step=1)
        if st.button("Enkripsi"):
            c1, c2 = encrypt(m_input, h)
            st.success(f"Ciphertext:\nc1 = {c1}\nc2 = {c2}")

    else:
        c1_input = st.number_input("Masukkan c1 (integer):", min_value=0, max_value=p-1, value=0, step=1)
        c2_input = st.number_input("Masukkan c2 (integer):", min_value=0, max_value=p-1, value=0, step=1)
        if st.button("Dekripsi"):
            if c1_input == 0 and c2_input == 0:
                st.warning("Masukkan ciphertext yang valid!")
            else:
                m = decrypt(c1_input, c2_input, x)
                st.success(f"Pesan asli (plaintext) = {m}")
