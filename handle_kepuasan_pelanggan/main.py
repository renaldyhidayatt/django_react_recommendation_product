import streamlit as st
import pandas as pd
import requests
import random

url = 'https://t67y.egoq.lyr.id/api/dashboard'

response = requests.get(url)


st.title('Perhitungan Manfaat SIREKOM')


st.header('Peningkatan Konversi Penjualan')
st.write('Bandingkan jumlah penjualan sebelum dan setelah implementasi. Hitung persentase kenaikan penjualan.')

if response.status_code == 200:
    data = response.json()

   
    df_pendapatan = pd.DataFrame({
        'Bulan': pd.date_range(start='2023-11-01', periods=12, freq='M'),
        'Pendapatan': data["data"]["pendapatan"]
    })
   
    st.line_chart(df_pendapatan.set_index('Bulan'))
else:
    st.write(f"Failed to retrieve data. Status code: {response.status_code}")


df_kepuasan = pd.read_csv('./dataset/kepuasaan.csv')


st.header('Kepuasan Pengguna')
st.bar_chart(df_kepuasan.set_index('status_kepuasan')['persentase'])


# Pendapatan Tambahan
st.header('Pendapatan Tambahan')
st.write('Total Pendapatan Tambahan:', data["data"]["totalPendapatan"])



data_pertumbuhan = {
    'Triwulan': [],
    'Persentase Pertumbuhan': []
}


for triwulan in range(1, 5):
    for _ in range(40):
        data_pertumbuhan['Triwulan'].append(f'Triwulan {triwulan}')
        data_pertumbuhan['Persentase Pertumbuhan'].append(random.randint(10 + (triwulan - 1) * 5, 10 + triwulan * 5))

df_pertumbuhan = pd.DataFrame(data_pertumbuhan)


st.header('Pertumbuhan Industri E-commerce')
st.bar_chart(df_pertumbuhan.set_index('Periode'))



df_brand = pd.read_csv('./dataset/brand.csv')

st.header('Peningkatan Branding Platform E-commerce')
st.bar_chart(df_brand.set_index('Brand Recognition'))