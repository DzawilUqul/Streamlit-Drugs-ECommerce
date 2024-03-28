import streamlit as st


def app(connection, cursor):
    st.title("Edit Jenis Obat")

    cursor.execute(
        """
        SELECT id_jenis_obat, nama_jenis_obat FROM jenis_obat
        """
    )

    obat = cursor.fetchall()

    with st.form("edit_jenis_obat_form"):
        # obat_id
        cursor.execute(
            """
            SELECT id_jenis_obat, nama_jenis_obat FROM jenis_obat
            """
        )

        jenis_obat_list = cursor.fetchall()

        jenis_obat_dict = {option[1]: option[0] for option in jenis_obat_list}
        selected_id_jenis_obat = st.selectbox(
            label="Id Jenis Obat",
            options=jenis_obat_dict,
            index=None,
            placeholder="Edit Id Jenis Obat...",
            disabled=False
        )

        nama_obat_renamed = st.text_input("Rename Jenis Obat", key="nama_jenis_obat")

        # Submit
        submitted = st.form_submit_button("Update")
        if submitted:
            if not selected_id_jenis_obat:
                st.warning("Harap pilih jenis obat yang ingin diubah", icon="⚠️")
                return
            if not nama_obat_renamed:
                st.warning("Harap isi nama jenis obat", icon="⚠️")
                return
            if selected_id_jenis_obat:
                selected_id_jenis_obat = jenis_obat_dict[selected_id_jenis_obat]

            # Insert data
            try:
                cursor.callproc('spUpdateJenisObat', [selected_id_jenis_obat, nama_obat_renamed])
                connection.commit()
                st.success("Berhasil mengedit jenis obat", icon="✅")
            except Exception as e:
                st.error("Gagal mengedit jenis obat", e)
