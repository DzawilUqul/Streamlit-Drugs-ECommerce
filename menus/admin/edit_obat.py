import streamlit as st
import pandas as pd


def id_to_name():
    st.session_state.id_obat = st.session_state.nama_obat


def app(connection, cursor):
    st.title("Edit Obat")

    cursor.execute(
        """
        SELECT id_obat, nama_obat, harga, stok FROM obat
        """
    )

    obat = cursor.fetchall()

    with st.form("drugs_edit_form"):
        # obat_id
        cursor.execute(
            """
            SELECT id_obat, nama_obat FROM obat
            """
        )

        obat_list = cursor.fetchall()

        obat_dict = {option[1]: option[0] for option in obat_list}
        selected_id_obat = st.selectbox(
            label="Id_Obat",
            options=obat_dict,
            index=None,
            placeholder="Edit Id Obat...",
            disabled=False
        )
        # st.session_state.id_obat = selected_id_obat[:2]
        # nama_obat_disabled = st.text_input("Nama Obat", key="nama_obat_disabled", on_change=id_to_name)
        nama_obat_renamed = st.text_input("Rename Obat", key="nama_obat")
        harga = st.number_input("Harga", min_value=0, step=1000, key="harga")
        stok = st.number_input("Stok", min_value=0, step=1, key="stok")

        # id_jenis_obat_id
        cursor.execute(
            """
            SELECT id_jenis_obat, nama_jenis_obat FROM jenis_obat
            """
        )
        jenis_obat_list = cursor.fetchall()
        jenis_obat_dict = {option[1]: option[0] for option in jenis_obat_list}
        selected_jenis_obat = st.selectbox(
            label="Jenis Obat",
            options=jenis_obat_dict,
            index=None,
            placeholder="Edit jenis obat...",
            key="jenis_obat"
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
            placeholder="Edit satuan...",
        )

        # Submit
        submitted = st.form_submit_button("Update")
        if submitted:
            if not nama_obat_renamed:
                st.error("Nama obat tidak boleh kosong")
                return
            if not harga:
                st.error("Harga tidak boleh kosong")
                return
            if not stok:
                st.error("Stok tidak boleh kosong")
                return
            if not selected_jenis_obat:
                st.error("Jenis obat tidak boleh kosong")
                return
            if not diskon:
                st.error("Diskon tidak boleh kosong")
                return
            if not selected_satuan:
                st.error("Satuan tidak boleh kosong")
                return

            if selected_id_obat:
                selected_id_obat = obat_dict[selected_id_obat]
                print(selected_id_obat)
            if diskon:
                diskon = diskon_dict[diskon]
            if selected_satuan:
                selected_satuan = satuan_dict[selected_satuan]
            if selected_jenis_obat:
                selected_jenis_obat = jenis_obat_dict[selected_jenis_obat]

            # Insert data
            try:
                cursor.callproc('spUpdateProduct',
                                [selected_id_obat, nama_obat_renamed, harga, stok, selected_jenis_obat, diskon,
                                 selected_satuan])
                connection.commit()
                st.success("Berhasil mengedit obat", icon="✅")
            except Exception as e:
                st.error("Gagal mengedit obat", e)
