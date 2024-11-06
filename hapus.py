import tkinter as tk
from tkinter import ttk, messagebox
from utils import baca_file, tulis_file, tulis_history

def halaman_hapus_data(root):
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")

    label_hapus = tk.Label(hapus_window, text="Pilih Data yang ingin dihapus:", bg="#003366", fg="white")
    label_hapus.grid(row=0, column=0, padx=10, pady=5)

    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_hapus.grid(row=0, column=1, padx=10, pady=5)

    # Dropdown untuk memilih data yang akan dihapus
    label_data_lama = tk.Label(hapus_window, text="Pilih Data Lama:", bg="#003366", fg="white")
    label_data_lama.grid(row=1, column=0, padx=10, pady=5)

    dropdown_data_lama = ttk.Combobox(hapus_window)
    dropdown_data_lama.grid(row=1, column=1, padx=10, pady=5)

    # Label untuk menampilkan data sebelumnya
    label_data_sebelumnya = tk.Label(hapus_window, text="Data Sebelumnya:", bg="#003366", fg="white")
    label_data_sebelumnya.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def update_fields(event):
        data_file_mapping = {
            "Nama Ikan": 'nama_ikan.txt',
            "Jenis Ikan": 'nama_jenis.txt',
            "Warna Ikan": 'nama_warna.txt',
            "Jarak Tempuh": 'jarak_tempuh.txt'
        }

        # Ambil data dari file berdasarkan pilihan dropdown
        data = baca_file(data_file_mapping[dropdown_hapus.get()])
        if data:
            # Mengisi dropdown untuk memilih data lama
            dropdown_data_lama['values'] = [item[0] for item in data]
            dropdown_data_lama.set('')  # Reset pilihan dropdown data lama
            label_data_sebelumnya.config(text="Data Sebelumnya:")  # Reset label data sebelumnya

    dropdown_hapus.bind("<<ComboboxSelected>>", update_fields)

    def tampilkan_data_sebelumnya(event):
        data_file_mapping = {
            "Nama Ikan": 'nama_ikan.txt',
            "Jenis Ikan": 'nama_jenis.txt',
            "Warna Ikan": 'nama_warna.txt',
            "Jarak Tempuh": 'jarak_tempuh.txt'
        }

        # Tampilkan data yang dipilih sebelumnya
        data_lama = dropdown_data_lama.get()
        if data_lama:
            label_data_sebelumnya.config(text=f"Data Sebelumnya: {data_lama}")

    dropdown_data_lama.bind("<<ComboboxSelected>>", tampilkan_data_sebelumnya)

    def hapus_data():
        data_lama = dropdown_data_lama.get()
        data_file_mapping = {
            "Nama Ikan": 'nama_ikan.txt',
            "Jenis Ikan": 'nama_jenis.txt',
            "Warna Ikan": 'nama_warna.txt',
            "Jarak Tempuh": 'jarak_tempuh.txt'
        }

        if data_lama:
            data = baca_file(data_file_mapping[dropdown_hapus.get()])
            data_baru = [item for item in data if item[0] != data_lama]
            tulis_file(data_file_mapping[dropdown_hapus.get()], data_baru)
            tulis_history(f"Hapus {dropdown_hapus.get()}: {data_lama}")
            messagebox.showinfo("Sukses", f"Data {dropdown_hapus.get()} berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")

    hapus_button = tk.Button(hapus_window, text="Hapus Data", command=hapus_data, bg="white", fg="black")
    hapus_button.grid(row=3, columnspan=2, pady=10)

    tombol_keluar = tk.Button(hapus_window, text="Keluar", command=hapus_window.destroy, bg="red", fg="white")
    tombol_keluar.grid(row=4, columnspan=2, pady=10)
