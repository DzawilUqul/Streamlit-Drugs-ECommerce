import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from menus.admin import insert_obat, edit_obat, delete_obat


def app(connection, cursor):
    # Create navbar to edit and delete customer
    selected_obat = option_menu(
        menu_title="Menu Obat",
        options=["View Obat", "Add Obat", "Edit Obat", "Delete Obat"],
        orientation=["horizontal"],
        icons=["capsule", "capsule", "capsule", "capsule"],
        default_index=0
    )

    if selected_obat == "View Obat":
        cursor.execute(
            """
            SELECT id_obat AS 'ID Obat', nama_obat AS 'Nama Obat', harga AS 'Harga', 
            stok AS 'Stok', nama_jenis_obat AS 'Jenis Obat', CONCAT(persentase_diskon, '%') AS 'Diskon', 
            nama_satuan AS 'Nama Satuan' FROM obat
            JOIN jenis_obat ON obat.id_jenis_obat = jenis_obat.id_jenis_obat
            JOIN diskon ON obat.id_diskon = diskon.id_diskon
            JOIN satuan ON obat.id_satuan = satuan.id_satuan
            ORDER BY id_obat
            """
        )
        data = cursor.fetchall()

        st.title("Data Obat")
        st.dataframe(pd.DataFrame(data, columns=cursor.column_names), use_container_width=True, hide_index=True)
    elif selected_obat == "Add Obat":
        insert_obat.app(connection, cursor)
    elif selected_obat == "Edit Obat":
        edit_obat.app(connection, cursor)
    elif selected_obat == "Delete Obat":
        delete_obat.app(connection, cursor)
