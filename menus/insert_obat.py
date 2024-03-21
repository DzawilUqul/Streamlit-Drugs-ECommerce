import streamlit as st
import pandas as pd


def app(connection, cursor):
    st.title("Insert Obat")
    with st.form("my_form"):
        # Nama Obat
        nama_obat = st.text_input("Nama Obat : ")

        # Harga
        harga = st.number_input("Harga : ", min_value=0, step=1000)

        # Stok
        stok = st.number_input("Stok : ", min_value=0, step=1)

        # Jenis Obat
        cursor.execute(
            """
            SELECT id_jenis_obat, nama_jenis_obat FROM jenis_obat
            """
        )
        obat_list = cursor.fetchall()

        jenis_obat_dict = {option[1]: option[0] for option in obat_list}
        selected_pelanggan = st.selectbox(
            label="Obat",
            options=list(jenis_obat_dict.keys()),
            index=None,
            placeholder="Pilih jenis obat...",
        )

        # diskon
        cursor.execute(
            """
            SELECT id_diskon, persentase_diskon FROM diskon
            """
        )

        diskon_list = cursor.fetchall()

        diskon_dict = {option[1]: option[0] for option in diskon_list}
        diskon = st.selectbox(
            label="Diskon",
            options=list(diskon_dict.keys()),
            index=None,
            placeholder="Pilih diskon...",
        )

        # satuan
        cursor.execute(
            """
            SELECT id_satuan, nama_satuan FROM satuan
            """
        )

        satuan_list = cursor.fetchall()

        satuan_dict = {option[1]: option[0] for option in satuan_list}
        selected_satuan = st.selectbox(
            label="Satuan",
            options=list(satuan_dict.keys()),
            index=None,
            placeholder="Pilih satuan...",
        )

        # Submit
        submitted = st.form_submit_button("Insert")
        if submitted:
            if not nama_obat:
                st.warning("Harap masukkan nama obat", icon="⚠️")
                return
            if not harga:
                st.warning("Harap masukkan harga", icon="⚠️")
                return
            if not stok:
                st.warning("Harap masukkan stok", icon="⚠️")
                return
            if not selected_pelanggan:
                st.warning("Harap masukkan jenis obat", icon="⚠️")
                return
            if not diskon:
                st.warning("Harap masukkan diskon", icon="⚠️")
                return
            if not selected_satuan:
                st.warning("Harap masukkan satuan", icon="⚠️")
                return
            if selected_pelanggan:
                id_pelanggan = jenis_obat_dict[selected_pelanggan]
            if diskon:
                id_diskon = diskon_dict[diskon]
            if selected_satuan:
                id_satuan = satuan_dict[selected_satuan]

            # Insert data
            try:
                cursor.callproc('spInsertProduct', [nama_obat, harga, stok, id_pelanggan,
                                id_diskon, id_satuan])
                connection.commit()
                st.success("Berhasil menambahkan obat", icon="✅")
            except Exception as e:
                st.error("Gagal menambahkan obat", e)
