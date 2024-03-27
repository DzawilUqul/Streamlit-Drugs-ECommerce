import streamlit as st


def app(connection, cursor):
    st.title("Insert Jenis Obat")
    with st.form("my_form"):
        # Nama Obat
        nama_jenis_obat = st.text_input("Nama Jenis Obat : ")

        # Submit
        submitted = st.form_submit_button("Insert")
        if submitted:
            if not nama_jenis_obat:
                st.warning("Harap isi nama jenis obat", icon="⚠️")
                return
            if nama_jenis_obat:
                jenis_obat = [nama_jenis_obat]

            # Insert data
            try:
                cursor.callproc('spInsertJenisObat', jenis_obat)
                connection.commit()
                st.success("Berhasil menambahkan jenis obat", icon="✅")
            except Exception as e:
                st.error("Gagal menambahkan jenis obat", e)
