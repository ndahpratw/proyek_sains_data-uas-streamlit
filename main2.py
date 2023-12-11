import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

st.markdown(
    "<h1 style='text-align: center;'>Klasifikasi Diabetes Menggunakan Model Support Vector Machine</h1>", unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center;'>Indah Pratiwi | 210411100050 | PSD - B</h4>", unsafe_allow_html=True
)

# st.info("Data latih diperoleh dari situs UCI Machine Learning dan dapat diakses pada link berikut : https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators ")

with open('model_svm.pkl', 'rb') as file_model:
    model_svm = pickle.load(file_model)

st.warning("Tekan 0 untuk 'tidak' dan 1 untuk 'ya'")

HighBP = st.radio("Apakah tekanan darah anda tinggi?", ["none", "0", "1"])
BMI = st.number_input ('Input Body Mass Index anda. Anda bisa menghitung BMI melalui url berikut : https://www.halodoc.com/bmi-calculator/')
st.warning("Tekan 1 untuk 'excellent', 2 untuk 'very good', 3 untuk 'good', 4 untuk 'pair' dan 5 untuk 'poor'")
GenHlth = st.radio("Bagaimana kondisi kesehatan anda menurut anda?", ["none", "1", "2", "3", "4", "5"])
umur = st.number_input ('Input umur anda.')


if st.button('Cek Status'):
    if HighBP != "none" and BMI is not None and GenHlth != "none" and umur is not None:
        
        # # Konversi input yang diterima menjadi tipe data numerik
        # HighBP = int(HighBP)
        # GenHlth = int(GenHlth)

        data = {
            'HighBP': [HighBP],
            'BMI': [BMI],
            'GenHlth': [GenHlth],
            'umur': [umur]
        }

        df = pd.DataFrame(data)
        
        # Prediksi berdasarkan input yang telah diubah menjadi numerik
        prediksi = model_svm.predict(df)
        if prediksi[0] == 0.0:
            st.success("Anda diprediksi tidak diabetese !")
        elif prediksi[0] == 1.0:
            st.warning("Anda diprediksi prediabetes !")
        else:
            st.error("Anda diprediksi diabetese !")
    else:
        st.text('Data tidak boleh kosong. Harap isi semua kolom.')
