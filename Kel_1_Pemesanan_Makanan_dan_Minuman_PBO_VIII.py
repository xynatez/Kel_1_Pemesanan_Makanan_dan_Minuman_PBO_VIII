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

        # Elemen GUI seperti label, dropdown, entry, dan tombol
        self.label_makanan = tk.Label(root, text="Pilihan Makanan:", bg="#ADD8E6", fg="black")
        self.label_makanan.grid(row=0, column=0, padx=10, pady=5)
        self.dropdown_makanan = tk.StringVar(root)
        self.dropdown_makanan.set("Tidak Memilih")  # Nilai default
        self.menu_makanan_option = tk.OptionMenu(root, self.dropdown_makanan, *self.menu_makanan.keys())
        self.menu_makanan_option.grid(row=0, column=1, padx=10, pady=5)

        self.label_minuman = tk.Label(root, text="Pilihan Minuman:", bg="#ADD8E6", fg="black")
        self.label_minuman.grid(row=1, column=0, padx=10, pady=5)
        self.dropdown_minuman = tk.StringVar(root)
        self.dropdown_minuman.set("Tidak Memilih")  # Nilai default
        self.menu_minuman_option = tk.OptionMenu(root, self.dropdown_minuman, *self.menu_minuman.keys())
        self.menu_minuman_option.grid(row=1, column=1, padx=10, pady=5)

        self.label_jumlah_makanan = tk.Label(root, text="Jumlah Pesanan Makanan:", bg="#ADD8E6", fg="black")
        self.label_jumlah_makanan.grid(row=2, column=0, padx=10, pady=5)
        self.entry_jumlah_makanan = tk.Entry(root)
        self.entry_jumlah_makanan.grid(row=2, column=1, padx=10, pady=5)

        self.label_jumlah_minuman = tk.Label(root, text="Jumlah Pesanan Minuman:", bg="#ADD8E6", fg="black")
        self.label_jumlah_minuman.grid(row=3, column=0, padx=10, pady=5)
        self.entry_jumlah_minuman = tk.Entry(root)
        self.entry_jumlah_minuman.grid(row=3, column=1, padx=10, pady=5)

        self.button_hitung = tk.Button(root, text="Hitung Total", command=self.hitung_total, bg="#00FFFF", fg="black", bd=0, relief="flat")
        self.button_hitung.grid(row=4, columnspan=2, pady=10)

        self.label_total = tk.Label(root, text="Total Harga: Rp 0.00", bg="#ADD8E6", fg="black", font=("Times New Roman", 12, "bold"))
        self.label_total.grid(row=5, columnspan=2)

        self.button_pesan = tk.Button(root, text="Pesan", command=self.pesan, bg="#00FFFF", fg="black", bd=0, relief="flat")
        self.button_pesan.grid(row=6, columnspan=2, pady=10)

        self.label_pesanan = tk.Label(root, text="", bg="#ADD8E6", fg="black")
        self.label_pesanan.grid(row=7, columnspan=2)

    def hitung_total(self):
        # Mengambil input dari pengguna dan menghitung total harga pesanan
        makanan = self.dropdown_makanan.get()
        minuman = self.dropdown_minuman.get()
        jumlah_pesanan_makanan_str = self.entry_jumlah_makanan.get()
        jumlah_pesanan_minuman_str = self.entry_jumlah_minuman.get()

        try:
            jumlah_pesanan_makanan = int(jumlah_pesanan_makanan_str)
            jumlah_pesanan_minuman = int(jumlah_pesanan_minuman_str)

            harga_makanan = self.menu_makanan.get(makanan, 0)
            harga_minuman = self.menu_minuman.get(minuman, 0)
            total_harga = (harga_makanan * jumlah_pesanan_makanan) + (harga_minuman * jumlah_pesanan_minuman)
            self.label_total.config(text=f"Total Harga: Rp {total_harga:.2f}")
        except ValueError:
            print("Jumlah pesanan harus berupa angka.")

    def pesan(self):
        # Mengambil input dari pengguna dan menampilkan pesanan beserta total harga
        # Menampilkan pesan pemesanan pada GUI dan menunjukkan pesan konfirmasi
        makanan = self.dropdown_makanan.get()
        minuman = self.dropdown_minuman.get()
        jumlah_pesanan_makanan_str = self.entry_jumlah_makanan.get()
        jumlah_pesanan_minuman_str = self.entry_jumlah_minuman.get()

        try:
            jumlah_pesanan_makanan = int(jumlah_pesanan_makanan_str)
            jumlah_pesanan_minuman = int(jumlah_pesanan_minuman_str)

            harga_makanan = self.menu_makanan.get(makanan, 0)
            harga_minuman = self.menu_minuman.get(minuman, 0)
            total_harga = (harga_makanan * jumlah_pesanan_makanan) + (harga_minuman * jumlah_pesanan_minuman)

            pesan_str = f"Anda memesan {jumlah_pesanan_makanan} {makanan} dan {jumlah_pesanan_minuman} {minuman}. Total harga pesanan Anda adalah Rp {total_harga:.2f}. Terima kasih atas pesanan Anda!"
            self.label_pesanan.config(text=pesan_str)

            print(pesan_str)
            messagebox.showinfo("Pesan Diterima", "Pesanan Anda Telah Diterima dengan senang hati!")
        except ValueError:
            print("Jumlah pesanan harus berupa angka.")

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

        # Mengonfigurasi ulang tombol-tombol untuk tampilan yang lebih bersih

    def pesan(self):
        # Menambahkan logika khusus untuk pesanan online, termasuk metode pembayaran
        # Menampilkan pesan pemesanan dengan detail tambahan pembayaran jika ada
        makanan = self.dropdown_makanan.get()
        minuman = self.dropdown_minuman.get()
        jumlah_pesanan_makanan_str = self.entry_jumlah_makanan.get()
        jumlah_pesanan_minuman_str = self.entry_jumlah_minuman.get()

        try:
            jumlah_pesanan_makanan = int(jumlah_pesanan_makanan_str)
            jumlah_pesanan_minuman = int(jumlah_pesanan_minuman_str)

            if makanan == "Tidak Memilih" and minuman == "Tidak Memilih":
                pesan_str = "Tidak memesan makanan dan Tidak memesan minuman. Total harga pesanan Anda adalah Rp 0.00. Terima kasih atas pesanan Anda! Tidak ada Pembayaran."
            else:
                if makanan == "Tidak Memilih":
                    pesan_makanan = "Tidak memesan makanan"
                    harga_makanan = 0
                else:
                    pesan_makanan = f"Anda memesan {jumlah_pesanan_makanan} {makanan}"
                    harga_makanan = self.menu_makanan.get(makanan, 0)

                if minuman == "Tidak Memilih":
                    pesan_minuman = "Tidak memesan minuman"
                    harga_minuman = 0
                else:
                    pesan_minuman = f"Anda memesan {jumlah_pesanan_minuman} {minuman}"
                    harga_minuman = self.menu_minuman.get(minuman, 0)

                total_harga = (harga_makanan * jumlah_pesanan_makanan) + (harga_minuman * jumlah_pesanan_minuman)

                pesan_str = f"{pesan_makanan} dan {pesan_minuman}. Total harga pesanan Anda adalah Rp {total_harga:.2f}. Terima kasih atas pesanan Anda!"

                if makanan != "Tidak Memilih" or minuman != "Tidak Memilih":
                    pesan_str += f" Pembayaran dapat dilakukan melalui {self.dropdown_metode_pembayaran.get()}."

            self.label_pesanan.config(text=pesan_str)

            print(pesan_str)
            messagebox.showinfo("Pesan Diterima", "Pesanan Anda Telah Diterima dengan senang hati!")
        except ValueError:
            print("Jumlah pesanan harus berupa angka.")

if __name__ == "__main__":
    # Membuat instance dari kelas PemesananOnline
    root = tk.Tk()
    app = PemesananOnline(root)
    root.mainloop()
