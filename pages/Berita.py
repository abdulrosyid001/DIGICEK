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
        </style>
        """,
        unsafe_allow_html=True,
    )

custom_css()

# DATA BERITA
berita_data = [
    {"title": "IDAI Sebut Anak dengan Diabetes Lebih Rentan Terkena Gagal Ginjal, Ini Alasannya", "description": "Rabu, 27 November 2024","image":"image/gagal_ginjal.jpeg"},
    {"title": "Tren Penyakit Diabetes di Atas Usia 15 Tahun Meningkat, Pecinta Makanan Manis Penting Lakukan Ini", "description": "Kamis, 30 Januari 2025","image":"image/diabetes.webp"},
]

# CAROUSEL BERITA
st.title("Berita")

berita_cols = st.columns(len(berita_data))

for idx, berita in enumerate(berita_data):
    with berita_cols[idx]:
        st.image(berita["image"], width=300)
        st.markdown(f"**{berita['title']}**")
        st.write(berita["description"])
