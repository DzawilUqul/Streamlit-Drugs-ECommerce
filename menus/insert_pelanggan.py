import streamlit as st
import pandas as pd


def app(connection, cursor):
    st.title("Insert Pelanggan")
    with st.form("my_form"):
        # Nama Pelanggan
        nama_pelanggan = st.text_input("Nama Pelanggan : ")

        # Alamat
        alamat = st.text_input("Alamat : ")

        # No. Telp
        no_telp = st.text_input("No. Telp : ")

        # Submit
        submitted = st.form_submit_button("Insert")
        if submitted:
            # Cek input
            if not nama_pelanggan:
                st.warning("Harap masukkan nama pelanggan", icon="⚠️")
                return
            if not alamat:
                st.warning("Harap masukkan alamat", icon="⚠️")
                return
            if not no_telp:
                st.warning("Harap masukkan no. telp", icon="⚠️")
                return

            # Insert data
            try:
                cursor.callproc('spInsertCustomer', (nama_pelanggan, alamat, no_telp))
                connection.commit()
                st.success("Berhasil menambahkan pelanggan", icon="✅")
            except Exception as e:
                st.error("Gagal menambahkan pelanggan", e)