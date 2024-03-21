import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

from menus import data_obat, data_transaksi, insert_transaksi

st.set_page_config(
    page_title="Apotek"
)

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
        app_options = [app["title"] for app in self.apps]
        app_functions = {app["title"]: app["function"] for app in self.apps}
        
        with st.sidebar:
            selected_app=option_menu(
                menu_title="Menu",
                options=app_options,
                icons=["capsule", "receipt-cutoff", "plus-circle-fill"],
                default_index=0
            )

        app_functions[selected_app](self.connection, self.cursor)

    def __del__(self):
        self.connection.close()

app = App()

app.add_app("Data Obat", data_obat.app)
app.add_app("Data Transaksi", data_transaksi.app)
app.add_app("Insert Transaksi", insert_transaksi.app)

app.run()





# if selected == "Data Obat":
#     st.title("Data Obat")
#     st.write(pd.DataFrame(data, columns=cursor.column_names))
# elif selected == "Data Transaksi":
#     cursor.execute("SELECT * FROM transaksi")
#     data = cursor.fetchall()
#     st.title("Data Transaksi")
#     st.write(pd.DataFrame(data, columns=cursor.column_names))
# elif selected == "Insert Transaksi":
#     st.title("Insert Transaksi")
#     user_id = st.number_input(
#         label="ID User : ",
#         min_value=1,
#         placeholder="ID User"
#     )
#     date = st.date_input("Tanggal : ")
#     product_id = st.number_input(
#         label="ID Produk : ",
#         min_value=1
#     )
#     quantity = st.number_input(
#         label="Jumlah : ",
#         min_value=1
#     )
#     # button
#     if st.button("Insert"):
#         try:
#             cursor.callproc('spInsertTransaction', [user_id, date, product_id, quantity])
#             connection.commit()
#             st.toast("Berhasil menambahkan transaksi", icon="✅")
#         except mysql.connector.Error as err:
#             st.toast("Gagal menambahkan transaksi. Err: " + str(err), icon="❌")