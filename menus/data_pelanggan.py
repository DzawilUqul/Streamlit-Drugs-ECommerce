import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from menus import insert_pelanggan


def app(connection, cursor):
    # Create navbar to edit and delete customer
    selected_customer = option_menu(
        menu_title="Select Customer",
        options=["View Customer", "Add Customer", "Edit Customer", "Delete Customer"],
        orientation=["horizontal"],
        icons=["person", "person", "person", "person"],
        default_index=0
    )

    if selected_customer == "View Customer":
        cursor.execute(
            """
            SELECT id_pelanggan AS 'ID Pelanggan', nama_pelanggan AS 'Nama Pelanggan', alamat AS 'Alamat', no_telepon AS 'No. Telp' FROM pelanggan
            """
        )
        data = cursor.fetchall()

        st.title("Data Pelanggan")
        st.dataframe(pd.DataFrame(data, columns=cursor.column_names), use_container_width=True)
    elif selected_customer == "Add Customer":
        insert_pelanggan.app(connection, cursor)
    elif selected_customer == "Edit Customer":
        st.write("Edit Customer")
        # edit customer using
    elif selected_customer == "Delete Customer":
        st.write("Delete Customer")

