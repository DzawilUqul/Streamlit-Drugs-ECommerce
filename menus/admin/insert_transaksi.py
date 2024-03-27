import streamlit as st
import pandas as pd
import mysql.connector

def app(connection, cursor):
    st.title("Insert Transaksi")

    # Ambil semua pelanggan
    cursor.execute(
        """
        SELECT id_pelanggan, nama_pelanggan FROM user
        """
    )
    pelanggan = cursor.fetchall()
    
    # Ambil semua obat
    cursor.execute(
        """
        SELECT id_obat, nama_obat FROM obat
        """
    )
    obat = cursor.fetchall()
    

    with st.form("my_form"):
        # Pelanggan
        pelanggan_dict = {option[1]: option[0] for option in pelanggan}
        selected_pelanggan = st.selectbox(
            label="Pelanggan",
            options=list(pelanggan_dict.keys()),
            index=None,
            placeholder="Pilih pelanggan...",
        )

        # Tanggal
        date = st.date_input("Tanggal : ")

        # Produk
        obat_dict = {option[1]: option[0] for option in obat}
        selected_obat = st.selectbox(
            label="Obat",
            options=list(obat_dict.keys()),
            index=None,
            placeholder="Pilih obat...",
        )

        # Jumlah
        quantity = st.number_input(
            label="Jumlah : ",
            min_value=1
        )

        # Submit
        submitted = st.form_submit_button("Insert")
        if submitted:
            # Cek input
            if selected_pelanggan:
                user_id = pelanggan_dict[selected_pelanggan]
            else:
                st.warning("Harap masukkan pelanggan", icon="⚠️")
                return
            
            if selected_obat:
                product_id = obat_dict[selected_obat]
            else:
                st.warning("Harap masukkan obat", icon="⚠️")
                return

            # Insert ke database
            try:
                cursor.callproc('spInsertTransaction', [user_id, date, product_id, quantity])
                connection.commit()
                st.success("Berhasil menambahkan transaksi", icon="✅")
                
            except mysql.connector.Error as err:
                st.error("Gagal menambahkan transaksi. Err: " + str(err), icon="❌")