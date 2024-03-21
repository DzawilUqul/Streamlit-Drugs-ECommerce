import streamlit as st
import pandas as pd


def app(connection, cursor):
    cursor.execute(
        """
        SELECT id_pelanggan AS 'ID Pelanggan', nama_pelanggan AS 'Nama Pelanggan', alamat AS 'Alamat', no_telepon AS 'No. Telp' FROM pelanggan
        """
    )
    data = cursor.fetchall()

    st.title("Data Pelanggan")
    st.write(pd.DataFrame(data, columns=cursor.column_names))
