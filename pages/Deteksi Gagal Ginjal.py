import streamlit as st
import xgboost as xgb
import pandas as pd
import joblib

# UI Streamlit
st.set_page_config(page_title="DIGICEK", page_icon="", layout="wide")

# Custom CSS untuk styling
st.markdown("""
    <style>
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

# Memuat model yang sudah dilatih
model = xgb.Booster(model_file="model_dan_data/kti_unmul_model_gagal_ginjal.json")
X_train = joblib.load("model_dan_data/gagal_ginjal.pkl")

st.title("Deteksi Gagal Ginjal")

# Membuat input form dengan beberapa kategori
with st.form(key="gagal_ginjal_form"):
    st.header("Informasi Pengguna")

    usia = st.number_input(
        "Usia",
        min_value=2,
        max_value=90,
        value=20,
        help="..."
    )

    hemoglobin = st.number_input(
        "Hemoglobin",
        min_value=3,
        max_value=18,
        value=15,
        help="..."
    )

    tekanan_darah = st.number_input(
        "Tekanan Darah",
        min_value=50,
        max_value=180,
        value=90,
        help="..."
    )

    gula_darah_acak = st.number_input(
        "Gula Darah Acak",
        min_value=20,
        max_value=500,
        value=150,
        help="..."
    )

    hipertensi = st.selectbox(
        "Hipertensi",
        ["Tidak", "Ya"],
        help="..."
    )

    pedal_edema = st.selectbox(
        "Pedal Edema",
        ["Tidak", "Ya"],
        help="..."
    )

    submit_button = st.form_submit_button("Prediksi")

# Fungsi prediksi
def make_prediction(inputs):
    # Membuat dataframe untuk inputan pengguna
    df = pd.DataFrame(
        [inputs],
        columns=[
            "hemo",
            "htn",
            "age",
            "bp",
            "pe",
            "bgr"
        ],
    )

    # Menggunakan predict_proba() untuk mendapatkan probabilitas
    pred_proba = model.predict(xgb.DMatrix(df, enable_categorical=True))
    return float(pred_proba[0])  # Mengembalikan probabilitas untuk kelas 1 (narkolepsi)
    
def convert_to_category(kolom):
    if kolom == 'Tidak':
        return 0
    elif kolom == 'Ya':
        return 1

# Prediksi jika tombol ditekan
if submit_button:
    hipertensi = convert_to_category(hipertensi)
    pedal_edema = convert_to_category(pedal_edema)

    # Mengumpulkan data input dari form
    inputs = {
        "hemo": hemoglobin,
        "htn": hipertensi,
        "age": usia,
        "bp": tekanan_darah,
        "pe": pedal_edema,
        "bgr": gula_darah_acak,
    }

    proba_pos = make_prediction(inputs)

    # Menampilkan hasil probabilitas dengan format persentase
    proba_pos_percentage = proba_pos * 100
    proba_neg_percentage = (1 - proba_pos) * 100

    st.subheader(f"Probabilitas:")
    st.markdown(f"**Tidak menderita:** {proba_neg_percentage:.2f}%")
    st.markdown(f"**Menderita:** {proba_pos_percentage:.2f}%")

    # Memberikan hasil prediksi berdasarkan probabilitas
    if proba_pos > 0.5:
        st.success("Anda kemungkinan besar menderita gagal ginjal.")
    else:
        st.success("Anda kemungkinan besar tidak menderita gagal ginjal.")
