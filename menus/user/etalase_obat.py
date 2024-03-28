import streamlit as st
import pandas as pd

def handle_button_beli(id_obat, nama_obat, harga):
    # Cek apakah obat sudah ada di keranjang
    for i in range(len(st.session_state.keranjang)):
        if st.session_state.keranjang[i]['ID Obat'] == id_obat:
            st.toast("Obat sudah ada di keranjang", icon="⚠️")
            return

    # Tambahkan ke state keranjang
    st.session_state.keranjang.append({
        "ID Obat": id_obat,
        "Nama Obat": nama_obat,
        "Harga": harga,
        "Jumlah": 1
    })
    st.toast("Berhasil menambahkan ke keranjang!", icon="✅")

def handle_button_hapus(id_obat):
    # Hapus obat dari keranjang
    for i in range(len(st.session_state.keranjang)):
        if st.session_state.keranjang[i]['ID Obat'] == id_obat:
            st.session_state.keranjang.pop(i)
            st.toast("Berhasil menghapus obat dari keranjang!", icon="✅")
            return

def handle_button_jumlah(id_obat):
    # Ubah jumlah obat di keranjang berdasarkan input number dengan key jumlah_{id_obat}
    for i in range(len(st.session_state.keranjang)):
        if st.session_state.keranjang[i]['ID Obat'] == id_obat:
            st.session_state.keranjang[i]['Jumlah'] = st.session_state[f"jumlah_{id_obat}"]
            return

