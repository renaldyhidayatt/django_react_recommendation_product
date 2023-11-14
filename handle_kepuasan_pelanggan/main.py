import streamlit as st
import pandas as pd
import requests
import random
import matplotlib.pyplot as plt

url = 'https://t67y.egoq.lyr.id/api/dashboard'

response = requests.get(url)


st.title('Perhitungan Manfaat SIREKOM')


st.header('Peningkatan Konversi Penjualan')
st.write('Bandingkan jumlah penjualan sebelum dan setelah implementasi. Hitung persentase kenaikan penjualan.')

if response.status_code == 200:
    data = response.json()

   
    df_pendapatan = pd.DataFrame({
        'Bulan': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'Pendapatan': data["data"]["pendapatan"]
    })
   
 
    plt.figure(figsize=(10, 6))
    plt.plot(df_pendapatan['Bulan'], df_pendapatan['Pendapatan'])
    plt.xlabel('Bulan')
    plt.ylabel('Pendapatan')
    plt.title('Grafik Pendapatan')
    plt.xticks(rotation=45)
    plt.grid(True)

   
    st.pyplot(plt)
else:
    st.write(f"Failed to retrieve data. Status code: {response.status_code}")


df_kepuasan = pd.read_csv('./dataset/kepuasaan.csv')


st.header('Kepuasan Pengguna')
st.bar_chart(df_kepuasan.set_index('status_kepuasan')['persentase'])



st.header('Pertumbuhan Triwulan')
df_order = pd.read_csv('./dataset/modified_order.csv')

df_order['created_at'] = pd.to_datetime(df_order['created_at'])


df_order = df_order[
    (df_order['created_at'].dt.year == 2023) & 
    (df_order['created_at'].dt.quarter <= 4)  
]

transactions_per_quarter = df_order.groupby(df_order['created_at'].dt.to_period("Q")).size()


fig, ax = plt.subplots(figsize=(8, 6))
colors = ['skyblue', 'salmon', 'lightgreen', 'goldenrod']
quarters = ['Triwulan 1', 'Triwulan 2', 'Triwulan 3', 'Triwulan 4']
transactions_per_quarter.plot(kind='bar', color=colors, ax=ax)
ax.set_title('Jumlah Transaksi per Triwulan (Triwulan 1-4)')
ax.set_xlabel('Triwulan')
ax.set_ylabel('Persentase Pertumbuhan')
ax.set_xticks(range(len(quarters)))
ax.set_xticklabels(quarters, rotation=45)
ax.grid(axis='y')

st.pyplot(fig)



df_brand = pd.read_csv('./dataset/brand.csv')

grouped = df_brand.groupby('Brand Recognition')['Perubahan'].mean()

st.header('Peningkatan Branding Platform E-commerce')


fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(grouped.index, grouped.values)
ax.set_xlabel('Brand')
ax.set_ylabel('Rata-rata Perubahan')
ax.set_title('Peningkatan Branding Platform E-commerce')
ax.set_xticklabels(grouped.index, rotation=45)

st.pyplot(fig)



