import tkinter as tk
from tkinter import messagebox
from pages import halaman_tampilkan_data_ikan, halaman_tambah_data, halaman_hapus_data, halaman_history_call

# Setup main window
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.geometry("400x400")
root.configure(bg="#003366")

# Header aplikasi
header_label = tk.Label(root, text="Aplikasi Data Ikan", font=("Arial", 24), bg="#003366", fg="white")
header_label.pack(pady=20)

# Tombol untuk menampilkan data
tampilkan_button = tk.Button(root, text="Tampilkan Data Ikan", command=halaman_tampilkan_data_ikan, bg="white", fg="black")
tampilkan_button.pack(pady=10)

# Tombol untuk menambah data ikan
tambah_button = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, bg="white", fg="black")
tambah_button.pack(pady=10)

# Tombol untuk menghapus data ikan
hapus_button = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, bg="white", fg="black")
hapus_button.pack(pady=10)

# Tombol untuk melihat history call
history_button = tk.Button(root, text="Lihat History Call", command=halaman_history_call, bg="white", fg="black")
history_button.pack(pady=10)

# Tombol untuk keluar aplikasi
keluar_button = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
keluar_button.pack(pady=20)

root.mainloop()
