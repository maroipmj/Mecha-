import tkinter as tk
from tkinter import ttk
from utils import baca_file, tulis_history

def halaman_tampilkan_data_ikan(root):
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")

    header_label = tk.Label(tampil_window, text="Tampilkan Data Ikan", font=("Arial", 16), bg="#003366", fg="white")
    header_label.pack(pady=10)

    # Frame untuk menampung data
    frame_data = tk.Frame(tampil_window, bg="#003366")
    frame_data.pack(pady=20)

    # Label untuk menampilkan semua data
    data_label = tk.Label(frame_data, text="", bg="#003366", fg="white", justify=tk.LEFT)
    data_label.pack()

    def tampil_data():
        # Membaca data dari masing-masing file
        nama_ikan = baca_file('nama_ikan.txt')
        jenis_ikan = baca_file('nama_jenis.txt')
        warna_ikan = baca_file('nama_warna.txt')
        jarak_tempuh = baca_file('jarak_tempuh.txt')

        # Menyusun data untuk ditampilkan dalam format yang diinginkan
        data_strings = []
        for i in range(max(len(nama_ikan), len(jenis_ikan), len(warna_ikan), len(jarak_tempuh))):
            # Mengambil data dari setiap list, jika ada
            nama = nama_ikan[i][0] if i < len(nama_ikan) else ""
            jenis = jenis_ikan[i][0] if i < len(jenis_ikan) else ""
            warna = warna_ikan[i][0] if i < len(warna_ikan) else ""
            jarak = jarak_tempuh[i] if i < len(jarak_tempuh) else ["", ""]

            # Menggabungkan data dalam satu string
            data_strings.append(f"{nama}, {jenis}, {warna}, {jarak[0]} jam, {jarak[1]} km")

        # Menggabungkan semua string data menjadi satu
        all_data = "\n".join(data_strings)
        data_label.config(text=all_data)

        tulis_history("Menampilkan semua data ikan")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Semua Data", command=tampil_data, bg="white", fg="black")
    tombol_tampil.pack(pady=10)

    tombol_keluar = tk.Button(tampil_window, text="Keluar", command=tampil_window.destroy, bg="red", fg="white")
    tombol_keluar.pack(pady=10)
