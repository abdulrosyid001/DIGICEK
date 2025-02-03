import streamlit as st
import xgboost as xgb
import pandas as pd
import joblib

# Memuat model yang sudah dilatih
model = xgb.Booster(model_file="model_dan_data\kti_unmul_model_diabetes.json")
X_train = joblib.load("model_dan_data/train_data.pkl")

# UI Streamlit
st.set_page_config(page_title="DIGICEK", page_icon="", layout="wide")

# CSS Kustom untuk Latar Belakang Putih
# st.markdown("""
#     <style>
#         body, .stApp {
#             background-color: white !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

st.title("Deteksi Gagal Ginjal dan Diabetes")

# # Deskripsi yang lebih menarik
# st.write(
#     "Isi formulir berikut untuk mengetahui kemungkinan seseorang mengidap narkolepsi."
#     " Data yang Anda masukkan akan digunakan untuk memberikan hasil prediksi yang akurat."
# )

# st.write(
#     "Narkolepsi adalah gangguan tidur neurologis yang menyebabkan kantuk berlebihan dan serangan tidur tiba-tiba. "
#     "Gejalanya meliputi katapleksi (kelemahan otot) dan halusinasi tidur. "
#     "Isi formulir berikut untuk mengetahui kemungkinan seseorang mengidap narkolepsi. "
#     "Data yang Anda masukkan akan digunakan untuk memberikan hasil prediksi yang akurat. "
#     "Jika Anda kurang paham tentang variabel yang dibutuhkan, Anda dapat mengklik tanda '?' untuk penjelasan lebih lanjut."
# )

# Membuat input form dengan beberapa kategori
with st.form(key="narkolepsi_form"):
    st.header("Informasi Pengguna")

    usia = st.number_input(
        "Usia",
        min_value=1,
        max_value=100,
        value=20,
        help="..."
    )

    jenis_kelamin = st.selectbox(
        "Jenis Kelamin",
        ["Perempuan", "Laki-laki"],
        help="..."
    )

    pendidikan = st.selectbox(
        "Pendidikan Terakhir",
        ["Tidak Sekolah", "Sekolah Dasar (SD)", "Sekolah Menengah Pertama (SMP)","Sekolah Menengah Atas (SMA)", "Kuliah tapi Tidak Lulus Sarjana","Sarjana"],
        help="..."
    )

    berat_badan = st.number_input(
        "Berat Badan (Kg)",
        min_value=1,
        max_value=200,
        value=60,
        help="..."
    )

    tinggi_badan = st.number_input(
        "Tinggi Badan (cm)",
        min_value=1,
        max_value=250,
        value=170,
        help="..."
    )

    st.header("Kebiasaan Sehari-hari")

    aktivitas_fisik = st.selectbox(
        "Aktivitas Fisik",
        ["Ya","Tidak"],
        help="..."
    )

    jalan_naik_turun_tangga = st.selectbox(
        "Jalan Kaki atau Naik Turun Tangga",
        ["Ya", "Tidak"],
        help="..."
    )

    buah = st.selectbox(
        "Makan Buah-buahan",
        ["Ya", "Tidak"],
        help="..."
    )

    sayur = st.selectbox(
        "Makan Sayur-sayuran",
        ["Ya", "Tidak"],
        help="..."
    )

    smoker = st.selectbox(
        "Perokok Aktif",
        ["Tidak", "Ya"],
        help="..."
    )

    alkohol = st.selectbox(
        "Konsumsi Alkohol Berlebihan",
        ["Tidak", "Ya"],
        help="..."
    )

    st.header("Kesehatan Tubuh")

    kesehatan = st.selectbox(
        "Kesehatan secara Umum",
        ["Luar Biasa", "Sangat Bagus","Bagus","Cukup","Jelek"],
        help="..."
    )

    kesehatan_mental = st.number_input(
        "Mental yang Sehat (Hari)",
        min_value=0,
        max_value=30,
        value=15,
        help="..."
    )

    kesehatan_fisik = st.number_input(
        "Fisik yang Sehat (Hari)",
        min_value=0,
        max_value=30,
        value=15,
        help="..."
    )

    bp = st.selectbox(
        "Tekanan Darah Tinggi",
        ["Tidak", "Ya"],
        help="..."
    )

    kolesterol = st.selectbox(
        "Kolesterol Tinggi",
        ["Tidak", "Ya"],
        help="..."
    )

    HeartDiseaseorAttack = st.selectbox(
        "Penyakit Jantung",
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
            "HighBP",
            "HighChol",
            "BMI",
            "Smoker",
            "HeartDiseaseorAttack",
            "PhysActivity",
            "Fruits",
            "Veggies",
            "HvyAlcoholConsump",
            "GenHlth",
            "MentHlth",
            "PhysHlth",
            "DiffWalk",
            "Sex",
            "Age",
            "Education"
        ],
    )

    # Menggunakan predict_proba() untuk mendapatkan probabilitas
    pred_proba = model.predict(xgb.DMatrix(df, enable_categorical=True))
    return float(pred_proba[0])  # Mengembalikan probabilitas untuk kelas 1 (narkolepsi)

