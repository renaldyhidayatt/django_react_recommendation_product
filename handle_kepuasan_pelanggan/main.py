import streamlit as st
import pandas as pd
import requests
import random
import matplotlib.pyplot as plt

url = 'https://t67y.egoq.lyr.id/api/dashboard'

response = requests.get(url)


st.title('Perhitungan Manfaat SIREKOM')


st.header('Grafik Pendapatan per Bulan')
st.write("Grafik ini menunjukkan total pendapatan per bulan dari data penjualan yang telah diolah.")


df_order = pd.read_csv('./dataset/modified_order.csv')


df_order['created_at'] = pd.to_datetime(df_order['created_at'])


df_monthly_sales = df_order.groupby(df_order['created_at'].dt.strftime('%B')).agg({'totalPrice': 'sum'}).reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_monthly_sales['created_at'], df_monthly_sales['totalPrice'], marker='o', linestyle='-')
plt.xlabel('Bulan')
plt.ylabel('Pendapatan')
plt.title('Grafik Pendapatan per Bulan')
plt.xticks(rotation=45)
plt.grid(True)

st.pyplot(plt)



df_kepuasan = pd.read_csv('./dataset/kepuasaan.csv')


st.header('Kepuasan Pengguna')
st.write("Diagram batang ini memvisualisasikan tingkat kepuasan pengguna dari dataset kepuasaan yang telah tersedia.")

st.bar_chart(df_kepuasan.set_index('status_kepuasan')['persentase'])



st.header('Pertumbuhan Triwulan')
st.write("Grafik batang ini memperlihatkan jumlah transaksi per triwulan (Triwulan 1-4) dari data penjualan.")

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



df_orderitems = pd.read_csv('./dataset/OrderItems_with_brand.csv')


fig, axs = plt.subplots(2, 1, figsize=(10, 12))

axs[0].bar(df_orderitems['brand'].value_counts().index, df_orderitems['brand'].value_counts())
axs[0].set_xlabel('Brand')
axs[0].set_ylabel('Jumlah Produk Terjual')
axs[0].set_title('Jumlah Produk terjual per Brand')
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(True)


axs[1].pie(df_orderitems['brand'].value_counts(), labels=df_orderitems['brand'].value_counts().index, autopct='%1.1f%%')
axs[1].set_title('Pie Chart Distribusi Brand')

plt.tight_layout()

st.header('Visualisasi Jumlah Produk terjual per Brand')
st.write("Grafik batang dan pie chart ini menunjukkan jumlah produk yang terjual per brand dari dataset OrderItems.")
st.pyplot(fig)




