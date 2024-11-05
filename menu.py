import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Fungsi untuk membuka file Python eksternal langsung tanpa jendela tambahan atau delay
def buka_file_py(filename):
    try:
        subprocess.Popen(["python", filename])  # Jalankan file Python yang ditentukan
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka {filename}.\nError: {str(e)}")

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Menu Utama - Data Ikan")
root.geometry("400x300")

# Membuat label judul
label_judul = tk.Label(root, text="Menu Data Ikan", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

# Membuat frame untuk tombol navigasi
frame_menu = tk.Frame(root)
frame_menu.pack(pady=20)

# Membuat tombol navigasi di frame menu
btn_ikan = tk.Button(frame_menu, text="Ikan", command=lambda: buka_file_py("ikan.py"), width=20)
btn_ikan.grid(row=0, column=0, padx=5, pady=5)

btn_jenis = tk.Button(frame_menu, text="Jenis", command=lambda: buka_file_py("jenis.py"), width=20)
btn_jenis.grid(row=1, column=0, padx=5, pady=5)

btn_warna = tk.Button(frame_menu, text="Warna", command=lambda: buka_file_py("warna.py"), width=20)
btn_warna.grid(row=2, column=0, padx=5, pady=5)

btn_transaksi = tk.Button(frame_menu, text="Transaksi", command=lambda: buka_file_py("transaksi.py"), width=20)
btn_transaksi.grid(row=3, column=0, padx=5, pady=5)

# Membuat tombol Keluar dengan background merah
btn_keluar = tk.Button(frame_menu, text="Keluar", command=keluar_aplikasi, width=20, bg="red", fg="white")
btn_keluar.grid(row=4, column=0, padx=5, pady=20)

# Menjalankan aplikasi
root.mainloop()