# Fungsi untuk mengonversi usia ke kategori
def convert_age_to_category(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    elif age >= 80:
        return 13
    else:
        return None  # Jika usia tidak valid
    
def convert_to_category(kolom):
    if kolom == 'Tidak':
        return 0
    elif kolom == 'Ya':
        return 1
    
def convert_kesehatan_to_category(kolom):
    if kolom == 'Luar Biasa':
        return 1
    elif kolom == 'Sangat Bagus':
        return 2
    elif kolom == 'Bagus':
        return 3
    elif kolom == 'Cukup':
        return 4
    elif kolom == 'Jelek':
        return 5
    
def convert_sex_to_category(kolom):
    if kolom == 'Perempuan':
        return 0
    elif kolom == 'Laki-laki':
        return 1
    
def convert_education_to_category(kolom):
    if kolom == 'Tidak Sekolah':
        return 1
    elif kolom == 'Sekolah Dasar (SD)':
        return 2
    elif kolom == 'Sekolah Menengah Pertama (SMP)':
        return 3
    elif kolom == 'Sekolah Menengah Atas (SMA)':
        return 4
    elif kolom == 'Kuliah tapi Tidak Lulus Sarjana':
        return 5
    elif kolom == 'Sarjana':
        return 6

# Prediksi jika tombol ditekan
if submit_button:
    # Mengonversi usia numerik ke kategori
    age_category = convert_age_to_category(usia)

    highbp = convert_to_category(bp)
    highchol = convert_to_category(kolesterol)
    perokok = convert_to_category(smoker)
    jantung = convert_to_category(HeartDiseaseorAttack)
    PhysActivity = convert_to_category(aktivitas_fisik)
    Fruits = convert_to_category(buah)
    Veggies = convert_to_category(sayur)
    HvyAlcoholConsump = convert_to_category(alkohol)
    DiffWalk = convert_to_category(jalan_naik_turun_tangga)

    kesehatan = convert_kesehatan_to_category(kesehatan)

    sex = convert_sex_to_category(jenis_kelamin)

    edukasi = convert_education_to_category(pendidikan)

    bmi = berat_badan/(tinggi_badan^2)

    # Pastikan usia kategori valid sebelum prediksi
    if age_category is None:
        st.error("Usia tidak valid. Harap masukkan usia antara 18 hingga 100 tahun.")
    else:
        # Mengumpulkan data input dari form
        inputs = {
            "HighBP": highbp,
            "HighChol": highchol,
            "BMI": bmi,
            "Smoker": perokok,
            "HeartDiseaseorAttack": jantung,
            "PhysActivity": PhysActivity,
            "Fruits": Fruits,
            "Veggies": Veggies,
            "HvyAlcoholConsump": HvyAlcoholConsump,
            "GenHlth": kesehatan,
            "MentHlth": kesehatan_mental,
            "PhysHlth": kesehatan_fisik,
            "DiffWalk": DiffWalk,
            "Sex": sex,
            "Age": age_category,  # Gunakan kategori usia
            "Education": edukasi
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
            st.success("Anda kemungkinan besar menderita.")
        else:
            st.success("Anda kemungkinan besar tidak menderita.")