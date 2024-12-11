import tkinter as tk
from tkinter import messagebox  # Import messagebox untuk konfirmasi
from lihatdata import lihat_data  # Import fungsi lihat_data dari file lihatdata.py
from tambahdata import tambah_data  # Import fungsi tambah_data dari file tambahdata.py
from editdata import edit_data  # Import fungsi edit_data dari file editdata.py
from hapusdata import hapus_data  # Import fungsi hapusdata dari file hapusdata.py

def main():
    root = tk.Tk()
    root.title("Program Data Ikan")
    root.configure(bg='#87CEFA')  # Latar belakang biru langit

    # Menentukan ukuran jendela
    root.geometry("600x400")  # Ukuran jendela yang lebih besar, sesuaikan sesuai kebutuhan

    # Menambahkan label header
    tk.Label(root, text="Menu Utama", font=("Arial", 18, "bold"), bg='#87CEFA').pack(pady=20)

    # Menambahkan tombol untuk membuka menu masing-masing
    tk.Button(root, text="Lihat Data", command=lihat_data, width=25, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=5)
    tk.Button(root, text="Tambah Data", command=tambah_data, width=25, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=5)
    tk.Button(root, text="Edit Data", command=edit_data, width=25, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=5)
    tk.Button(root, text="Hapus Data", command=hapus_data, width=25, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=5)

    # Menambahkan tombol untuk keluar dari aplikasi dengan konfirmasi
    def keluar_aplikasi():
        # Tampilkan dialog konfirmasi
        if messagebox.askyesno("Konfirmasi", "Yakin keluar?"):
            root.destroy()  # Menutup aplikasi jika pengguna memilih 'Yes'

    tk.Button(root, text="Keluar", command=keluar_aplikasi, width=25, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main() 