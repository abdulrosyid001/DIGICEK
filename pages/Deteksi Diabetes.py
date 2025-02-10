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
model = xgb.Booster(model_file="model_dan_data/kti_unmul_model_diabetes.json")
X_train = joblib.load("model_dan_data/train_data.pkl")

st.title("Deteksi Diabetes")

# Membuat input form dengan beberapa kategori
with st.form(key="diabetes_form"):
    st.header("Informasi Pengguna")

    usia = st.number_input("Usia", min_value=1, max_value=100, value=20, help = "Berapa usia Anda saat ini  (dalam tahun)?")
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"], help = "Apakah jenis kelamin Anda?")
    pendidikan = st.selectbox("Pendidikan Terakhir", ["Tidak Sekolah", "SD", "SMP", "SMA", "Kuliah tidak lulus", "Sarjana"], help = "Apakah pendidikan terakhir yang Anda tempuh?")
    berat_badan = st.number_input("Berat Badan (Kg)", min_value=1, max_value=200, value=60, help= "Berapa berat badan Anda saat ini (dalam kg)?")
    tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=1, max_value=250, value=170,help = "Berapa tinggi badan Anda saat ini (dalam cm)?")

    st.header("Kebiasaan Sehari-hari")
    aktivitas_fisik = st.selectbox("Aktivitas Fisik", ["Ya", "Tidak"], help = "Apakah Anda melakukan aktivitas fisik atau olahraga dalam 30 hari terakhir di luar pekerjaan utama?")
    jalan_naik_turun_tangga = st.selectbox("Kesusahan saat Jalan Kaki atau Naik Turun Tangga", ["Ya", "Tidak"], help = "Apakah Anda kesusahan untuk berjalan kaki maupun naik turun tangga?")
    buah = st.selectbox("Makan Buah-buahan", ["Ya", "Tidak"],help = "Apakah Anda mengonsumsi buah sekali atau lebih dalam sehari?")
    sayur = st.selectbox("Makan Sayur-sayuran", ["Ya", "Tidak"],help = "Apakah Anda mengonsumsi sayuran sekali atau lebih dalam sehari?")
    smoker = st.selectbox("Perokok Aktif", ["Tidak", "Ya"], help = "Apakah Anda pernah merokok paling tidak sebanyak 100 batang rokok dalam hidup Anda?")
    alkohol = st.selectbox("Konsumsi Alkohol Berlebihan", ["Tidak", "Ya"], help = "Anda dikatakan mengonsumsi alkohol secara berlebihan jika Anda adalah orang dewasa laki-laki yang mengonsumsi lebih dari 14 kali dalam seminggu atau orang dewasa perempuan yang mengonsumsi lebih dari 7 kali dalam seminggu.")

    st.header("Kesehatan Tubuh")
    kesehatan = st.selectbox("Kesehatan secara Umum", ["Luar Biasa", "Sangat Bagus", "Bagus", "Cukup", "Jelek"], help = "Bagaimana Anda mengatakan kesehatan Anda secara umum?")
    kesehatan_mental = st.number_input("Mental yang Buruk (Hari)", min_value=0, max_value=30, value=15,help = "Berapa hari dalam sebulan Anda mengalami stress, depresi, dan masalah dengan emosi?")
    kesehatan_fisik = st.number_input("Fisik yang Tidak Sehat (Hari)", min_value=0, max_value=30, value=15,help = "Berapa hari dalam sebulan Anda mengalami sakit fisik dan cedera?")
    bp = st.selectbox("Tekanan Darah Tinggi", ["Tidak", "Ya"],help = "Apakah Anda mengalami tekanan darah tinggi?")
    kolesterol = st.selectbox("Kolesterol Tinggi", ["Tidak", "Ya"],help = "Apakah Anda mengalami kolesterol tinggi?")
    HeartDiseaseorAttack = st.selectbox("Penyakit Jantung", ["Tidak", "Ya"], help = "Apakah Anda mengalamai sakit jantung atau serangan jantung?")

    submit_button = st.form_submit_button("Prediksi")

