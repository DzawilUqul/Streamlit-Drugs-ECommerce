import streamlit as st


def id_to_name():
    st.session_state.id_obat = st.session_state.nama_obat


def app(connection, cursor):
    st.title("Delete Obat")

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

        obat_dict = {option[0]: option[1] for option in obat_list}
        selected_id_obat = st.selectbox(
            label="Id_Obat",
            options=obat_dict,
            index=None,
            placeholder="Delete Id Obat...",
            disabled=False
        )

        # Submit
        submitted = st.form_submit_button("Delete")
        if submitted:
            if not selected_id_obat:
                st.warning("Harap pilih obat yang ingin dihapus", icon="⚠️")
                return


            # Insert data
            try:
                cursor.callproc('spDeleteProduct', [selected_id_obat])
                connection.commit()
                st.success("Berhasil menghapus obat", icon="✅")
            except Exception as e:
                st.error("Gagal menghapus obat", e)
