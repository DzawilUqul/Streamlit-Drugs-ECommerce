import streamlit as st


def app(connection, cursor):
    st.title("Edit User")

    cursor.execute(
        """
        SELECT id_pelanggan, nama_pelanggan, no_telepon, alamat, user_role, username, password FROM user
        """
    )

    user = cursor.fetchall()

    with st.form("drugs_edit_form"):
        # user_id
        cursor.execute(
            """
            SELECT id_pelanggan, nama_pelanggan FROM user
            """
        )

        user_list = cursor.fetchall()

        user_dict = {option[1]: option[0] for option in user_list}
        selected_id_user = st.selectbox(
            label="Id User",
            options=user_dict,
            index=None,
            placeholder="Edit Id User...",
            disabled=False
        )

        nama_user_renamed = st.text_input("Rename User", key="nama_user_renamed")
        no_telp = st.number_input("No Telp", min_value=0, step=1, key="no_telp")
        alamat = st.text_input("Alamat", key="alamat")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", key="password", type="password")
        confirmation_password = st.text_input("Confirmation Password", key="confirmation_password", type="password")

        role_dict = {"user": "user", "admin": "admin"}
        selected_role = st.selectbox(
            label="Role",
            options=role_dict,
            index=None,
            placeholder="Pilih role...",
        )

        # Submit
        submitted = st.form_submit_button("Update")
        if submitted:
            if not selected_id_user:
                st.warning("Harap pilih user yang ingin diubah", icon="⚠️")
                return
            if not nama_user_renamed:
                st.warning("Harap isi nama user", icon="⚠️")
                return
            if not selected_role:
                st.warning("Harap pilih role", icon="⚠️")
                return
            if not no_telp:
                st.warning("Harap isi no telp", icon="⚠️")
                return
            if not alamat:
                st.warning("Harap isi alamat", icon="⚠️")
                return
            if not username:
                st.warning("Harap isi username", icon="⚠️")
                return
            if not password:
                st.warning("Harap isi password", icon="⚠️")
                return
            if not confirmation_password:
                st.warning("Harap isi confirmation password", icon="⚠️")

            if password != confirmation_password:
                st.warning("Confirmation password tidak cocok", icon="⚠️")
                return

            if selected_id_user:
                selected_id = user_dict[selected_id_user]


            # Edit data
            print(selected_id_user, nama_user_renamed, no_telp, alamat, selected_role, username, password)
            try:
                cursor.callproc('spUpdatePelanggan', [selected_id, nama_user_renamed, no_telp, alamat,
                                                      selected_role, username, password])
                connection.commit()
                st.success("Berhasil mengedit pelanggan", icon="✅")
            except Exception as e:
                st.error("Gagal mengedit pelanggan", e)