def app(connection, cursor):
    st.markdown(f"Selamat berbelanja, *{st.session_state.user_data['nama']}*!")

    st.subheader("Keranjang Anda")

    if 'keranjang' not in st.session_state:
        st.session_state.keranjang = []
    
    container_keranjang = st.container(border=True)
    if st.session_state.keranjang == []:
        container_keranjang.markdown("Keranjang Anda masih kosong")
    else:
        container_item = []
        for i in range(len(st.session_state.keranjang)):
            container_item.append(st.container(border=True))
            container_item[i].markdown(f"**{st.session_state.keranjang[i]['Nama Obat']}**<br>Harga: Rp{st.session_state.keranjang[i]['Harga']}<br>", unsafe_allow_html=True)
            # Tambah input number untuk jumlah obat
            container_item[i].number_input("Jumlah", min_value=1, max_value=100, value=st.session_state.keranjang[i]['Jumlah'], key=f"jumlah_{st.session_state.keranjang[i]['ID Obat']}", on_change=handle_button_jumlah, args=(st.session_state.keranjang[i]['ID Obat'],))
            container_item[i].button("Hapus", key=f"hapus_{st.session_state.keranjang[i]['ID Obat']}", on_click=handle_button_hapus, args=(st.session_state.keranjang[i]['ID Obat'],))
        
        # tambah tombol checkout
        # if st.button("Checkout", type="primary"):
        #     st.session_state.menu_option = 2
            

    st.title("Daftar Obat")
    search = st.text_input('Cari obat:', key='search_obat')

    # Search obat jika ada input search
    if search:
        cursor.execute(
            """
            SELECT id_obat AS 'ID Obat', nama_obat AS 'Nama Obat', harga AS 'Harga', 
            stok AS 'Stok', nama_jenis_obat AS 'Jenis Obat', CONCAT(persentase_diskon, '%') AS 'Diskon', 
            nama_satuan AS 'Nama Satuan' FROM obat
            JOIN jenis_obat ON obat.id_jenis_obat = jenis_obat.id_jenis_obat
            JOIN diskon ON obat.id_diskon = diskon.id_diskon
            JOIN satuan ON obat.id_satuan = satuan.id_satuan
            WHERE nama_obat LIKE %s
            ORDER BY nama_obat
            """,
            (f"%{search}%",)
        )
    else:
        cursor.execute(
                """
                SELECT id_obat AS 'ID Obat', nama_obat AS 'Nama Obat', harga AS 'Harga', 
                stok AS 'Stok', nama_jenis_obat AS 'Jenis Obat', CONCAT(persentase_diskon, '%') AS 'Diskon', 
                nama_satuan AS 'Nama Satuan' FROM obat
                JOIN jenis_obat ON obat.id_jenis_obat = jenis_obat.id_jenis_obat
                JOIN diskon ON obat.id_diskon = diskon.id_diskon
                JOIN satuan ON obat.id_satuan = satuan.id_satuan
                ORDER BY nama_obat
                """
        )
    data = cursor.fetchall()
    
    if search:
        # Jika tidak ada obat yang ditemukan
        if data == []:
            st.write(f'Tidak ada obat yang ditemukan untuk "{search}"')
        else:
            st.write(f'Menampilkan hasil untuk "{search}"')


    # change data to list of dictionary
    data = [dict(zip(cursor.column_names, row)) for row in data]

    # split data
    data1 = data[::3]
    data2 = data[1::3]
    data3 = data[2::3]
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        container1 = []
        for i in range(len(data1)):
            container1.append(st.container(border=True))
            container1[i].image(f"https://cdn4.vectorstock.com/i/1000x1000/59/18/medicine-bottle-icon-vector-16825918.jpg", width=50, use_column_width=True)
            container1[i].markdown(f"**{data1[i]['Nama Obat']}**<br>Rp{data1[i]['Harga']}<br>Stok: {data1[i]['Stok']}<br>Jenis Obat: {data1[i]['Jenis Obat']}<br>Satuan: {data1[i]['Nama Satuan']}<br>:green[Diskon {data1[i]['Diskon']}]<br>", unsafe_allow_html=True)
            if(data1[i]['Stok'] == 0):
                container1[i].button("Beli", key=f"beli_{data1[i]['ID Obat']}", disabled=True)
            else:
                container1[i].button("Beli", key=f"beli_{data1[i]['ID Obat']}", on_click=handle_button_beli, args=(data1[i]['ID Obat'], data1[i]['Nama Obat'], data1[i]['Harga'],))
    with col2:
        container2 = []
        for i in range(len(data2)):
            container2.append(st.container(border=True))
            container2[i].image(f"https://cdn4.vectorstock.com/i/1000x1000/59/18/medicine-bottle-icon-vector-16825918.jpg", width=50, use_column_width=True)
            container2[i].markdown(f"**{data2[i]['Nama Obat']}**<br>Rp{data2[i]['Harga']}<br>Stok: {data2[i]['Stok']}<br>Jenis Obat: {data2[i]['Jenis Obat']}<br>Satuan: {data2[i]['Nama Satuan']}<br>:green[Diskon {data2[i]['Diskon']}]<br>", unsafe_allow_html=True)
            if(data2[i]['Stok'] == 0):
                container2[i].button("Beli", key=f"beli_{data2[i]['ID Obat']}", disabled=True)
            else:
                container2[i].button("Beli", key=f"beli_{data2[i]['ID Obat']}", on_click=handle_button_beli, args=(data2[i]['ID Obat'], data2[i]['Nama Obat'], data2[i]['Harga'],))
    with col3:
        container3 = []
        for i in range(len(data3)):
            container3.append(st.container(border=True))
            container3[i].image(f"https://cdn4.vectorstock.com/i/1000x1000/59/18/medicine-bottle-icon-vector-16825918.jpg", width=50, use_column_width=True)
            container3[i].markdown(f"**{data3[i]['Nama Obat']}**<br>Rp{data3[i]['Harga']}<br>Stok: {data3[i]['Stok']}<br>Jenis Obat: {data3[i]['Jenis Obat']}<br>Satuan: {data3[i]['Nama Satuan']}<br>:green[Diskon {data3[i]['Diskon']}]<br>", unsafe_allow_html=True)
            if(data3[i]['Stok'] == 0):
                container3[i].button("Beli", key=f"beli_{data3[i]['ID Obat']}", disabled=True)
            else:
                container3[i].button("Beli", key=f"beli_{data3[i]['ID Obat']}", on_click=handle_button_beli, args=(data3[i]['ID Obat'], data3[i]['Nama Obat'], data3[i]['Harga'],))
