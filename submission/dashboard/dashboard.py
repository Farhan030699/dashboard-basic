# -*- coding: utf-8 -*-
"""Dashboard.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oq31Kr5eERTfpswFXbPUZjEW1crslYAY
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Judul aplikasi
st.set_page_config(page_title="Dashboard Air Quality in Guanyuan", page_icon=":bar_chart:")
st.title('DASHBOARD BASIC EDGE')
st.header('Air Quality in Guanyuan March2013 - Feb2017 :sparkles:')

# Tambahkan teks ke dashboard
st.write("Ini adalah dashboard sederhana yang dibuat menggunakan Streamlit Package.")

# Tambahkan dataframe Pandas ke dashboard
df = pd.read_csv(/dashboard/'Air_quality-guanyuan_2013-2017.csv', delimiter=',')
df.dropna(axis=0, inplace=True)
df['tanggal']=pd.to_datetime(df[['year','month','day','hour']])
df1=df.sort_values(['tanggal'])
df1['Di Bawah Nol'] = df1['TEMP'][df1['TEMP'] < 0]
df1['Di Atas Nol'] = df1['TEMP'][df1['TEMP'] >= 0]



# Tambahkan grafik
min_date = df1["tanggal"].min()
max_date = df1["tanggal"].max()

with st.sidebar:
    st.header("Waktu Kejadian")
    # Menambahkan logo perusahaan
    st.image("air.jpg")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    all_df = df1[(df1["tanggal"] >= str(start_date)) &
                (df1["tanggal"] <= str(end_date))]

# membuat grafik pertama
st.subheader('Grafik Temperatur di Guanyuan (Maret 2013 - Februari 2017)')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(all_df['tanggal'], all_df['Di Atas Nol'], linestyle='-',color='orange')
ax.plot(all_df['tanggal'], all_df['Di Bawah Nol'], linestyle='-', color='lightblue', label='Di Bawah Nol')

#mengatur format label sumbu x menjadi hanya tahun dan bulan
date_format= mdates.DateFormatter('%B %Y')
plt.gca().xaxis.set_major_formatter(date_format)

ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xlabel('TAHUN',fontsize=15)
plt.ylabel('Temperatur',fontsize=15)
plt.grid(True)
st.pyplot(fig)

#membuat grafik kedua
st.subheader('Grafik Curah Hujan di Guanyuan (Maret 2013 - Februari 2017)')
mean_value= all_df['RAIN'].mean()
#membuat plot
fig2, ax2 = plt.subplots(figsize=(16, 8))
ax2.plot(
    all_df['tanggal'],
    all_df['RAIN'],
    marker='o',
    linewidth=1,
    linestyle='-',
    color="#72BCD4"
)
#mengatur format label sumbu x menjadi hanya tahun dan bulan
date_format1= mdates.DateFormatter('%B %Y')
plt.gca().xaxis.set_major_formatter(date_format1)

ax2.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='x', labelsize=15)

plt.xlabel('TAHUN',fontsize=15)
plt.ylabel('Curah hujan',fontsize=15)
plt.grid(True)
#tambahkan garis rata - rata
ax2.axhline(mean_value, color='red',linestyle='--',label=f'Rata - rata:{mean_value:.2f}')
st.pyplot(fig2)
# Footer
st.markdown('---')  # Garis pemisah
st.write('Created with :heart: Farhan Rasyad Koswara')
st.caption('Copyright (c) Farhan 2023')
