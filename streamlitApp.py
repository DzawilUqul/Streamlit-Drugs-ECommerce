import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

from menus.admin import data_obat, data_transaksi, insert_transaksi, data_pelanggan, data_jenis_obat
from Authentication import login_page


class App:
    def __init__(self):
        self.apps = []
        self.connection = mysql.connector.connect(
            host='localhost',
            database='penjualan_obat',
            user='root',
            password=''
        )
        self.cursor = self.connection.cursor()

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        if not hasattr(st.session_state, 'logged_in'):
            login_page.main(self.connection, self.cursor)
        else:
            # Display authenticated user's page here
            # st.set_page_config(
            #     page_title="Apotek"
            # )

            app_options = [app["title"] for app in self.apps]
            app_functions = {app["title"]: app["function"] for app in self.apps}

            with st.sidebar:
                selected_app = option_menu(
                    menu_title="Menu",
                    options=app_options,
                    icons=["capsule", "capsule", "person-fill", "receipt-cutoff", "plus-circle-fill"],
                    default_index=0
                )

            app_functions[selected_app](self.connection, self.cursor)

    def __del__(self):
        self.connection.close()


app = App()

app.add_app("Data Obat", data_obat.app)
app.add_app("Data Jenis Obat", data_jenis_obat.app)
app.add_app("Data Pelanggan", data_pelanggan.app)
app.add_app("Data Transaksi", data_transaksi.app)
app.add_app("Insert Transaksi", insert_transaksi.app)
app.add_app("Logout", login_page.logout_function)

app.run()
