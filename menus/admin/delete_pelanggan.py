import streamlit as st


def app(connection, cursor):
    st.title("Delete User")

    cursor.execute(
        """
        SELECT id_pelanggan, nama_pelanggan, no_telepon, alamat, user_role, username, password FROM user
        """
    )

    user = cursor.fetchall()

    with st.form("delete_user_form"):
        # obat_id
        cursor.execute(
            """
            SELECT id_pelanggan, nama_pelanggan FROM user
            """
        )

        user_list = cursor.fetchall()

        user_dict = {option[0]: option[1] for option in user_list}
        selected_id_user = st.selectbox(
            label="Id_Obat",
            options=user_dict,
            index=None,
            placeholder="Delete Id User...",
            disabled=False
        )

        # Submit
        submitted = st.form_submit_button("Delete")
        if submitted:
            if not selected_id_user:
                st.warning("Harap pilih user yang ingin dihapus", icon="⚠️")
                return


            # Insert data
            try:
                cursor.callproc('spDeletePelanggan', [selected_id_user])
                connection.commit()
                st.success("Berhasil menghapus user", icon="✅")
            except Exception as e:
                st.error("Gagal menghapus user", e)
