import tkinter as tk
from tkinter import ttk, messagebox
from utils import baca_file, tulis_file, tulis_history

def halaman_tambah_data(root):
    tambah_window = tk.Toplevel(root)
    tambah_window.title("Tambah Data Ikan")
    tambah_window.configure(bg="#003366")

    # Label untuk penambahan data
    label_tambah = tk.Label(tambah_window, text="Pilih Data Ikan yang ingin ditambah:", bg="#003366", fg="white")
    label_tambah.grid(row=0, column=0, padx=10, pady=5)

    # Dropdown untuk memilih tipe data
    dropdown_tambah = ttk.Combobox(tambah_window)
    dropdown_tambah['values'] = ["Semua Data"]  # hanya satu pilihan untuk menambah semua data
    dropdown_tambah.grid(row=0, column=1, padx=10, pady=5)

    # Label dan entry untuk semua data
    label_nama_ikan = tk.Label(tambah_window, text="Nama Ikan:", bg="#003366", fg="white")
    label_nama_ikan.grid(row=1, column=0, padx=10, pady=5)
    entry_nama_ikan = tk.Entry(tambah_window)
    entry_nama_ikan.grid(row=1, column=1, padx=10, pady=5)

    label_jenis_ikan = tk.Label(tambah_window, text="Jenis Ikan:", bg="#003366", fg="white")
    label_jenis_ikan.grid(row=2, column=0, padx=10, pady=5)
    entry_jenis_ikan = tk.Entry(tambah_window)
    entry_jenis_ikan.grid(row=2, column=1, padx=10, pady=5)

    label_warna_ikan = tk.Label(tambah_window, text="Warna Ikan:", bg="#003366", fg="white")
    label_warna_ikan.grid(row=3, column=0, padx=10, pady=5)
    entry_warna_ikan = tk.Entry(tambah_window)
    entry_warna_ikan.grid(row=3, column=1, padx=10, pady=5)

    label_waktu = tk.Label(tambah_window, text="Waktu (jam):", bg="#003366", fg="white")
    label_waktu.grid(row=4, column=0, padx=10, pady=5)
    entry_waktu = tk.Entry(tambah_window)
    entry_waktu.grid(row=4, column=1, padx=10, pady=5)

    label_jarak = tk.Label(tambah_window, text="Jarak (km):", bg="#003366", fg="white")
    label_jarak.grid(row=5, column=0, padx=10, pady=5)
    entry_jarak = tk.Entry(tambah_window)
    entry_jarak.grid(row=5, column=1, padx=10, pady=5)

    def tambah_data():
        # Ambil data dari semua entry
        nama_ikan = entry_nama_ikan.get()
        jenis_ikan = entry_jenis_ikan.get()
        warna_ikan = entry_warna_ikan.get()
        waktu = entry_waktu.get()
        jarak = entry_jarak.get()
        
        # Cek apakah ada data yang ingin ditambahkan
        data_added = False
        
        if nama_ikan:
            daftar_nama_ikan = baca_file('nama_ikan.txt')
            daftar_nama_ikan.append([nama_ikan])
            tulis_file('nama_ikan.txt', daftar_nama_ikan)
            tulis_history(f"Menambahkan Nama Ikan: {nama_ikan}")
            data_added = True

        if jenis_ikan:
            daftar_jenis_ikan = baca_file('nama_jenis.txt')
            daftar_jenis_ikan.append([jenis_ikan])
            tulis_file('nama_jenis.txt', daftar_jenis_ikan)
            tulis_history(f"Menambahkan Jenis Ikan: {jenis_ikan}")
            data_added = True

        if warna_ikan:
            daftar_warna_ikan = baca_file('nama_warna.txt')
            daftar_warna_ikan.append([warna_ikan])
            tulis_file('nama_warna.txt', daftar_warna_ikan)
            tulis_history(f"Menambahkan Warna Ikan: {warna_ikan}")
            data_added = True

        if waktu and jarak:
            daftar_jarak_tempuh = baca_file('jarak_tempuh.txt')
            daftar_jarak_tempuh.append([waktu, jarak])
            tulis_file('jarak_tempuh.txt', daftar_jarak_tempuh)
            tulis_history(f"Menambahkan Jarak Tempuh: Waktu {waktu} jam, Jarak {jarak} km")
            data_added = True
            
        if data_added:
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang ditambahkan!")

    tambah_button = tk.Button(tambah_window, text="Tambah Data Ikan", command=tambah_data, bg="white", fg="black")
    tambah_button.grid(row=6, columnspan=2, pady=10)

    tombol_keluar = tk.Button(tambah_window, text="Keluar", command=tambah_window.destroy, bg="red", fg="white")
    tombol_keluar.grid(row=7, columnspan=2, pady=10)

