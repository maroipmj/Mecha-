# main.py
import tkinter as tk
from tampilkan import halaman_tampilkan_data_ikan
from tambah import halaman_tambah_data
from edit import halaman_edit_data
from hapus import halaman_hapus_data

root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.geometry("400x500")
root.configure(bg="#003366")

header_label = tk.Label(root, text="Aplikasi Data Ikan", font=("Helvetica", 20), bg="#003366", fg="white")
header_label.pack(pady=20)

tombol_tampilkan = tk.Button(root, text="Tampilkan Data Ikan", command=lambda: halaman_tampilkan_data_ikan(root), bg="white", fg="black")
tombol_tampilkan.pack(pady=10)

tombol_tambah = tk.Button(root, text="Tambah Data Ikan", command=lambda: halaman_tambah_data(root), bg="white", fg="black")
tombol_tambah.pack(pady=10)

tombol_edit = tk.Button(root, text="Edit Data Ikan", command=lambda: halaman_edit_data(root), bg="white", fg="black")
tombol_edit.pack(pady=10)

tombol_hapus = tk.Button(root, text="Hapus Data Ikan", command=lambda: halaman_hapus_data(root), bg="white", fg="black")
tombol_hapus.pack(pady=10)

tombol_keluar = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
tombol_keluar.pack(pady=20)

root.mainloop()
