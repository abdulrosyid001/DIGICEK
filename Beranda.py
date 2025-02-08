import streamlit as st

# Mengatur judul halaman
st.set_page_config(page_title="DIGICEK", layout="wide")

# Custom CSS untuk styling
st.markdown("""
    <style>
        .hero-text {
            margin-left: 30px; /* Memindahkan teks lebih ke kiri */
        }
        .hero-text h1 {
            font-size: 2.5em;
            color: #007bff;
            margin-bottom: 20px;
        }
        .hero-text p {
            font-size: 1.2em;
            margin-bottom: 40px;
        }
        .hero-image-container {
            text-align: right;
        }
        .button-container {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        .contact-button {
            padding: 8px 15px;
            background-color: #007bff;
            color: #fff;
            border-radius: 20px;
            text-decoration: none;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER dengan popover untuk kontak
col_header1, col_header2 = st.columns([1, 0.2])
with col_header1:
    st.markdown("<div style='font-size: 1.8em; font-weight: bold; color: #007bff;'>DIGICEK</div>", unsafe_allow_html=True)

with col_header2:
    with st.popover("📞 Kontak Kami"):
        st.markdown("""
        **Hubungi Kami:**  
        📸 Instagram: [@digicek](https://instagram.com/digicek)  
        📺 YouTube: [DIGICEK Official](https://youtube.com/digicek)  
        📧 Email: [info@digicek.com](mailto:info@digicek.com)
        """)

# HERO SECTION (Menambahkan 1 kolom kosong di tengah)
col1, col_empty, col2 = st.columns([2.5, 1, 1.5])

with col1:
    st.markdown("""
        <div class="hero-text">
            <h1>Ayo Check Kesehatanmu Sekarang</h1>
            <p>DIGICEK hadir sebagai solusi untuk deteksi dini penyakit diabetes dan gagal ginjal. Mulailah tindakan proaktif untuk menjaga kesehatan Anda.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Membuat tombol untuk berpindah ke halaman prediksi
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("Cek Diabetes", use_container_width=True):
            st.switch_page("pages/Deteksi Diabetes.py")

    with col_btn2:
        if st.button("Cek Gagal Ginjal", use_container_width=True):
            st.switch_page("pages/Deteksi Gagal Ginjal.py")

# Kolom kosong di tengah
with col_empty:
    st.write("")  # Biarkan kosong untuk memberi jarak

# Kolom gambar
with col2:
    st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
    st.image("image/ilustrasi.png", width=350)
    st.markdown('</div>', unsafe_allow_html=True)
