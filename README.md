# Kel_1_Pemesanan_Makanan_dan_Minuman_PBO_VIII
Tugas Pemrograman Berorientasi Objek
----------------------------------------------------------------------------
LAPORAN APLIKASI PEMESANAN MAKANAN ONLINE BERBASIS OOP DAN GUI
Disusun guna memenuhi tugas mata kuliah Pemrograman Berorientasi Objek

Dosen Pengampu:
Irma Handayani, S.Kom., M.Cs.

 

Oleh:
Kelompok 1
Muhammad Alwin Prima			5220411271
Sirajudin					        5220411276
Syahrul Ramadhan			    5220411289
Abimanyu Putra Aria		  	5220411291
Haikal Fawwaz Karim			  5220411302

PROGRAM STUDI INFORMATIKA
FAKULTAS SAINS DAN TEKNOLOGI
UNIVERSITAS TEKNOLOGI YOGYAKARTA
2024

KATA PENGANTAR

Puji syukur kami panjatkan kepada Tuhan Yang Maha Esa, karena atas limpahan rahmatnya penyusun dapat menyelesaikan laporan ini tepat waktu tanpa ada halangan yang berarti dan sesuai dengan harapan.
Ucapan terima kasih kami sampaikan kepada ibu Irma Handayani, S.Kom., M.Cs. sebagai dosen pengampu mata kuliah Pemrograman Berorientasi Objek yang telah membantu memberikan arahan dan pemahaman dalam penyusunan makalah ini.
Kami menyadari bahwa dalam penyusunan laporan ini masih banyak kekurangan karena keterbatasan kami. Maka dari itu penyusun sangat mengharapkan kritik dan saran untuk menyempurnakan laporan ini. Semoga apa yang ditulis dapat bermanfaat bagi semua pihak yang membutuhkan. 


Yogyakarta, 1 Januari 2024


Kelompok 1


BAB I
LATAR BELAKANG

Dalam era digital yang terus berkembang, teknologi informasi memainkan peran penting dalam memudahkan berbagai aspek kehidupan sehari-hari. Salah satunya dalam dunia kuliner. Pemesanan makanan secara online telah menjadi tren yang populer dan memudahkan konsumen.

Dalam konteks ini, penggunaan paradigma Object-Oriented Programming (OOP) dan Graphical User Interface (GUI) menjadi suatu keharusan. OOP memungkinkan pengembang perangkat lunak untuk mengorganisasi dan mengelola kode dengan cara yang lebih terstruktur dan modular. Dengan menggunakan OOP, kita dapat membagi fungsionalitas program menjadi objek-objek yang saling terkait, meningkatkan keterbacaan, dan memudahkan pemeliharaan kode.

Selain itu, GUI memberikan pengalaman pengguna yang lebih interaktif dan intuitif. Dengan tampilan grafis, pengguna dapat dengan mudah berinteraksi dengan program tanpa harus memahami atau mengetikkan perintah-perintah secara manual. Hal ini sangat penting dalam pengembangan aplikasi pemesanan makanan, di mana kenyamanan dan kecepatan dalam melakukan transaksi menjadi prioritas utama.

Tujuan dari laporan ini adalah untuk menjelaskan perancangan program pemesanan makanan berbasis OOP dan GUI. Dengan mengintegrasikan konsep OOP, diharapkan program dapat dikembangkan dengan struktur yang jelas, mudah dipahami, dan dapat diadaptasi untuk memenuhi kebutuhan masa depan. Sementara itu, penggunaan GUI diharapkan dapat meningkatkan antarmuka pengguna, memberikan pengalaman pengguna yang lebih baik, dan meningkatkan efisiensi dalam proses pemesanan makanan.

BAB II
DEMONSTRASI

Sebelum memulai perancangan program, dilakukan analisis kebutuhan untuk memahami secara mendalam fitur-fitur yang dibutuhkan oleh aplikasi pemesanan makanan. Hal ini mencakup antarmuka pengguna, proses pemesanan, manajemen menu, pengelolaan pelanggan, dan integrasi dengan sistem pembayaran.

Dalam perancangan ini, dipilih bahasa pemrograman yang mendukung OOP dan memiliki kemampuan untuk mengembangkan GUI dengan mudah. Yaitu, penggunaan Python dengan library Tkinter untuk GUI.

Pada penyusunan sistem GUI sendiri digunakan beberapa elemen, seperti:
•	Label: Digunakan untuk menampilkan teks atau informasi penting kepada pengguna, seperti daftar menu atau petunjuk.
•	OptionMenu: Memberikan pengguna pilihan untuk memilih menu makanan dan minuman yang tersedia.
•	Entry: Digunakan sebagai kotak input di mana pengguna dapat memasukkan informasi seperti jumlah pesanan makanan atau minuman.
•	Button: Tombol-tombol ini memungkinkan pengguna untuk melakukan aksi tertentu, seperti menghitung total harga pesanan atau melakukan pemesanan




