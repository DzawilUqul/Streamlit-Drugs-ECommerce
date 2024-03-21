import streamlit as st
import pandas as pd
import mysql.connector

def app(connection, cursor):

    cursor.execute(
        """
        SELECT id_transaksi AS 'ID Transaksi', pelanggan.nama_pelanggan AS 'Pelanggan', tanggal AS 'Tanggal', total_harga AS 'Total Harga' FROM transaksi
        JOIN pelanggan ON transaksi.id_pelanggan = pelanggan.id_pelanggan
        ORDER BY id_transaksi
        """
    )
    data = cursor.fetchall()
    st.title("Data Transaksi")

    st.dataframe(pd.DataFrame(data, columns=cursor.column_names), hide_index=True)