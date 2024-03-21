import streamlit as st
import pandas as pd

def app(connection, cursor):
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

    st.title("Data Obat")
    st.dataframe(pd.DataFrame(data, columns=cursor.column_names), hide_index=True, use_container_width=True, height=500)