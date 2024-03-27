import streamlit as st
import pandas as pd

def app(connection, cursor):
    st.title("Pesanan Saya")

    cursor.execute(
        """
        SELECT transaksi.id_transaksi, transaksi.tanggal, transaksi.total_harga
        FROM transaksi
        JOIN user ON transaksi.id_pelanggan = user.id_pelanggan
        WHERE user.id_pelanggan = %s
        ORDER BY transaksi.id_transaksi DESC
        """,
        (st.session_state.user_data["id"],)
    )
    data = cursor.fetchall()

    if data == []:
        st.markdown("Anda belum pernah melakukan transaksi")
    else:
        container_transaksi = []
        for i in range(len(data)):
            cursor.execute(
                """
                SELECT obat.nama_obat, transaksi_detail.jumlah_obat, transaksi_detail.harga_obat
                FROM transaksi_detail
                JOIN obat ON transaksi_detail.id_obat = obat.id_obat
                WHERE transaksi_detail.id_transaksi = %s
                """,
                (data[i][0],)
            )
            data_detail = cursor.fetchall()

            container_transaksi.append(st.container(border=True))
            container_transaksi[i].markdown(f"**Pesanan ke-{len(data)-i}**<br>Tanggal: {data[i][1]}<br>Total Harga: Rp{data[i][2]}<br>", unsafe_allow_html=True)
            container_transaksi[i].dataframe(pd.DataFrame(data_detail, columns=cursor.column_names), use_container_width=True, hide_index=True)
            container_transaksi[i].write("")

            # st.write(f"Transaksi {i+1}")
            # st.dataframe(pd.DataFrame(data_detail, columns=cursor.column_names), use_container_width=True, hide_index=True)
            # st.write("")

    