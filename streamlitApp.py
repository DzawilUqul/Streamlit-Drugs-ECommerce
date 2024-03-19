import streamlit as st
import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host='localhost',
    database='penjualan_obat',
    user='root',
    password='')
cursor = connection.cursor()

cursor.execute("SELECT * FROM obat")
data = cursor.fetchall()

st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu", ["Data Obat", "Data Transaksi", "Insert Transaksi"])

if menu == "Data Obat":
    st.title("Data Obat")
    st.write(pd.DataFrame(data, columns=cursor.column_names))
elif menu == "Data Transaksi":
    cursor.execute("SELECT * FROM transaksi")
    data = cursor.fetchall()
    st.title("Data Transaksi")
    st.write(pd.DataFrame(data, columns=cursor.column_names))
elif menu == "Insert Transaksi":
    st.title("Insert Transaksi")
    user_id = st.number_input("id User : ")
    date = st.date_input("Tanggal : ")
    product_id = st.number_input("id Produk : ")
    quantity = st.number_input("Jumlah : ")
    # button
    if st.button("Insert"):
        cursor.callproc('spInsertTransaction', [user_id, date, product_id, quantity])
        for result in cursor.stored_results():
            st.write(result.fetchall())
        # cursor.close()
