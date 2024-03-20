import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

connection = mysql.connector.connect(
    host='localhost',
    database='penjualan_obat',
    user='root',
    password='')
cursor = connection.cursor()

cursor.execute(
    """
    SELECT id_obat AS 'ID Obat', nama_obat AS 'Nama Obat', harga AS 'Harga', 
    stok AS 'Stok', nama_jenis_obat AS 'Jenis Obat', CONCAT(persentase_diskon, '%') AS 'Diskon', 
    nama_satuan AS 'Nama Satuan' FROM obat
    JOIN jenis_obat ON obat.id_jenis_obat = jenis_obat.id_jenis_obat
    JOIN diskon ON obat.id_diskon = diskon.id_diskon
    JOIN satuan ON obat.id_satuan = satuan.id_satuan
    ORDER BY id_obat
    """
)
data = cursor.fetchall()

with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Data Obat", "Data Transaksi", "Insert Transaksi"],
        icons=["capsule", "receipt-cutoff", "plus-circle-fill"],
        default_index=0
    )

if selected == "Data Obat":
    st.title("Data Obat")
    st.write(pd.DataFrame(data, columns=cursor.column_names))
elif selected == "Data Transaksi":
    cursor.execute("SELECT * FROM transaksi")
    data = cursor.fetchall()
    st.title("Data Transaksi")
    st.write(pd.DataFrame(data, columns=cursor.column_names))
elif selected == "Insert Transaksi":
    st.title("Insert Transaksi")
    user_id = st.number_input(
        label="ID User : ",
        min_value=1,
        placeholder="ID User"
    )
    date = st.date_input("Tanggal : ")
    product_id = st.number_input(
        label="ID Produk : ",
        min_value=1
    )
    quantity = st.number_input(
        label="Jumlah : ",
        min_value=1
    )
    # button
    if st.button("Insert"):
        try:
            cursor.callproc('spInsertTransaction', [user_id, date, product_id, quantity])
            connection.commit()
            st.toast("Berhasil menambahkan transaksi", icon="✅")
        except mysql.connector.Error as err:
            st.toast("Gagal menambahkan transaksi. Err: " + str(err), icon="❌")