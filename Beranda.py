import streamlit as st

# Mengatur judul halaman
st.set_page_config(page_title="DIGICEK", layout="wide")

# Custom CSS untuk styling
st.markdown("""
    <style>
        .hero-text h1 {
            font-size: 2.5em;
            color: #007bff;
            margin-bottom: 20px;
        }
        .hero-text p {
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .hero-image {
            margin-top: 50px;
        }
        .button-container {
            display: flex;
            gap: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 30px; background-color: #fff; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); border-radius: 10px;">
        <div style="font-size: 1.8em; font-weight: bold; color: #007bff;">DIGICEK</div>
        <a href="#" style="padding: 8px 15px; background-color: #007bff; color: #fff; border-radius: 20px; text-decoration: none; font-weight: bold;">Kontak Kami</a>
    </div>
""", unsafe_allow_html=True)

# HERO SECTION
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="hero-text">
            <h1>Ayo Check Kesehatanmu Sekarang</h1>
            <p>DIGICEK hadir sebagai solusi untuk deteksi dini penyakit diabetes dan gagal ginjal. Mulailah tindakan proaktif untuk menjaga kesehatan Anda.</p>
        </div>
    """, unsafe_allow_html=True)

    # Membuat tombol untuk berpindah ke halaman prediksi
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("Cek Diabetes", use_container_width=True):
            st.switch_page("pages/Deteksi Diabetes.py")  # Sesuaikan dengan path halaman di Streamlit
    
    with col_btn2:
        if st.button("Cek Gagal Ginjal", use_container_width=True):
            st.switch_page("pages/Deteksi Gagal Ginjal.py")  # Sesuaikan dengan path halaman di Streamlit

with col2:
    st.markdown('<div class="hero-image">', unsafe_allow_html=True)
    st.image("image/ilustrasi.png", width=300)  # Ganti dengan path gambar yang sesuai
    st.markdown('</div>', unsafe_allow_html=True)
