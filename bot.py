#Melih Çetin / 2023

import mysql.connector
from mysql.connector import Error
import os

# MySQL veritabanı bağlantısı kurma / Set up a MySQL database connection
try:
    connection = mysql.connector.connect(
        host='localhost',
        database=input('Database Name: '),
        user=input('Username: '),
        password=input('Password: ')
    )
    if connection.is_connected():
        cursor = connection.cursor()
        print("MySQL veritabanına bağlanıldı")

        # Resim dosyalarının bulunduğu klasör / Folder with image files
        resim_klasoru = './Bitenler/Dolap'

        # Klasördeki tüm dosyaları listeleme / List all files in the folder
        resimler = os.listdir(resim_klasoru)

        for resim in resimler:
            if resim.endswith(('.jpg', '.png', '.jpeg')):  # Sadece resim dosyalarını işleme / Process image files only
                resim_adi = resim
                resim_yolu = os.path.join(resim_klasoru, resim)

                # Resim dosyasını MySQL'e yükleme / Loading the image file into MySQL
                with open(resim_yolu, "rb") as dosya:
                    resim_verisi = dosya.read()
                insert_query = "INSERT INTO dolap (urun_adi, urun_resim) VALUES (%s, %s)"
                val = (resim_adi, resim_verisi)
                cursor.execute(insert_query, val)
                connection.commit()
                print(f"{resim_adi} veritabanına yüklendi.")

except Error as e:
    print("MySQL bağlantı hatası:", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL bağlantısı kapatıldı.")