# Fungsi prediksi
def make_prediction(inputs):
    df = pd.DataFrame([inputs], columns=[
        "HighBP", "HighChol", "BMI", "Smoker", "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education"
    ])
    pred_proba = model.predict(xgb.DMatrix(df, enable_categorical=True))
    return float(pred_proba[0])

# Fungsi konversi kategori
def convert_to_category(value, mapping):
    return mapping.get(value, None)

age_mapping = {"18-24": 1, "25-29": 2, "30-34": 3, "35-39": 4, "40-44": 5, "45-49": 6, "50-54": 7, "55-59": 8, "60-64": 9, "65-69": 10, "70-74": 11, "75-79": 12, "80+": 13}
kesehatan_mapping = {"Luar Biasa": 1, "Sangat Bagus": 2, "Bagus": 3, "Cukup": 4, "Jelek": 5}
edukasi_mapping = {"Tidak Sekolah": 1, "SD": 2, "SMP": 3, "SMA": 4, "Kuliah tidak lulus": 5, "Sarjana": 6}

if submit_button:
    bmi = berat_badan / ((tinggi_badan / 100) ** 2)
    inputs = {
        "HighBP": 1 if bp == "Ya" else 0,
        "HighChol": 1 if kolesterol == "Ya" else 0,
        "BMI": bmi,
        "Smoker": 1 if smoker == "Ya" else 0,
        "HeartDiseaseorAttack": 1 if HeartDiseaseorAttack == "Ya" else 0,
        "PhysActivity": 1 if aktivitas_fisik == "Ya" else 0,
        "Fruits": 1 if buah == "Ya" else 0,
        "Veggies": 1 if sayur == "Ya" else 0,
        "HvyAlcoholConsump": 1 if alkohol == "Ya" else 0,
        "GenHlth": convert_to_category(kesehatan, kesehatan_mapping),
        "MentHlth": kesehatan_mental,
        "PhysHlth": kesehatan_fisik,
        "DiffWalk": 1 if jalan_naik_turun_tangga == "Ya" else 0,
        "Sex": 1 if jenis_kelamin == "Laki-laki" else 0,
        "Age": usia,
        "Education": convert_to_category(pendidikan, edukasi_mapping)
    }

    proba_pos = make_prediction(inputs)
    proba_pos_percentage = proba_pos * 100
    proba_neg_percentage = (1 - proba_pos) * 100

    st.subheader("Probabilitas:")
    st.markdown(f"Tidak menderita: {proba_neg_percentage:.2f}%")
    st.markdown(f"Menderita: {proba_pos_percentage:.2f}%")

    if proba_pos > 0.5:
        st.success("Anda kemungkinan besar menderita diabetes.")
    else:
        st.success("Anda kemungkinan besar tidak menderita diabetes.")

    # Menampilkan saran berdasarkan input
    saran = []
    if aktivitas_fisik == "Tidak":
        saran.append("Tidak aktivitas fisik : Lakukan aktivitas fisik scara rutin.")
    if buah == "Tidak":
        saran.append("Tidak makan buah : Makanlah buah-buahan.")
    if sayur == "Tidak":
        saran.append("Tidak makan sayur : Makanlah sayur-sayuran.")
    if smoker == "Ya":
        saran.append("Merokok : Kurangi dan hilangkan kebiasaan merokok.")
    if alkohol == "Ya":
        saran.append("Alkohol berlebih: Kurangi dan hilangkan konsumsi alkohol berlebih.")
    if bp == "Ya":
        saran.append("Tekanan darah tinggi: Kurangi konsumsi garam, turunkan berat badan, makan sehat, dan olahraga teratur.")
    if kolesterol == "Ya":
        saran.append("Kolestrol tinggi : Hindari makanan yang digoreng, batasi makanan berlemak, dan olahraga teratur.")
    if HeartDiseaseorAttack == "Ya":
        saran.append("Penyakit Jantung: Periksa Kedokter, olahraga teratur, berhenti merokok, dan makan-makanan bergizi seimbang.")

    if saran:
        st.subheader("Saran untuk Anda:")
        for s in saran:
            st.write(f"- {s}")
