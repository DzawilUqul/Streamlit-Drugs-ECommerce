import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from menus.admin import (insert_obat, edit_obat, delete_obat, insert_jenis_obat, edit_jenis_obat)


def app(connection, cursor):
    # Create navbar to edit and delete customer
    selected_obat = option_menu(
        menu_title="Menu Obat",
        options=["View Jenis Obat", "Add Jenis Obat", "Edit Jenis Obat"],
        orientation=["horizontal"],
        icons=["capsule", "capsule", "capsule"],
        default_index=0
    )

    if selected_obat == "View Jenis Obat":
        cursor.execute(
            """
            SELECT * FROM jenis_obat
            """
        )
        data = cursor.fetchall()

        st.title("Data Jenis Obat")
        st.dataframe(pd.DataFrame(data, columns=cursor.column_names), use_container_width=True, hide_index=True)
    elif selected_obat == "Add Jenis Obat":
        insert_jenis_obat.app(connection, cursor)
    elif selected_obat == "Edit Jenis Obat":
        edit_jenis_obat.app(connection, cursor)
