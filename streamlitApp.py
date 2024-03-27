import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

from menus.admin import data_obat, data_transaksi, insert_transaksi, data_pelanggan, data_jenis_obat
from menus.user import etalase_obat, checkout, pesanan_saya, edit_profile
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

    def add_app(self, title, func, icon):
        self.apps.append({
            "title": title,
            "function": func,
            "icon": icon
        })

    def run(self):
        st.set_page_config(page_title="Appotek")

        if not hasattr(st.session_state, 'logged_in'):
            login_page.main(self.connection, self.cursor)
        else:
            if st.session_state.user_data["role"] == "user":
                # == Halaman User ==

                self.add_app("Etalase Obat", etalase_obat.app, icon="capsule")
                self.add_app("Checkout", checkout.app, icon="cart3")
                self.add_app("Pesanan Saya", pesanan_saya.app, icon="receipt-cutoff")
                self.add_app("Edit Profile", edit_profile.app, icon="person-fill")  
                self.add_app("Logout", login_page.logout_function, icon="box-arrow-right")

                app_options = [app["title"] for app in self.apps]
                app_functions = {app["title"]: app["function"] for app in self.apps}
                app_icons = [app["icon"] for app in self.apps]

                with st.sidebar:
                    selected_app = option_menu(
                        menu_title="Menu",
                        options=app_options,
                        icons=app_icons,
                        default_index=0
                    )

                app_functions[selected_app](self.connection, self.cursor)
                
            else:
                # == Halaman Admin ==

                self.add_app("Insert Transaksi", insert_transaksi.app, icon="plus-circle-fill")
                self.add_app("Data Obat", data_obat.app, icon="capsule")
                self.add_app("Data Jenis Obat", data_jenis_obat.app, icon="capsule")
                self.add_app("Data Pelanggan", data_pelanggan.app, icon="person-fill")
                self.add_app("Data Transaksi", data_transaksi.app, icon="receipt-cutoff")
                self.add_app("Logout", login_page.logout_function, icon="box-arrow-right")

                app_options = [app["title"] for app in self.apps]
                app_functions = {app["title"]: app["function"] for app in self.apps}
                app_icons = [app["icon"] for app in self.apps]

                with st.sidebar:
                    selected_app = option_menu(
                        menu_title="Menu",
                        options=app_options,
                        icons=app_icons,
                        default_index=0
                    )

                app_functions[selected_app](self.connection, self.cursor)

    def __del__(self):
        self.connection.close()


app = App()
app.run()
