import streamlit as st
import pandas as pd
import mysql.connector

def app(connection, cursor):
    st.title("Edit Profile")

    cursor.execute(
        """
        SELECT * FROM user WHERE id_pelanggan = %s
        """,
        (st.session_state.user_data["id"],)
    )
    user_data = cursor.fetchone()

    with st.form("edit_profile_form"):
        nama = st.text_input("Nama", value=user_data[1])
        no_telp = st.text_input("No. Telp", value=user_data[2])
        alamat = st.text_area("Alamat", value=user_data[3])

        if st.form_submit_button("Update"):
            try:
                cursor.callproc('spUpdatePelanggan', [st.session_state.user_data["id"], nama, no_telp, alamat])
                connection.commit()
                st.success("✅ Berhasil mengedit profile")
            except mysql.connector.Error as err:
                st.error("❌ Gagal mengedit. Err: " + str(err))
