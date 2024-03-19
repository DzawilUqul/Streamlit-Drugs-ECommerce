import mysql.connector
import pandas as pd
from mysql.connector import Error

connection = None
cursor = None


def spInsertTransaction(cursor):
    user_id = int(input("id User : "))
    date = input("Tanggal : ")
    product_id = int(input("id Produk : "))
    quantity = int(input("Jumlah : "))
    cursor.callproc('spInsertTransaction', [user_id, date, product_id, quantity])
    for result in cursor.stored_results():
        print(result.fetchall())


try:
    connection = mysql.connector.connect(host='localhost', database='penjualan_obat', user='root', password='')
    cursor = connection.cursor()

    # spInsertTransaction(cursor)
    pd.read_sql("SELECT * FROM obat", connection)
except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("MySQL connection is not closed")
