import streamlit as st

# Custom CSS untuk styling
def custom_css():
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: white;
            }
            .top-bar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 30px;
                background-color: #FEA33A;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            .logo-header {
                width: 40px;
                margin-right: 10px;
            }
            .logo {
                font-size: 1.5em;
                font-weight: bold;
                color: black;
            }
            .menu a {
                margin: 0 10px;
                font-size: 16px;
                text-decoration: none;
                color: black;
            }
            .menu a:hover {
                text-decoration: underline;
            }
            .footer {
                text-align: center;
                padding: 10px;
                background-color: #FEA33A;
                color: white;
            }
            .socials a {
                color: black;
                text-decoration: none;
                font-size: 14px;
                margin: 0 10px;
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
        """,
        unsafe_allow_html=True,
    )

custom_css()

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

# DATA BERITA dengan URL
berita_data = [
    {"title": "IDAI Sebut Anak dengan Diabetes Lebih Rentan Terkena Gagal Ginjal, Ini Alasannya", 
     "description": "Rabu, 27 November 2024",
     "image": "image/gagal_ginjal.jpeg",
     "url": "https://health.detik.com/berita-detikhealth/d-7657862/idai-sebut-anak-dengan-diabetes-lebih-rentan-terkena-gagal-ginjal-ini-alasannya#:~:text=Ikatan%20Dokter%20Anak%20Indonesia%20(IDAI,dalam%20batas%20normal%20terbilang%20buruk."},

    {"title": "Tren Penyakit Diabetes di Atas Usia 15 Tahun Meningkat, Pecinta Makanan Manis Penting Lakukan Ini", 
     "description": "Kamis, 30 Januari 2025",
     "image": "image/diabetes.webp",
     "url": "https://mediaindonesia.com/humaniora/739296/tren-penyakit-diabetes-di-atas-usia-15-tahun-meningkat-pecinta-makanan--manis-penting-lakukan-ini"},
]

st.title("Berita")

berita_cols = st.columns(len(berita_data))

for idx, berita in enumerate(berita_data):
    with berita_cols[idx]:
        st.image(berita["image"], width=300)
        st.markdown(f"**{berita['title']}**")
        st.write(berita["description"])
        st.link_button("Baca Selengkapnya", berita["url"])
