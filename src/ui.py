import streamlit as st
import requests

# Judul aplikasi
st.title('Obesity Prediction System')
st.write('Masukkan data untuk prediksi tingkat obesitas:')

# Input data dari pengguna
age = st.number_input('Age', min_value=14, max_value=61, step=1)
height = st.number_input('Height (in meters)', min_value=1.0, max_value=2.5, step=0.01)
weight = st.number_input('Weight (in kg)', min_value=30.0, max_value=200.0, step=1.0)
gender = st.selectbox('Gender', ['Male', 'Female'])
family_history = st.selectbox('Family History of Obesity', ['Yes', 'No'])
favc = st.selectbox('Frequent Consumption of High Calorie Food (FAVC)', ['Yes', 'No'])
fcvc = st.slider('Frequency of Vegetable Consumption (FCVC)', min_value=1.0, max_value=3.0, step=0.1)
ncp = st.slider('Number of Main Meals (NCP)', min_value=1.0, max_value=4.0, step=0.1)
caec = st.selectbox('Consumption of Food Between Meals (CAEC)', ['Always', 'Frequently', 'Sometimes', 'No'])
smoke = st.selectbox('Smoke', ['Yes', 'No'])
ch2o = st.slider('Daily Water Intake (CH2O)', min_value=1.0, max_value=3.0, step=0.1)
scc = st.selectbox('Monitor Calories Consumption (SCC)', ['Yes', 'No'])
faf = st.slider('Physical Activity Frequency (FAF)', min_value=0, max_value=3, step=1)
tue = st.slider('Time Using Technology (TUE)', min_value=0, max_value=2, step=1)
calc = st.selectbox('Consumption of Alcohol (CALC)', ['Always', 'Frequently', 'Sometimes', 'No'])
mtrans = st.selectbox(
    'Mode of Transportation (MTRANS)',
    ['Public_Transportation', 'Walking', 'Private', 'Bike', 'Motorbike']
)

# Konversi input kategori ke angka sesuai dengan preprocessing
categorical_mapping = {
    'Yes': 1,
    'No': 0,
    'Male': 1,
    'Female': 0,
    'Always': 0,
    'Frequently': 1,
    'Sometimes': 2,
    'No': 3,
    'Public_Transportation': 0,
    'Walking': 1,
    'Private': 2,
    'Bike': 3,
    'Motorbike': 4
}

# Data dalam bentuk array
features = [
    age,
    height,
    weight,
    categorical_mapping[gender],
    categorical_mapping[family_history],
    categorical_mapping[favc],
    fcvc,
    ncp,
    categorical_mapping[caec],
    categorical_mapping[smoke],
    ch2o,
    categorical_mapping[scc],
    faf,
    tue,
    categorical_mapping[calc],
    categorical_mapping[mtrans]
]

# Tombol untuk prediksi
if st.button('Predict'):
    # Kirim data ke API
    response = requests.post(
        'http://127.0.0.1:8000/predict',
        json={'features': features}
    )

    if response.status_code == 200:
        prediction = response.json().get('prediction', 'Error')
        st.write(f'Hasil Prediksi Tingkat Obesitas: {prediction}')
    else:
        st.write('Terjadi kesalahan pada prediksi. Mohon cek kembali input atau API.')

