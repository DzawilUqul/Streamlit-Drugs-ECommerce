import streamlit as st
import pandas as pd
import mysql.connector

def app(connection, cursor):
    st.title("Drugs Edit")
    
    cursor.execute(
        """
        SELECT id_obat, nama_obat, harga, stok FROM obat
        """
    )

    obat = cursor.fetchall()

    with st.form("drugs_edit_form"):
        edit_id = st.number_input("Enter ID of obat to edit (or leave blank to view data):", min_value=1)

        if edit_id:  # If user enters an ID to edit
            cursor.execute("SELECT * FROM obat WHERE id_obat = %s", (edit_id,))
            edit_data = cursor.fetchone()

            if edit_data:  # If obat with entered ID exists
                # Pre-fill edit fields with fetched data
                drugs_name = st.text_input("Nama: ", value=edit_data[1], key="drug_name")
                drugs_price = st.number_input("Harga : ", min_value= 1, value=int(edit_data[2]), max_value=99999999, key="drug_price")
                drugs_stock = st.number_input("Stok : ", value=edit_data[3], key="drug_stock")

                if st.button("Update Obat"):
                    try:
                        cursor.callproc('spEditDrugs', [edit_id, drugs_name, drugs_price, drugs_stock])
                        connection.commit()
                        st.toast("Berhasil mengedit obat", icon="✅")
                    except mysql.connector.Error as err:
                        st.toast("Gagal menambahkan transaksi. Err: " + str(err), icon="❌")
            else:
                st.warning("Obat with ID {} not found.".format(edit_id))