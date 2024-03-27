import streamlit as st


def app(connection, cursor):
    st.title("Sign Up")
    with st.form("my_form"):
        nama_pelanggan = st.text_input("Nama Pelanggan : ")

        alamat = st.text_input("Alamat : ")

        no_telp = st.text_input("No. Telp : ")

        username = st.text_input("Username : ")

        password = st.text_input("Password : ", type="password")

        confirm_password = st.text_input("Confirm Password : ", type="password")

        role_dict = {"user": "user", "admin": "admin"}
        selected_role = st.selectbox(
            label="Role",
            options=["user", "admin"],
            index=None,
            placeholder="Pilih role...",
        )

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
            if not no_telp.isdigit():
                st.warning("No. telp harus berupa angka", icon="⚠️")
                return
            if not username:
                st.warning("Harap masukkan username", icon="⚠️")
                return
            if not password:
                st.warning("Harap masukkan password", icon="⚠️")
                return
            if not confirm_password:
                st.warning("Harap masukkan konfirmasi password", icon="⚠️")
                return
            if password != confirm_password:
                st.warning("Konfirmasi password tidak cocok", icon="⚠️")
                return
            if not selected_role:
                st.warning("Harap masukkan role", icon="⚠️")
                return
            selected_role_id = role_dict[selected_role]

            # Insert data
            try:
                cursor.callproc('spInsertCustomer', (nama_pelanggan, no_telp, alamat, selected_role_id, username, password))
                connection.commit()
                st.success("Berhasil menambahkan pelanggan", icon="✅")
            except Exception as e:
                st.error("Gagal menambahkan pelanggan", e)
