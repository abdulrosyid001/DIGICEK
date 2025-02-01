import streamlit as st

# Mengatur judul halaman
st.set_page_config(page_title="DIGICEK", layout="wide")

# Custom CSS untuk styling
st.markdown("""
    <style>
        /* Reset style */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f5f9ff;
            color: #333;
            padding: 20px;
        }

        /* HEADER */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }

        .logo {
            font-size: 1.8em;
            font-weight: bold;
            color: #007bff;
        }

        .nav a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
            margin: 0 15px;
        }

        .contact {
            padding: 8px 15px;
            background-color: #007bff;
            color: #fff;
            border-radius: 20px;
            text-decoration: none;
            font-weight: bold;
        }

        /* HERO SECTION */
        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 50px;
            gap: 20px;
            padding: 0 50px;
        }

        .hero-text {
            max-width: 50%;
        }

        .hero-text h1 {
            font-size: 2.5em;
            color: #007bff;
            margin-bottom: 20px;
        }

        .hero-text p {
            font-size: 1.2em;
            margin-bottom: 20px;
        }

        .cta-button {
            padding: 12px 20px;
            font-size: 1em;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
        }

        /* FOOTER */
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9em;
            color: #666;
            padding: 20px;
        }

        /* Gambar lebih ke bawah */
        .hero-image {
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div class="header">
        <div class="logo">DIGICEK</div>
        <a href="#" class="contact">Kontak Kami</a>
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

    # Tombol untuk menuju ke halaman prediksi di Streamlit
    if st.button("Cek Sekarang"):
        st.switch_page("pages/Deteksi.py")  # Gantilah dengan halaman Streamlit Anda

with col2:
    st.markdown('<div class="hero-image">', unsafe_allow_html=True)
    st.image("image/ilustrasi.png", width=300)  # Gantilah dengan path gambar yang sesuai
    st.markdown('</div>', unsafe_allow_html=True)