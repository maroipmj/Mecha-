import tkinter as tk
from tkinter import messagebox
from lihatdata import lihat_data
from tambahdata import tambah_data
from editdata import edit_data
from hapusdata import hapus_data

def main_menu():
    # Membuat window utama
    root = tk.Tk()
    root.title("Aplikasi Manajemen Data Ikan")
    root.geometry("600x500")
    
    # Mengatur background menjadi biru langit
    root.configure(bg="#87CEEB")  # Warna biru langit

    # Header Data Ikan
    header_label = tk.Label(root, text="Data Ikan", font=("Arial", 24, "bold"), bg="#87CEEB", fg="black")
    header_label.pack(pady=30)

    # Fungsi untuk melihat data ikan
    def open_lihat_data():
        lihat_data()

    # Fungsi untuk menambah data ikan
    def open_tambah_data():
        tambah_data()

    # Fungsi untuk mengedit data ikan
    def open_edit_data():
        edit_data()

    # Fungsi untuk menghapus data ikan
    def open_hapus_data():
        hapus_data()

    # Fungsi untuk keluar aplikasi
    def quit_app():
        root.quit()

    # Tombol untuk Lihat Data
    btn_lihat_data = tk.Button(root, text="Lihat Data", width=20, height=2, command=open_lihat_data, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
    btn_lihat_data.pack(pady=10)

    # Tombol untuk Tambah Data
    btn_tambah_data = tk.Button(root, text="Tambah Data", width=20, height=2, command=open_tambah_data, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
    btn_tambah_data.pack(pady=10)

    # Tombol untuk Edit Data
    btn_edit_data = tk.Button(root, text="Edit Data", width=20, height=2, command=open_edit_data, bg="#FFC107", fg="white", font=("Arial", 12, "bold"))
    btn_edit_data.pack(pady=10)

    # Tombol untuk Hapus Data
    btn_hapus_data = tk.Button(root, text="Hapus Data", width=20, height=2, command=open_hapus_data, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
    btn_hapus_data.pack(pady=10)

    # Tombol untuk Menutup Aplikasi
    btn_tutup_app = tk.Button(root, text="Tutup Aplikasi", width=20, height=2, command=quit_app, bg="#9E9E9E", fg="white", font=("Arial", 12, "bold"))
    btn_tutup_app.pack(pady=20)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main_menu()
