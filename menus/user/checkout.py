import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime

def app(connection, cursor):
    st.title("Checkout")

    
    # cek jika keranjang kosong
    if 'keranjang' not in st.session_state:
        st.session_state.keranjang = []

    if st.session_state.keranjang == []:
        st.markdown("Keranjang Anda masih kosong")
        return
    
    st.subheader("Keranjang Anda")

    # tampilkan keranjang dalam dataframe tanpa id obat
    df_keranjang = pd.DataFrame(st.session_state.keranjang)
    df_keranjang.drop(columns='ID Obat', inplace=True)
    # Tambah kolom nomor di awal
    df_keranjang.insert(0, 'No', range(1, 1 + len(df_keranjang)))
    st.dataframe(df_keranjang, use_container_width=True, hide_index=True)

    # hitung total harga obat (harga * jumlah)
    total_harga = df_keranjang['Harga'] * df_keranjang['Jumlah']
    st.markdown(f"<span style='font-size: 16px'>Total Harga</span><br> <span style='font-size: 26px'>Rp{total_harga.sum()}</span>", unsafe_allow_html=True)

    # Data pelanggan
    # ambil data pelanggan dari sql
    cursor.execute("SELECT * FROM user WHERE id_pelanggan = %s", (st.session_state.user_data['id'],))
    user_data = cursor.fetchone()

    st.subheader("Data Pembeli")
    st.markdown(
        f"""
        <table>
        <tr>
            <th>Nama</th>
            <td>{user_data[1]}</td>
        </tr>
        <tr>
            <th>No. Telp</th>
            <td>{user_data[2]}</td>
        </tr>
        <tr>
            <th>Alamat</th>
            <td>{user_data[3]}</td>
        </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # Tombol checkout
    if st.button("Selesaikan Pembayaran", key="selesaikan_pembayaran", type="primary"):
        id_user = st.session_state.user_data['id']
        data = st.session_state.keranjang
        current_date = datetime.now().strftime("%Y-%m-%d")

        try:
            connection.autocommit = False
            cursor.callproc("spInsertTransaction", [id_user, current_date])
            # Dapatkan ID transaksi terakhir
            cursor.execute("SELECT LAST_INSERT_ID()")
            transactionId = cursor.fetchone()[0]
            for i in range(len(data)):
                cursor.callproc("spInsertTransactionDetail", [transactionId, data[i]['ID Obat'], data[i]['Jumlah']])
            connection.commit()

            st.session_state.keranjang = []
            st.success("✅ Pembayaran berhasil dilakukan")
        except mysql.connector.Error as error:
            st.error(f"Failed to start transaction: {error}")
            connection.rollback()
        finally:
            connection.autocommit = True