2.1 Penggunaan Class
Program yang kami rancang setidaknya menggunakan dua buah class, dengan rincian satu parent class dan satu child class. Dengan demikian, konsep pemrograman yang dipakai ialah inheritance (pewarisan).
Class pertama adalah PemesananMakananMinuman, class ini menyiapkan elemen-elemen GUI seperti label, dropdown, entry, dan tombol. Mendefinisikan dua dictionary menu_makanan dan menu_minuman sebagai menu dan harga makanan serta minuman. Serta menginisialisasi label dan warna latar belakang jendela. Class ini berisi method hitung_total yang berperan untuk mengambil input dari dropdown menu, entry jumlah pesanan, dan menghitung total harga pesanan. Juga menangani kasus ketika input jumlah pesanan bukan angka. Dan menampilkan total harga pada label. Adapun method pesan juga berguna untuk mengambil input dari dropdown menu, entry jumlah pesanan, dan menampilkan pesan pesanan. Menangani kasus ketika input jumlah pesanan bukan angka, serta menampilkan pesan pemesanan pada label dan memberikan notifikasi dengan messagebox.


Berikut Sepenggal kode pada class PemesananMakananMinuman:
import tkinter as tk
from tkinter import messagebox

class PemesananMakananMinuman:

    def __init__(self, root):
        # Inisialisasi jendela utama
        self.root = root
        self.root.title("Pemesanan Makanan dan Minuman")
        self.root.configure(bg="#ADD8E6")  # Warna latar belakang biru muda

        # Menu makanan beserta harga
        self.menu_makanan = {
            "Tidak Memilih": 0,  # Opsi baru
            "Mie Ayam (10K)": 10000,
            "Bakso (12K)": 12000,
            "Soto (10K)": 10000,
            "Magelangan (12K)": 12000,
            "Geprek (12K)": 12000
        }
        # Menu minuman beserta harga
        self.menu_minuman = {
            "Tidak Memilih": 0,  # Opsi baru
            "Jeruk Es/Panas (4K)": 4000,
            "Teh Es/Panas (3K)": 3000,
            "Es Kepal Milo (7K)": 7000,
            "Es Buah (5K)": 5000,
            "Air Es (1K)": 1000
        }
        
Class kedua adalah PemesananOnline yang  merupakan turunan dari class PemesananMakananMinuman. Konstruktor __init__ pada class ini berperan dalam menambahkan elemen GUI untuk metode pembayaran, seperti dropdown untuk pilihan "Transfer Bank", "E-Wallet", dan "Kartu Kredit". Method pada class ini yaitu pesan berguna untuk menambahkan logika khusus untuk pesanan online, termasuk metode pembayaran serta menampilkan pesan pesanan dengan detail tambahan pembayaran jika ada.

Berikut Sepenggal kode pada class PemesananOnline:

class PemesananOnline(PemesananMakananMinuman):

    def __init__(self, root):
        # Memanggil konstruktor kelas induk
        super().__init__(root)

        # Menambahkan elemen GUI untuk metode pembayaran
        self.label_metode_pembayaran = tk.Label(root, text="Metode Pembayaran:", bg="#ADD8E6", fg="black")
        self.label_metode_pembayaran.grid(row=8, column=0, padx=10, pady=5)
        self.dropdown_metode_pembayaran = tk.StringVar(root)
        self.dropdown_metode_pembayaran.set("Transfer Bank")  # Nilai default
        self.menu_metode_pembayaran_option = tk.OptionMenu(root, self.dropdown_metode_pembayaran, "Transfer Bank", "E-Wallet", "Kartu Kredit")
        self.menu_metode_pembayaran_option.grid(row=8, column=1, padx=10, pady=5)



2.2 Pemanggilan aplikasi
Untuk menjalankan serta menampilkan antarmuka aplikasi, maka perlu dituliskan blok kode sebagai berikut.
  
Kode ini berfungsi untuk membuat instance dari kelas PemesananOnline, membuat objek root untuk menampilkan GUI, dan memanggil metode mainloop() untuk menjalankan aplikasi secara terus-menerus hingga ditutup.

Apabila kode di atas dijalankan, maka tercipta antarmuka pengguna untuk memasukkan pesanan makanan dan minuman, menghitung total harga, dan memberikan notifikasi untuk pesanan diterima. Program ini juga memberikan opsi untuk metode pembayaran. Program dapat dilihat pada gambar berikut.


-------------------------------- GAMBAR OUTPUT GUI ADA PADA LAPORAN-------------------------------


BAB III
KESIMPULAN

Program pemesanan makanan dan minuman berbasis GUI dan OOP dengan menggunakan Tkinter berhasil memberikan solusi yang efisien dan user-friendly. Antarmuka pengguna yang intuitif, desain yang bersih, dan penerapan konsep pemrograman berorientasi objek (OOP) menjadikan program ini mudah dipahami dan dikelola. Kemampuannya dalam mengelola pesanan makanan dan minuman, menghitung total harga, dan memberikan notifikasi pesanan diterima merupakan fitur-fitur yang signifikan. Kelas turunan PemesananOnline juga memperluas fungsionalitas dengan menambahkan opsi metode pembayaran. Program ini tidak hanya memberikan pengalaman pengguna yang positif tetapi juga menciptakan dasar yang solid untuk pengembangan lebih lanjut, seperti penambahan fitur atau integrasi dengan sistem pembayaran online. Dengan demikian, program ini menjadi solusi komprehensif dalam mengotomatisasi proses pemesanan makanan dan minuman, baik secara konvensional maupun online.

Link github Program GUI : 
https://github.com/xynatez/Kel_1_Pemesanan_Makanan_dan_Minuman_PBO_VIII


-------------------------------------------------------------------------------------------------







