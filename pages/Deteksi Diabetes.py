import streamlit as st
import xgboost as xgb
import pandas as pd
import joblib

# Memuat model yang sudah dilatih
model = xgb.Booster(model_file="model_dan_data/kti_unmul_model_diabetes.json")
X_train = joblib.load("model_dan_data/train_data.pkl")

# UI Streamlit
st.set_page_config(page_title="DIGICEK", page_icon="", layout="wide")
st.title("Deteksi Diabetes")

# Membuat input form dengan beberapa kategori
with st.form(key="diabetes_form"):
    st.header("Informasi Pengguna")

    usia = st.number_input("Usia", min_value=1, max_value=100, value=20)
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
    pendidikan = st.selectbox("Pendidikan Terakhir", ["Tidak Sekolah", "SD", "SMP", "SMA", "Kuliah tidak lulus", "Sarjana"])
    berat_badan = st.number_input("Berat Badan (Kg)", min_value=1, max_value=200, value=60)
    tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=1, max_value=250, value=170)

    st.header("Kebiasaan Sehari-hari")
    aktivitas_fisik = st.selectbox("Aktivitas Fisik", ["Ya", "Tidak"])
    jalan_naik_turun_tangga = st.selectbox("Jalan Kaki atau Naik Turun Tangga", ["Ya", "Tidak"])
    buah = st.selectbox("Makan Buah-buahan", ["Ya", "Tidak"])
    sayur = st.selectbox("Makan Sayur-sayuran", ["Ya", "Tidak"])
    smoker = st.selectbox("Perokok Aktif", ["Tidak", "Ya"])
    alkohol = st.selectbox("Konsumsi Alkohol Berlebihan", ["Tidak", "Ya"])

    st.header("Kesehatan Tubuh")
    kesehatan = st.selectbox("Kesehatan secara Umum", ["Luar Biasa", "Sangat Bagus", "Bagus", "Cukup", "Jelek"])
    kesehatan_mental = st.number_input("Mental yang Sehat (Hari)", min_value=0, max_value=30, value=15)
    kesehatan_fisik = st.number_input("Fisik yang Sehat (Hari)", min_value=0, max_value=30, value=15)
    bp = st.selectbox("Tekanan Darah Tinggi", ["Tidak", "Ya"])
    kolesterol = st.selectbox("Kolesterol Tinggi", ["Tidak", "Ya"])
    HeartDiseaseorAttack = st.selectbox("Penyakit Jantung", ["Tidak", "Ya"])

    submit_button = st.form_submit_button("Prediksi")

# Fungsi prediksi
def make_prediction(inputs):
    df = pd.DataFrame([inputs], columns=[
        "HighBP", "HighChol", "BMI", "Smoker", "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education"
    ])
    pred_proba = model.predict(xgb.DMatrix(df, enable_categorical=True))
    return float(pred_proba[0])

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
        "GenHlth": kesehatan,
        "MentHlth": kesehatan_mental,
        "PhysHlth": kesehatan_fisik,
        "DiffWalk": 1 if jalan_naik_turun_tangga == "Ya" else 0,
        "Sex": 1 if jenis_kelamin == "Laki-laki" else 0,
        "Age": usia,
        "Education": pendidikan
    }

    proba_pos = make_prediction(inputs)
    st.subheader("Probabilitas:")
    st.write(f"Tidak menderita: {(1 - proba_pos) * 100:.2f}%")
    st.write(f"Menderita: {proba_pos * 100:.2f}%")

    saran = {}
    if aktivitas_fisik == "Tidak":
        saran["Aktivitas Fisik"] = "Lakukan aktivitas fisik."
    if buah == "Tidak":
        saran["Makan Buah-buahan"] = "Makanlah buah-buahan."
    if sayur == "Tidak":
        saran["Makan Sayur-sayuran"] = "Makanlah sayur-sayuran."
    if smoker == "Ya":
        saran["Perokok Aktif"] = "Kurangi dan hilangkan kebiasaan merokok."
    if alkohol == "Ya":
        saran["Konsumsi Alkohol Berlebihan"] = "Kurangi konsumsi alkohol berlebih."
    if bp == "Ya":
        saran["Tekanan Darah Tinggi"] = "Kurangi konsumsi garam, turunkan berat badan, makan sehat, dan rajin berolahraga."
    if kolesterol == "Ya":
        saran["Kolesterol Tinggi"] = "Hindari makanan yang digoreng, batasi makanan berlemak, dan olahraga teratur."
    if HeartDiseaseorAttack == "Ya":
        saran["Penyakit Jantung"] = "Olahraga rutin, berhenti merokok, dan makan makanan bergizi seimbang."

    if saran:
        st.subheader("Saran untuk Anda:")
        for kondisi, rekomendasi in saran.items():
            st.write(f"{kondisi}:** {rekomendasi}")
