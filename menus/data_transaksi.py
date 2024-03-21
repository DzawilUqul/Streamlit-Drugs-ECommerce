import streamlit as st
import pandas as pd
import mysql.connector

def app(connection, cursor):

    cursor.execute(
        """
        SELECT id_transaksi AS 'ID Transaksi', pelanggan.nama_pelanggan AS 'Pelanggan', tanggal AS 'Tanggal', total_harga AS 'Total Harga' FROM transaksi
        JOIN pelanggan ON transaksi.id_pelanggan = pelanggan.id_pelanggan
        ORDER BY id_transaksi
        """
    )
    data = cursor.fetchall()

    st.title("Data Transaksi")
    st.dataframe(pd.DataFrame(data, columns=cursor.column_names), hide_index=True, use_container_width=True, height=500)

    cursor.execute(
        """
        SELECT id_transaksi FROM transaksi
        ORDER BY id_transaksi
        """
    )
    transaction_ids = [str(id_tuple[0]) for id_tuple in cursor.fetchall()]


    st.subheader("Detail Transaksi")

    selected_transaction_id = st.selectbox(
            label="ID Transaksi",
            options=transaction_ids,
            index=None,
            placeholder="Pilih ID transaksi...",
        )

    if st.button("Tampilkan"):
        if selected_transaction_id:
            cursor.execute(
                """
                SELECT obat.nama_obat, transaksi_detail.harga_obat, transaksi_detail.jumlah_obat, transaksi_detail.jumlah_obat*transaksi_detail.harga_obat AS Total
                FROM transaksi_detail
                JOIN obat ON transaksi_detail.id_obat = obat.id_obat
                WHERE transaksi_detail.id_transaksi = %s
                """, (selected_transaction_id,))
            detail_data = cursor.fetchall()
            if detail_data:
                # Assuming cursor.description to get column names works similar to your initial setup
                detail_df = pd.DataFrame(detail_data, columns=[desc[0] for desc in cursor.description])
                st.dataframe(detail_df, use_container_width=True, hide_index=True)
            else:
                st.info("Tidak ada detail yang ditemukan untuk transaksi ini.", icon="ℹ️")
        else:
            st.warning("Harap pilih ID transaksi", icon="⚠️")
            return